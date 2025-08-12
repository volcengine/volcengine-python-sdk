from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.multimodal_embedding import MultimodalEmbeddingResponse

client = Ark()

print("----- multimodal embeddings request -----")
resp: MultimodalEmbeddingResponse = client.multimodal_embeddings.create(
    model="doubao-embedding-vision-250615",
    input=[
        {
            "type": "text",
            "text": "花椰菜又称菜花、花菜，是一种常见的蔬菜。"
        }
    ],
    sparse_embedding={"type": "enabled"},  # enable sparse embedding
)
# dense embeddings
print("---- dense embeddings ----")
print(resp.data.embedding)

# sparse embeddings
print("---- sparse embeddings ----")
for item in resp.data.sparse_embedding:
    print(item)

