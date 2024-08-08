from volcenginesdkarkruntime import Ark

client = Ark()

print("----- tokenization request -----")
resp = client.tokenization.create(
    model="${YOUR_ENDPOINT_ID}",
    text=["花椰菜又称菜花、花菜，是一种常见的蔬菜。"]
)
print(resp)
