import requests
import json
import weaviate
import weaviate.classes as wvc

client = weaviate.connect_to_local(
    port=8080,
    grpc_port=50051,
    headers={
        "X-OpenAI-Api-Key": "#####" # Replace with your inference API key
    }
)

questions = client.collections.get("Question")
response = questions.query.near_text(
    query="biology",
    limit=2
)

print(response.objects[0].properties)