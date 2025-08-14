from volcenginesdkarkruntime import Ark

client = Ark()

print("----- multimodal embeddings request -----")
resp = client.multimodal_embeddings.create(
    model="doubao-embedding-vision-250615",
    input=[
        {
            "type": "text",
            "text": "What is the weather like today?"
        },
        {
            "type": "image_url",
            "image_url": {
                "url": "https://ark-project.tos-cn-beijing.volces.com/images/view.jpeg"
            }
        }
    ]
)
print(resp.data)
