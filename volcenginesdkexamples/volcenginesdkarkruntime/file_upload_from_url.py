import os
import asyncio

from volcenginesdkarkruntime import AsyncArk

client = AsyncArk(api_key=os.environ.get("ARK_API_KEY"))


async def main():
    print("Upload video file from URL to user-owned TOS bucket")
    file = await client.files.create(
        url="https://ark-project.tos-cn-beijing.volces.com/videos/aigen.mp4",
        purpose="user_data",
        tos={
            # Replace with your own TOS bucket and prefix
            "bucket": os.environ.get("TOS_BUCKET"),
            "prefix": os.environ.get("TOS_PREFIX"),
        },
    )
    print(f"File uploaded: {file.id}")
    print(f"File status: {file.status}")
    print(f"File filename: {file.filename}")
    print(f"File mime_type: {file.mime_type}")
    print(f"File bytes: {file.bytes}")
    print(f"File tos: {file.tos}")

    file = await client.files.wait_for_processing(file.id)
    print(f"\nFile processed: {file.id}")
    print(f"File status: {file.status}")
    if file.tos:
        print(f"File tos.bucket: {file.tos.bucket}")
        print(f"File tos.object_key: {file.tos.object_key}")


if __name__ == "__main__":
    # Usage:
    #   export ARK_API_KEY=<your-api-key>
    #   export TOS_BUCKET=<your-tos-bucket>
    #   export TOS_PREFIX=<your-upload-prefix/>
    #   python file_upload_from_url.py
    asyncio.run(main())
