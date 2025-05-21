
from volcenginesdkwaf import WAFApi, CheckLLMResponseStreamRequest
from volcenginesdkwafruntime.models.llm_stream_session import LLMStreamSession

global_llm_send_len = 10

class WAFRuntimeApi(WAFApi):
    """继承自 WAFApi 并重写 check_llm_response_stream 方法"""
    def check_llm_response_stream(
            self,
            body: CheckLLMResponseStreamRequest,
            **kwargs
    ):
        session: LLMStreamSession = kwargs.pop('session', None)
        if session is None:
            raise ValueError("session parameter is required")
        """
        重写父类方法，增加 session 参数，实现流式内容的合并与处理

        Args:
            body: 请求体，包含 content、use_stream 和 msg_id 等信息
            session: LLM 流会话对象，用于记录流式内容和状态
            **kwargs: 其他参数，包括 async_req 等

        Returns:
            CheckLLMResponseStreamResponse: 处理结果
        """
        # 1. 拼接内容到 session.stream_buf
        if body.content:
            session.append_stream_buf(body.content)

        # 2. 处理 use_stream 为 2 或 没有msgid （第一次调用） 的情况（直接发送，不累计长度）
        if (body.use_stream == 2
                or not session.msg_id):
            # 准备请求体
            body.content = session.get_stream_buf()
            body.msg_id = session.get_msg_id()
            # 调用原始 API
            # 同步调用并处理结果
            resp = self.check_llm_response_stream_with_http_info(body, **kwargs)
            if isinstance(resp, tuple):
                response = resp[0]  # 获取元组的第一个元素
            else:
                response = resp

            # 首次调用时(没有msgid) ，保存 msg_id 到 session
            if (not session.msg_id) and response.msg_id:
                session.set_msg_id(response.msg_id)

            # 保存默认响应
            session.set_default_body(response)

            # 重置流缓冲区和发送长度
            session.set_stream_send_len(0)

            return response

        # 3. 处理 use_stream 为其他值的情况（累计长度，超过阈值才发送）
        else:
            # 如果未发送长度超过 10 个字符，调用 API
            if session.get_stream_send_len() > global_llm_send_len:
                # 准备请求体，使用 session 中的完整流内容
                body.content = session.get_stream_buf()
                body.msg_id = session.get_msg_id()
                # 调用原始 API
                if kwargs.get('async_req'):
                    return self.check_llm_response_stream_with_http_info(body, **kwargs)

                # 同步调用并处理结果
                resp = self.check_llm_response_stream_with_http_info(body, **kwargs)
                if isinstance(resp, tuple) and len(resp) > 0:
                    response = resp[0]  # 获取元组的第一个元素
                else:
                    response = resp

                # 保存默认响应
                session.set_default_body(response)

                # 重置发送长度，保留完整流内容（因为可能还有后续数据）
                session.set_stream_send_len(0)
                return response
            # 如果未发送长度不足 10 个字符，返回上次的结果
            else:
                default_body = session.get_default_body()
                if default_body:
                    return default_body
                else:
                    # 如果没有默认结果，调用一次 API（这种情况理论上不会发生，因为首次调用 use_stream 应为 0）
                    return self.check_llm_response_stream(body, **kwargs)
