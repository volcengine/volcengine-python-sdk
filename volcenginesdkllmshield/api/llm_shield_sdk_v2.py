from pydantic import BaseModel, field_validator, Field
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, date
from uuid import UUID
import requests
from requests.adapters import HTTPAdapter
import json
import os
import queue
import sys
import threading
import time
from urllib.parse import urljoin, urlencode

from ..models.llm_shield_sign import request_sign, Version, SetServiceDev, GetServiceCode

LLM_STREAM_SEND_BASE_WINDOW_V2 = 10
LLM_STREAM_SEND_EXPONENT_V2 = 2

# 客户端初始化选项 Key
OPTION_ENABLE_AICC = "EnableAicc"
OPTION_LOG_LEVEL = "LogLevel"
OPTION_REWRITE_URL = "RewriteUrl"

# 定义内容类型常量
class ContentTypeV2:
    TEXT = 1
    AUDIO = 2
    IMAGE = 3
    VIDEO = 4
    FILE = 5

# 定义决策类型常量
class DecisionTypeV2:
    PASS = 1
    BLOCK = 2
    MARK = 3
    REPLACE = 4
    OPTIMIZE = 5


# 定义用户操作常量
class UserAction:
    PASS = 1
    BLOCK = 2
    MARK = 3
    REPLACE = 4


# 定义匹配来源常量
class MatchSource:
    UNKNOWN = 0
    GLOBAL_CONTENTLIB = 1
    ADMIN_CONTENTLIB = 2
    USER_CONTENTLIB = 3


# 定义扩展字段Key常量
class ExtensionsKey:
    USER_ID = "user_id"
    RUN_ID = "run_id"
    SESSION_ID = "session_id"
    CONTEXT_ID = "context_id"
    HOOK_NAME = "hook_name"
    TRACE_ID = "trace_id"


# 定义消息结构体
class MultiPart(BaseModel):
    content: str = Field("", alias="Content")
    content_type: int = Field(ContentTypeV2.TEXT, alias="ContentType")

    class Config:
        populate_by_name = True


# 定义函数调用结构体
class FunctionCall(BaseModel):
    name: str = Field("", alias="Name")
    arguments: str = Field("", alias="Arguments")

    class Config:
        populate_by_name = True


# 定义工具调用结构体
class ToolCall(BaseModel):
    id: str = Field("", alias="ID")
    type: str = Field("", alias="Type")
    function: Optional[FunctionCall] = Field(None, alias="Function")

    class Config:
        populate_by_name = True


# 定义消息结构体
class MessageV2(BaseModel):
    role: str = Field("", alias="Role")
    content: str = Field("", alias="Content")
    content_type: int = Field(ContentTypeV2.TEXT, alias="ContentType")
    multi_part: Optional[List[MultiPart]] = Field(None, alias="MultiPart")
    tool_call_id: Optional[str] = Field(None, alias="ToolCallID")
    tool_call: Optional[List[ToolCall]] = Field(None, alias="ToolCall")

    class Config:
        populate_by_name = True


# 定义审核请求结构体
class ModerateV2Request(BaseModel):
    message: MessageV2 = Field(None, alias="Message")
    msg_id: str = Field("", alias="MsgID")
    use_stream: int = Field(0, alias="UseStream")
    scene: str = Field("", alias="Scene")
    history: List[MessageV2] = Field([], alias="History")
    extensions: Optional[Dict[str, str]] = Field(None, alias="Extensions")
    call_generate_on_optimize: Optional[bool] = Field(None, alias="CallGenerateOnOptimize")

    class Config:
        populate_by_name = True

    # 深拷贝构造方法：通过 Pydantic 序列化/反序列化实现
    def __init__(self, other=None, **data):
        # 如果传入了其他 ModerateV2Request 实例，则进行深拷贝
        if other is not None and isinstance(other, ModerateV2Request):
            # 1. 将其他实例序列化为字典（包含嵌套对象）
            other_dict = other.model_dump(by_alias=True)  # 使用 alias 键名
            # 2. 用序列化后的字典初始化当前实例（实现深拷贝）
            super().__init__(**other_dict)
        else:
            # 正常初始化逻辑
            super().__init__(**data)


# 定义风险匹配结构体
class RiskMatchV2(BaseModel):
    word: str = Field("", alias="Word")
    action: Optional[int] = Field(None, alias="Action")
    source: Optional[int] = Field(None, alias="Source")
    rule_id: Optional[Any] = Field(None, alias="RuleID")
    position: Optional["PositionInfo"] = Field(None, alias="Position")

    class Config:
        populate_by_name = True


