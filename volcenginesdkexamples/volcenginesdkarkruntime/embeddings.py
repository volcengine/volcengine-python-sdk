from volcenginesdkarkruntime import Ark

client = Ark()

print("----- embeddings request -----")
resp = client.embeddings.create(
    model="${YOUR_ENDPOINT_ID}",
    input=["花椰菜又称菜花、花菜，是一种常见的蔬菜。"]
)
print(resp)