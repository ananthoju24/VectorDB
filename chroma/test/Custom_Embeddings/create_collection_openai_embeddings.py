import chromadb
from openai import OpenAI

# Replace with your OpenAI API key
api_key="#####"
# Define the OpenAI embedding model (e.g., davinci, curie, etc.)
embedding_model = "text-embedding-ada-002"

# Initialize OpenAI client
openai_client = OpenAI(api_key=api_key)

# Create or connect to Chromadb client
chroma_client = chromadb.Client()


def add_documents_with_openai(documents):
    for document in documents:
        # Generate embedding using OpenAI
        openai_client.embeddings
        embedding = openai_client.embeddings.create(input =[document], model=embedding_model)
        # Add document and embedding to Chromadb
        print(embedding)
        chroma_client.upsert(id=document["id"], embedding=embedding["embeddings"][0], metadata=document["metadata"])

documents = [
    {"id": "document1", "content": "This is the content of document 1.", "metadata": {"author": "John Doe"}},
    {"id": "document2", "content": "This is the content of document 2.", "metadata": {"publication_date": "2023-10-26"}},
]

add_documents_with_openai(documents)

result=chroma_client.query(
    query_texts=["Document 1"],
    n_results=2
)

print("\n Result \n", result)