class ImagePositionInfo(BaseModel):
    x_start: str = Field("", alias="xStart")
    y_start: str = Field("", alias="yStart")
    x_end: str = Field("", alias="xEnd")
    y_end: str = Field("", alias="yEnd")

    class Config:
        populate_by_name = True


class PositionInfo(BaseModel):
    image_position: Optional[ImagePositionInfo] = Field(None, alias="ImagePosition")

    class Config:
        populate_by_name = True


# 定义放行匹配结构体
class PermitMatchV2(BaseModel):
    word: str = Field("", alias="Word")
    action: Optional[int] = Field(None, alias="Action")
    source: Optional[int] = Field(None, alias="Source")
    rule_id: Optional[Any] = Field(None, alias="RuleID")

    class Config:
        populate_by_name = True


# 定义风险来源结构体
class SourceInfoV2(BaseModel):
    source: str = Field("", alias="Source")
    source_detail: Dict[str, str] = Field(default_factory=dict, alias="SourceDetail")

    class Config:
        populate_by_name = True


# 定义风险结构体
class RiskV2(BaseModel):
    category: str = Field("", alias="Category")
    label: str = Field("", alias="Label")
    prob: Optional[float] = Field(None, alias="Prob")
    matches: List[RiskMatchV2] = Field([], alias="Matches")
    source_infos: List[SourceInfoV2] = Field([], alias="SourceInfos")

    @field_validator('matches', mode="before")
    def convert_risk_matches_none_to_list(cls, value):
        return [] if value is None else value

    @field_validator('source_infos', mode="before")
    def convert_source_infos_none_to_list(cls, value):
        return [] if value is None else value

    class Config:
        populate_by_name = True


# 定义风险信息结构体 - 添加 None 转换
class RiskInfoV2(BaseModel):
    risks: List[RiskV2] = Field([], alias="Risks")

    @field_validator('risks', mode="before")
    def convert_none_to_list(cls, value):
        return [] if value is None else value

    class Config:
        populate_by_name = True


# 定义放行结构体
class PermitV2(BaseModel):
    category: str = Field("", alias="Category")
    label: str = Field("", alias="Label")
    prob: Optional[float] = Field(None, alias="Prob")
    matches: List[PermitMatchV2] = Field([], alias="Matches")

    @field_validator('matches', mode="before")
    def convert_permit_matches_none_to_list(cls, value):
        return [] if value is None else value

    class Config:
        populate_by_name = True


# 定义放行信息结构体 - 添加 None 转换
class PermitInfoV2(BaseModel):
    permits: List[PermitV2] = Field([], alias="Permits")

    @field_validator('permits', mode="before")
    def convert_none_to_list(cls, value):
        return [] if value is None else value

    class Config:
        populate_by_name = True


# 定义拦截详情结构体
class BlockDetailV2(BaseModel):
    class Config:
        extra = "forbid"


# 定义替换详情结构体
class ReplaceDetailV2(BaseModel):
    replacement: Optional[MessageV2] = Field(None, alias="Replacement")

    class Config:
        populate_by_name = True


# 定义决策详情结构体
class DecisionDetailV2(BaseModel):
    block_detail: Optional[BlockDetailV2] = Field(None, alias="BlockDetail")
    replace_detail: Optional[ReplaceDetailV2] = Field(None, alias="ReplaceDetail")

    class Config:
        populate_by_name = True


# 定义决策结构体
class DecisionV2(BaseModel):
    decision_type: int = Field(0, alias="DecisionType")
    decision_detail: DecisionDetailV2 = Field(default_factory=DecisionDetailV2, alias="DecisionDetail")
    decision_strategy_id: Optional[str] = Field(None, alias="DecisionStrategyID")
    hit_strategy_ids: List[str] = Field([], alias="HitStrategyIDs")

    @field_validator('hit_strategy_ids', mode="before")
    def convert_hit_strategies_none_to_list(cls, value):
        return [] if value is None else value

    class Config:
        populate_by_name = True


# 定义审核结果结构体
class ModerateV2Result(BaseModel):
    msg_id: str = Field("", alias="MsgID")
    risk_info: RiskInfoV2 = Field(default_factory=RiskInfoV2, alias="RiskInfo")
    decision: DecisionV2 = Field(default_factory=DecisionV2, alias="Decision")
    permit_info: PermitInfoV2 = Field(default_factory=PermitInfoV2, alias="PermitInfo")
    content_info: str = Field("", alias="ContentInfo")
    degraded: bool = Field(False, alias="Degraded")
    degrade_reason: str = Field("", alias="DegradeReason")

    class Config:
        populate_by_name = True


# 定义错误信息结构体
class ErrorInfo(BaseModel):
    code: str = Field("", alias="Code")
    codeN: Union[int, str] = Field("", alias="CodeN")
    message: str = Field("", alias="Message")

    class Config:
        populate_by_name = True


