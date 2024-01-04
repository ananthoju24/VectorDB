import weaviate
import weaviate.classes as wvc

# As of November 2023, we are working towards making all WCS instances compatible with the new API introduced in the v4 Python client.
# Accordingly, we show you how to connect to a local instance of Weaviate.
# Here, authentication is switched off, which is why you do not need to provide the Weaviate API key.
client = weaviate.connect_to_local(
    port=8080,
    grpc_port=50051,
    headers={
        "X-OpenAI-Api-Key": "####" # Replace with your inference API key
    }
)

questions = client.collections.create(
    name="Question_NEW",
    vectorizer_config=wvc.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    generative_config=wvc.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
)
