import chromadb
from datetime import datetime, timedelta

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")
chroma_collection = client.get_or_create_collection("simple_collection")

chroma_db_def= """
Chromadb: An AI-Native Vector Database
Chromadb is an open-source vector database specifically designed for storing and managing embeddings, which are numerical representations of data points that capture their meaning and relationships. This makes it a valuable tool for various applications in artificial intelligence, including:
Semantic Search: Finding similar documents based on their meaning rather than keywords.
Machine Learning: Training models with efficient data representation and retrieval.
Natural Language Processing: Understanding and generating human language with improved accuracy.
"""

about_jpmc= """
JPMorgan Chase & Co. (JPMC)
JPMorgan Chase & Co. is an American multinational financial services firm headquartered in New York City and incorporated in Delaware. It is one of the largest and oldest financial institutions in the world, offering a wide range of services including:

Investment banking: Advising companies on mergers and acquisitions, raising capital, and underwriting debt and equity offerings.
Financial services for consumers and small businesses: Checking and savings accounts, mortgages, credit cards, and small business loans.
Commercial banking: Providing loans and other financial services to large corporations.
Financial transactions processing: Processing payments and other financial transactions.
Asset management: Investing on behalf of individuals and institutions.
"""

today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")

chroma_collection.add(
    documents=["This is a test document", "This is another test document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

chroma_collection.add(
    documents=[chroma_db_def],
    metadatas=[{"source": "trychroma", "date" : formatted_date }],
    ids=["id3"]
)

chroma_collection.add(
    documents=[about_jpmc],
    metadatas=[{"source": "about_jpmc", "date" : formatted_date }],
    ids=["id4"]
)

count =chroma_collection.count()
print("\n After insertion : Total Records in Collection : \n", count, "\n")