# 定义响应元数据结构体
class ResponseMetadata(BaseModel):
    error: Union[ErrorInfo, None] = Field(default_factory=ErrorInfo, alias="Error")
    requestId: str = Field(..., alias="RequestId")  # 添加requestId字段，映射自RequestId
    service: Union[str, None] = Field(None, alias="Service")
    action: Union[str, None] = Field(None, alias="Action")
    version: Union[str, None] = Field(None, alias="Version")
    region: Union[str, None] = Field(None, alias="Region")

    class Config:
        populate_by_name = True
        validate_by_name = True


# 定义审核响应结构体
class ModerateV2Response(BaseModel):
    response_metadata: ResponseMetadata = Field(default_factory=ResponseMetadata, alias="ResponseMetadata")
    result: Union[ModerateV2Result, None] = Field(default_factory=ModerateV2Result, alias="Result")

    class Config:
        populate_by_name = True


class ModerateV2StreamSession:
    """流式会话结构体，用于积累流式请求、存储未发送长度和默认响应体"""

    def __init__(self):
        # 用于积累流式的请求（初始为 None，对应 Go 中的指针）
        self.request: Optional[ModerateV2Request] = None
        # 未发送的长度（对应 Go 中的 StreamSendLen）
        self.stream_send_len: int = 0
        self.CurrentSendWindow = LLM_STREAM_SEND_BASE_WINDOW_V2
        # 存储默认响应体（初始为 None，对应 Go 中的指针）
        self.default_body: Optional[ModerateV2Response] = None


class ModerateV2AsyncStreamSession:
    """异步流式会话结构体，不影响原有 ModerateV2StreamSession 的调用方式"""

    def __init__(self, send_threshold: int = LLM_STREAM_SEND_BASE_WINDOW_V2):
        if send_threshold <= 0:
            raise ValueError("send_threshold must be positive")
        self.request: Optional[ModerateV2Request] = None
        self.stream_send_len: int = 0
        self.send_threshold: int = send_threshold
        self.default_body: Optional[ModerateV2Response] = None

        self.lock = threading.RLock()
        self.pending_event = threading.Event()
        self.pending_event.set()
        self.result_cond = threading.Condition(self.lock)
        self.pending_thread: Optional[threading.Thread] = None
        self.pending_request: Optional[ModerateV2Request] = None
        self.pending_result: Optional[ModerateV2Response] = None
        self.pending_error: Optional[Exception] = None
        self.need_flush_after_pending: bool = False
        self.has_last_chunk: bool = False
        self.closed: bool = False
        self.last_request_content_len: int = 0
        self.result_version: int = 0
        self.next_send_seq: int = 0
        self.pending_send_seq: Optional[int] = None
        self.cancelled_send_seq: int = -1


class GenerateStreamV2Request(BaseModel):
    """生成流V2版本的请求模型"""
    msg_id: str = Field(..., alias="MsgID", description="消息ID，表示请求的唯一标识")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "validate": {"required": True}  # 对应Go中的validate:"required"
        }


class GenerateStreamV2Response(BaseModel):
    def __init__(self, reader=None):
        self.Reader = reader


class GenerateSummarizeV2(BaseModel):
    """生成过程的总结信息模型"""
    token_cost: int = Field(0, alias="TokenCost", description="消耗的token数量")
    time_cost_ms: int = Field(0, alias="TimeCostMS", description="消耗的时长（毫秒）")

    class Config:
        populate_by_name = True


class GenerateStreamResult(BaseModel):
    """生成流V2版本的结果模型"""
    message: Optional[MessageV2] = Field(None, alias="Message", description="优化内容，isFinished为true时为空")
    is_finished: bool = Field(False, alias="IsFinished", description="标识是否结束")

    # summarize: Optional[GenerateSummarizeV2] = Field(None, alias="Summarize", description="总结信息，isFinished为true时有值")

    class Config:
        populate_by_name = True


class GenerateStreamV2ResponseData(BaseModel):
    """生成流V2版本的响应数据模型"""
    response_metadata: ResponseMetadata = Field(..., alias="ResponseMetadata", description="响应元数据")
    result: GenerateStreamResult = Field(..., alias="Result", description="生成流结果")

    class Config:
        populate_by_name = True


