from volcenginesdkarkruntime import Ark

# gets API Key from environment variable ARK_API_KEY
client = Ark()

if __name__ == "__main__":

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
    )
    print(completion.choices[0].message.content)

    # Streaming:
    print("----- streaming request -----")
    stream = client.chat.completions.create(
        model="${YOUR_ENDPOINT_ID}",
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
        stream=True,
    )
    for chunk in stream:
        if not chunk.choices:
            continue

        print(chunk.choices[0].delta.content, end="")
    print()
