import asyncio

from volcenginesdkarkruntime import AsyncArk
from volcenginesdkarkruntime.types.responses.response_completed_event import ResponseCompletedEvent

client = AsyncArk()


async def main():
    # upload video file
    print("Upload video file")
    file = await client.files.create(
        # replace with your local video path
        file=open("ark_vlm_video_input.mp4", "rb"),
        purpose="user_data",
        preprocess_configs={
            "video": {
                "fps": 0.3,  # define the sampling fps of the video, default is 1.0
            }
        }
    )
    print(f"File uploaded: {file.id}")

    # 等待文件处理完成
    await client.files.wait_for_processing(file.id)
    print(f"File processed: {file.id}")

    # ==========================================================
    # 示例 1：多轮对话，开启 caching
    # ==========================================================
    print("Example 1: Use caching for multi-round chat")
    # ---------- 第 1 轮 ----------
    # 说明：开启 caching，store=True 表示把对话存储在服务端，以便后续引用
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        input=[
            {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
            {"role": "user", "content": [
                {
                    "type": "input_video",
                    "file_id": file.id  # ref video file id
                },
                {
                    "type": "input_text",
                    "text": "请逐帧分析视频内容"
                }
            ]},
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True
    )
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id

    # ---------- 第 2 轮 ----------
    # 说明：通过 previous_response_id 关联上一轮的上下文
    stream = await client.responses.create(
        model="doubao-seed-1-6",
        previous_response_id=response_id,
        input=[
            {"role": "user", "content": "上一轮对话里视频里的内容是"},
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True
    )
    async for event in stream:
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