# 自定义带默认超时的Session子类
class SessionTimeout(requests.Session):
    def __init__(self, default_timeout=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 保存默认超时时间
        self.default_timeout = default_timeout

    # 重写核心的request方法，自动注入超时
    def request(self, method, url, **kwargs):
        # 核心逻辑：如果没手动传timeout，就用默认值
        if "timeout" not in kwargs and self.default_timeout is not None:
            kwargs["timeout"] = self.default_timeout
        # 调用父类的request方法，保持原有逻辑不变
        return super().request(method, url, **kwargs)

# 定义客户端类
class ClientV2:
    def __init__(self, url: str, ak: str, sk: str, region: str, timeout: float, options: Optional[Dict[str, Any]] = None):
        self.url = url
        self.rewrite_url = options.get(OPTION_REWRITE_URL) if options else None
        self.ak = ak
        self.sk = sk
        self.region = region
        self.http_client = SessionTimeout(default_timeout=timeout)
        self.http_client.timeout = timeout
        self.aicc_client = None
        if options and options.get(OPTION_ENABLE_AICC):
            log_level = options.get(OPTION_LOG_LEVEL, "ERROR")
            os.environ["LOG_LEVEL"] = log_level
            try:
                self.SetAiccInit()
            except Exception as e:
                print(f"[ERROR] SetAiccInit failed: {e}")
                sys.exit(1)

    def _fetch_aicc_module_conf(self):
        """
        请求 AiccModuleConf 接口，返回 (aicc_topaddr, ser_accid, ser_policy_id, ser_service_name, trn_role_info)
        """
        path = "/ctrl/aicc_module_conf"
        action = "AiccModuleConf"
        version = "2025-08-31"

        postbody = {"Version": 100}
        request_body = json.dumps(postbody).encode("utf-8")
        header = {
        }

        sign_header = request_sign(
            header, self.ak, self.sk, self.region, self.url, path, action, request_body, self.rewrite_url
        )
        resp = self.http_client.post(
                url=self.url + path + "?Action=" + action + "&Version=" + str(version),
                data=request_body,
                headers=sign_header
            )

        try:
            resp_json = resp.json()
        except Exception as e:
            raise Exception("AiccModuleConf 响应解析失败: {}".format(e))

        result = resp_json.get("Result") or {}
        if not result:
            raise Exception("AiccModuleConf 响应缺少 Result 字段: {}".format(resp_json))

        aicc_topaddr = result.get("PccUrl")
        ser_accid = result.get("AccID")
        ser_policy_id = result.get("ServerID")
        ser_service_name = result.get("ServerName")
        trn_role_info = result.get("TrnInfo")

        if not aicc_topaddr or not ser_accid or not ser_policy_id or not ser_service_name or not trn_role_info:
            raise Exception("AiccModuleConf 响应缺少必要字段: {}".format(result))

        return aicc_topaddr, ser_accid, ser_policy_id, ser_service_name, trn_role_info

    def SetAiccInit(self):
        """
        初始化 AICC Client.

        说明：AICC 属于可选能力，为避免引入额外依赖导致 SDK 纯审核场景不可用，
        这里采用懒加载方式初始化；外部需要使用 AICC 能力时，请显式调用本方法。
        """
        # 懒加载，避免 import 时强依赖 aicc 的第三方依赖
        from ..aicc import Client as AiccClient
        from ..aicc import ClientConfig as AiccClientConfig


        aicc_topaddr, ser_accid, ser_policy_id, ser_service_name, trn_role_info = self._fetch_aicc_module_conf()
        # print(f"AiccList {aicc_topaddr}, {ser_accid}, {ser_policy_id}, {ser_service_name}, {trn_role_info}")

        aicc_rftick = 1800
        aicc_seraddr = self.url

        byte_top_info = f"{{\"url\": \"{aicc_topaddr}\",\"url_rewrite\": \"{aicc_seraddr}\", \"ak\": \"{self.ak}\", \"sk\": \"{self.sk}\", \"target_uid\": \"{ser_accid}\", \"aicc_saas_trn\": \"trn:iam::{ser_accid}:role/{trn_role_info}\", \"service\": \"pcc\"}}"
        aiccConf = dict()
        aiccConf["ra_url"] = aicc_seraddr
        aiccConf["attest_interval"] = aicc_rftick
        aiccConf["ra_uid"] = ser_accid
        aiccConf["ra_policy_id"] = ser_policy_id
        aiccConf["ra_service_name"] = ser_service_name
        aiccConf["bytedance_top_info"] = byte_top_info
        self.aicc_client = AiccClient(AiccClientConfig.from_dict(aiccConf))
        if self.aicc_client is None:
            raise Exception("AICC客户端初始化失败")

    def _require_aicc_client(self):
        if self.aicc_client is None:
            raise RuntimeError("AICC Client 未初始化，请先调用 ClientV2.SetAiccInit()")
        return self.aicc_client

    def Encrypt(self, plaintext: Union[str, bytes]) -> str:
        """使用 AICC Client 加密请求数据，返回信封加密字符串。"""
        return self._require_aicc_client().encrypt(plaintext)

    def EncryptWithResponse(self, plaintext: Union[str, bytes]):
        """使用 AICC Client 加密请求数据，并返回用于解密响应的 ResponseKey。"""
        return self._require_aicc_client().encrypt_with_response(plaintext)

    def DecryptResponse(self, response_key, response: Union[str, bytes]) -> bytes:
        """使用 EncryptWithResponse 返回的 response_key 解密服务端响应。"""
        if response_key is None:
            raise ValueError("response_key 不能为空")
        return response_key.decrypt(response)

    def SetProxy(self, proxy: dict):
        if proxy:
            self.http_client.proxies = proxy
        else:
            self.http_client.proxies.clear()

    def SetConnMax(self, connMax):
        if connMax > 0:
            adapter = HTTPAdapter(
                pool_connections=connMax,  # 全局连接池数量：最多维护多少个 Host 的连接池
                pool_maxsize=connMax,   # 单 Host 最大连接数：控制并发的核心（= 目标并发数）
                pool_block=False  # 连接池满时是否阻塞：False=非阻塞（超时抛异常），True=阻塞等待
            )
            # 将适配器挂载到 Session：所有 HTTP/HTTPS 请求都使用该连接池
            self.http_client.mount("http://", adapter)
            self.http_client.mount("https://", adapter)

    def Moderate(self, request: Optional[ModerateV2Request] = None) -> ModerateV2Response:
        path = "/v2/moderate"
        action = "Moderate"

        if request is None:
            request = ModerateV2Request()

        request_body = request.model_dump_json(by_alias=True, exclude_none=True).encode("utf-8")

        header = {
        }

        sign_header = request_sign(
            header, self.ak, self.sk, self.region, self.url, path, action, request_body, self.rewrite_url
        )

        try:
            enc_req_key = None
            if self.aicc_client is not None:
                request_body, enc_req_key = self.EncryptWithResponse(request_body)

            resp = self.http_client.post(
                url=self.url + path + "?Action=" + action + "&Version=" + Version,
                data=request_body,
                headers=sign_header
            )

            if enc_req_key is not None:
                resp_body = self.DecryptResponse(enc_req_key, resp.content)
            else:
                resp_body = resp.content

            # resp_body 为 bytes/str(JSON)，不要对 bytes 调用 .json()
            try:
                response = ModerateV2Response.model_validate_json(resp_body)
            except Exception:
                # 兼容极端场景：resp_body 不是合法 JSON bytes/str
                response = ModerateV2Response.model_validate(json.loads(resp_body))
            return response

        except requests.RequestException as e:
            raise Exception(f"请求失败: {e}")
        except Exception as e:
            raise Exception(f"处理响应失败: {e}")

    def _build_stream_request_snapshot(self, request: ModerateV2Request) -> ModerateV2Request:
        return ModerateV2Request(request)

    def _get_request_content_len(self, request: Optional[ModerateV2Request]) -> int:
        if request is None or request.message is None or request.message.content is None:
            return 0
        return len(request.message.content)

    def _append_stream_request(self, request: ModerateV2Request, session) -> None:
        if session.request is None:
            session.request = ModerateV2Request(request)
        else:
            if request.message and request.message.content:
                if session.request.message is None:
                    session.request.message = MessageV2()
                session.request.message.content += request.message.content
            session.request.use_stream = request.use_stream
            if request.scene:
                session.request.scene = request.scene
            if request.extensions is not None:
                session.request.extensions = request.extensions
            if request.history:
                session.request.history = request.history

        chunk_len = self._get_request_content_len(request)
        session.stream_send_len += chunk_len

    def _send_stream_request_snapshot(self, request_snapshot: ModerateV2Request) -> ModerateV2Response:
        response = self.Moderate(request_snapshot)
        request_snapshot.msg_id = response.result.msg_id
        return response

    def _update_async_session_after_response(
            self,
            session: ModerateV2AsyncStreamSession,
            request_snapshot: ModerateV2Request,
            moderate_response: ModerateV2Response
    ) -> None:
        session.default_body = moderate_response
        session.pending_result = moderate_response
        session.pending_error = None
        session.last_request_content_len = self._get_request_content_len(request_snapshot)
        session.result_version += 1

        if session.request is not None:
            session.request.msg_id = moderate_response.result.msg_id

        current_len = self._get_request_content_len(session.request)
        new_content_len = max(0, current_len - session.last_request_content_len)
        session.need_flush_after_pending = new_content_len > 0 and (
                session.has_last_chunk or new_content_len >= session.send_threshold)
        session.result_cond.notify_all()

    def _invalidate_pending_async_send(self, session: ModerateV2AsyncStreamSession) -> None:
        if session.pending_send_seq is not None:
            session.cancelled_send_seq = max(session.cancelled_send_seq, session.pending_send_seq)

    def _is_async_send_cancelled(
            self,
            session: ModerateV2AsyncStreamSession,
            send_seq: int
    ) -> bool:
        return send_seq <= session.cancelled_send_seq

    def _run_async_stream_send(
            self,
            session: ModerateV2AsyncStreamSession,
            request_snapshot: ModerateV2Request,
            send_seq: int
    ) -> None:
        try:
            current_snapshot = request_snapshot
            while True:
                moderate_response = self._send_stream_request_snapshot(current_snapshot)
                with session.lock:
                    if self._is_async_send_cancelled(session, send_seq):
                        break
                    self._update_async_session_after_response(session, current_snapshot, moderate_response)
                    if not session.need_flush_after_pending:
                        break
                    current_snapshot = self._build_stream_request_snapshot(session.request)
                    session.pending_request = current_snapshot
                    session.pending_result = None
                    session.pending_error = None
                    session.need_flush_after_pending = False
                    session.stream_send_len = 0
                    session.last_request_content_len = self._get_request_content_len(current_snapshot)
        except Exception as e:
            with session.lock:
                if self._is_async_send_cancelled(session, send_seq):
                    session.pending_error = None
                    session.need_flush_after_pending = False
                    session.result_cond.notify_all()
                    return
                session.pending_error = e
                current_len = self._get_request_content_len(session.request)
                snapshot_len = self._get_request_content_len(session.pending_request or request_snapshot)
                new_content_len = max(0, current_len - snapshot_len)
                session.need_flush_after_pending = new_content_len > 0 and (
                        session.has_last_chunk or new_content_len >= session.send_threshold)
                session.result_cond.notify_all()
        finally:
            with session.lock:
                if session.pending_send_seq == send_seq:
                    session.pending_thread = None
                    session.pending_request = None
                    session.pending_send_seq = None
                    session.pending_event.set()
                    session.result_cond.notify_all()

    def _start_async_stream_send(
            self,
            session: ModerateV2AsyncStreamSession,
            request_snapshot: ModerateV2Request,
            sent_len: int
    ) -> None:
        send_seq = session.next_send_seq
        session.next_send_seq += 1
        session.pending_event.clear()
        session.pending_request = request_snapshot
        session.pending_result = None
        session.pending_error = None
        session.need_flush_after_pending = False
        session.stream_send_len = 0
        session.last_request_content_len = sent_len
        session.pending_send_seq = send_seq

        thread = threading.Thread(
            target=self._run_async_stream_send,
            args=(session, request_snapshot, send_seq),
            daemon=True
        )
        session.pending_thread = thread
        thread.start()

    def _wait_pending_stream_send(
            self,
            session: ModerateV2AsyncStreamSession,
            timeout: Optional[float]
    ) -> bool:
        pending_event = session.pending_event
        if timeout is None:
            return pending_event.wait()
        return pending_event.wait(timeout)

    def _wait_for_async_result(
            self,
            session: ModerateV2AsyncStreamSession,
            observed_result_version: int,
            timeout: Optional[float]
    ) -> bool:
        with session.lock:
            if session.result_version > observed_result_version:
                return True

            deadline = None if timeout is None else time.monotonic() + timeout
            while session.result_version <= observed_result_version:
                if session.pending_thread is None:
                    break
                if deadline is None:
                    session.result_cond.wait()
                    continue

                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    break
                session.result_cond.wait(remaining)

            return session.result_version > observed_result_version

    def _flush_async_stream_session(
            self,
            session: ModerateV2AsyncStreamSession,
            force_until_idle: bool,
            preempt_pending: bool = False
    ) -> Optional[ModerateV2Response]:
        while True:
            with session.lock:
                pending_exists = session.pending_thread is not None
                if not pending_exists:
                    if session.request is None:
                        return session.default_body

                    current_len = self._get_request_content_len(session.request)
                    unsent_len = max(0, current_len - session.last_request_content_len)
                    should_send = force_until_idle or session.has_last_chunk or (
                            unsent_len >= session.send_threshold)

                    if not should_send:
                        session.stream_send_len = unsent_len
                        session.need_flush_after_pending = False
                        return session.default_body

                    request_snapshot = self._build_stream_request_snapshot(session.request)
                    session.pending_event.clear()
                    session.pending_request = request_snapshot
                    session.pending_result = None
                    session.pending_error = None
                    session.need_flush_after_pending = False
                    session.stream_send_len = 0

                else:
                    if not preempt_pending:
                        request_snapshot = None
                    else:
                        self._invalidate_pending_async_send(session)
                        request_snapshot = self._build_stream_request_snapshot(session.request)
                        session.pending_result = None
                        session.pending_error = None
                        session.need_flush_after_pending = False
                        session.stream_send_len = 0

            if request_snapshot is not None:
                try:
                    moderate_response = self._send_stream_request_snapshot(request_snapshot)
                except Exception as e:
                    with session.lock:
                        session.pending_request = None
                        session.pending_error = e
                        session.pending_event.set()
                    raise

                with session.lock:
                    self._update_async_session_after_response(session, request_snapshot, moderate_response)
                    session.pending_request = None
                    session.pending_event.set()
                    if not session.need_flush_after_pending:
                        return moderate_response
                    continue

            if preempt_pending:
                with session.lock:
                    return session.default_body

            self._wait_pending_stream_send(session, None)
            with session.lock:
                if session.pending_error is not None and not session.need_flush_after_pending:
                    raise session.pending_error
                if not force_until_idle and not session.need_flush_after_pending:
                    return session.default_body

    def ModerateStreamAsync(
            self,
            request: ModerateV2Request,
            session: ModerateV2AsyncStreamSession,
            wait_timeout: float
    ) -> Optional[ModerateV2Response]:
        """
        异步流式审核：
        - 首次和尾次请求强制等待服务端返回；
        - 中间请求相对上次已审核内容的新增长度达到固定阈值后，等待 wait_timeout，超时则返回上次缓存结果；
        - 同一 session 同时只允许一个后台审核任务；
        - 后台任务运行期间新增内容继续累加，任务结束后会基于首块到当前最新内容的全量快照自动补发。
        """
        if request is None:
            request = ModerateV2Request()

        if request.use_stream == 0 or session is None:
            raise ValueError("use_stream cannot be 0, and session cannot be None")

        if wait_timeout is not None and wait_timeout < 0:
            raise ValueError("wait_timeout cannot be negative")

        observed_result_version = 0
        should_wait_for_result = False

        with session.lock:
            is_first_request = session.request is None
            is_last_request = (request.use_stream == 2)
            observed_result_version = session.result_version

            self._append_stream_request(request, session)
            session.has_last_chunk = session.has_last_chunk or is_last_request

            if is_first_request:
                request_snapshot = self._build_stream_request_snapshot(session.request)
            else:
                request_snapshot = None

            if is_first_request:
                session.pending_event.clear()
                session.pending_request = request_snapshot
                session.pending_result = None
                session.pending_error = None
                session.stream_send_len = 0
            elif session.pending_thread is not None:
                current_len = self._get_request_content_len(session.request)
                pending_len = self._get_request_content_len(session.pending_request)
                new_content_len = max(0, current_len - pending_len)
                session.need_flush_after_pending = session.has_last_chunk or (
                        new_content_len >= session.send_threshold)
                if not is_last_request:
                    should_wait_for_result = True
            else:
                current_len = self._get_request_content_len(session.request)
                unsent_len = max(0, current_len - session.last_request_content_len)
                session.stream_send_len = unsent_len
                need_send_request = is_last_request or (unsent_len >= session.send_threshold)
                if not need_send_request:
                    return session.default_body

                if not is_last_request:
                    request_snapshot = self._build_stream_request_snapshot(session.request)
                    self._start_async_stream_send(session, request_snapshot, current_len)
                    should_wait_for_result = True

        if is_first_request:
            try:
                moderate_response = self._send_stream_request_snapshot(request_snapshot)
            except Exception as e:
                with session.lock:
                    session.pending_request = None
                    session.pending_error = e
                    session.pending_event.set()
                    session.result_cond.notify_all()
                raise

            with session.lock:
                self._update_async_session_after_response(session, request_snapshot, moderate_response)
                session.pending_request = None
                session.pending_event.set()
                session.result_cond.notify_all()
            return moderate_response

        if is_last_request:
            return self._flush_async_stream_session(session, True, preempt_pending=True)

        if should_wait_for_result and self._wait_for_async_result(session, observed_result_version, wait_timeout):
            with session.lock:
                if session.pending_error is not None and session.default_body is None:
                    raise session.pending_error
                return session.default_body

        with session.lock:
            return session.default_body

    def ModerateStream(
            self, request: ModerateV2Request, session: ModerateV2StreamSession
    ) -> Optional[ModerateV2Response]:
        """
        处理流式审核请求
        :param request: 当前流式请求片段（ModerateV2Request 类型）
        :param session: 流式会话对象（ModerateV2StreamSession 类型）
        :return: 审核响应（ModerateV2Response 类型）
        """
        # 1. 校验参数合法性
        path = "/v2/moderate"
        action = "Moderate"
        if request is None:
            request = ModerateV2Request()  # 初始化空请求

        # 本接口仅支持流式调用（use_stream 不能为 0，且 session 不能为空）
        if request.use_stream == 0 or session is None:
            raise ValueError("use_stream cannot be 0, and session cannot be None")

        is_first_request = (session.request is None)  # 判断是否为首次请求
        is_last_request = (request.use_stream == 2)  # 判断是否为最后一次请求

        # 2. 初始化或追加会话请求（深拷贝确保隔离）
        if session.request is None:
            session.request = ModerateV2Request(request)
        else:
            # 后续请求：追加当前请求内容到 session 积累的请求中
            # 示例：追加 message.content（根据实际业务调整）
            if request.message and request.message.content:
                if session.request.message is None:
                    session.request.message = MessageV2()
                session.request.message.content += request.message.content
                session.request.use_stream = request.use_stream
        session.stream_send_len += len(request.message.content)

        # 3. 判断是否需要发送请求到后端
        need_send_request = (
            is_last_request
            or is_first_request
            or session.stream_send_len >= session.CurrentSendWindow
        )

        # 如果不需要发送请求，直接返回上次的默认响应（如果有）
        if not need_send_request:
            return session.default_body

        session.CurrentSendWindow = session.CurrentSendWindow * LLM_STREAM_SEND_EXPONENT_V2

        # 3. 序列化请求（使用 Pydantic 的 model_dump 方法）
        try:
            request_body = session.request.model_dump_json(by_alias=True, exclude_none=True).encode("utf-8")
            # request_str = session.request.model_dump_json(by_alias=True)
        except Exception as e:
            raise IOError(f"Failed to serialize request: {str(e)}")
        headers = {
            # "Content-Type": "application/json",
        }
        sign_header = request_sign(
            headers, self.ak, self.sk, self.region, self.url, path, action, request_body, self.rewrite_url
        )
        try:
            enc_req_key = None
            if self.aicc_client is not None:
                request_body, enc_req_key = self.EncryptWithResponse(request_body)

            response = self.http_client.post(
                url=self.url + path + "?Action=" + action + "&Version=" + Version,
                data=request_body,
                headers=sign_header
            )
        except requests.exceptions.RequestException as e:
            raise IOError(f"HTTP request failed: {str(e)}")

        # 5. 解析响应
        try:
            if enc_req_key is not None:
                response_body = self.DecryptResponse(enc_req_key, response.content)
            else:
                response_body = response.content

            try:
                moderate_response = ModerateV2Response.model_validate_json(response_body)
            except Exception:
                response_data = json.loads(response_body)
                moderate_response = ModerateV2Response(**response_data)
        except Exception as e:
            raise IOError(f"Failed to parse response: {str(e)}")

        # 6. 更新会话状态
        session.default_body = moderate_response  # 存储响应体
        session.stream_send_len = 0  # 重置未发送长度（根据实际业务调整）
        session.request.msg_id = moderate_response.result.msg_id

        # 7. 若为最后一次流式请求（use_stream == 2），打印最终内容
        if session.request.use_stream == 2:
            final_content = session.request.message.content if (
                    session.request.message and session.request.message.content) else ""
            print(f"最终检测内容: {final_content}")

        return moderate_response
    

    def GenerateV2Stream(self, request):
        path = "/v2/generate"
        action = "Generate"
        if request is None:
            request = GenerateStreamV2Request()

        # 将请求结构体序列化为 JSON
        requestBody = request.model_dump_json(by_alias=True, exclude_none=True).encode("utf-8")

        headers = {
            # "Content-Type": "application/json",
        }
        try:
            sign_header = request_sign(
                headers, self.ak, self.sk, self.region, self.url, path, action, requestBody, self.rewrite_url
            )
            # 发送 HTTP 请求
            resp = self.http_client.post(url=self.url + path + "?Action=" + action + "&Version=" + Version,
                                         data=requestBody, headers=sign_header, stream=True)
            if resp.status_code != 200:
                raise Exception("bad response code: %d" % resp.status_code)

            for line in resp.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.lstrip().startswith('data:'):
                        sse_data = line[line.index(':') + 1:].strip()
                        yield sse_data
        except Exception as e:
            return None, Exception("failed to send request: %s" % str(e))


# 自定义 JSON 编码器
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # 处理datetime类型（如2023-10-01T12:00:00）
        if isinstance(obj, datetime):
            return obj.isoformat()
        # 处理date类型（如2023-10-01）
        elif isinstance(obj, date):
            return obj.isoformat()
        # 处理UUID类型
        elif isinstance(obj, UUID):
            return str(obj)
        # 处理其他未知的自定义类型（返回类型信息便于调试）
        elif hasattr(obj, '__dict__'):
            return obj.__dict__  # 返回对象的属性字典
        # 调用默认处理（会抛出TypeError）
        return super().default(obj)


RiskMatchV2.model_rebuild()
