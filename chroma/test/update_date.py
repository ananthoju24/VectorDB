import chromadb
from datetime import datetime

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")
chroma_collection = client.get_or_create_collection("simple_collection")


llama_index = """
LlamaIndex is a data framework designed to augment large language models (LLMs) with custom data. It facilitates the creation of robust applications powered by LLMs, tailored to specific data and requirements.

Here are some key features and benefits of LlamaIndex:

Features:

Data ingestion: LlamaIndex allows users to seamlessly import data from various sources, including APIs, SQL databases, and documents like PDFs.
Data indexing: It efficiently indexes the imported data, enabling fast and efficient retrieval based on user queries.
Query interface: It provides a user-friendly interface for submitting queries and retrieving knowledge-augmented responses.
Retrieval-augmented generation (RAG): It leverages RAG techniques to combine the strengths of LLMs with the knowledge embedded in the custom data.
Customization: Users can customize the data indexing and retrieval process to meet their specific needs.
Open-source: LlamaIndex is an open-source framework, allowing for community contributions and flexible integration into various projects.
"""
today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")

chroma_collection.update(
    ids=["id1"],
    documents= [llama_index],
    metadatas=[{"source":"google","date":formatted_date}]
)

print("Total count post update : ", chroma_collection.count())

result = chroma_collection.query(
    query_texts=["llamaIndex"],
    n_results=2
)
print("Query about llamaIndex ", result)