import chromadb
from datetime import datetime, timedelta

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")

chroma_collection = client.get_or_create_collection("simple_collection")

today = datetime.today()
#two_days_ago = today - timedelta(days=0)
#print(two_days_ago)
formatted_date = today.strftime("%d-%m-%Y")
print(formatted_date)
chroma_collection.delete(
    ids=[],
    where={"date" : formatted_date}
)
chroma_collection.delete(
    ids=["id2"]
)

chroma_collection.delete(
    ids=["id1"]
)
#Work on date format to delete older then 7 days 
#Any UI present for Vector DB -- 
#to delete all you can use delete_Collection option 
#chroma_collection.query(
#    query_texts=[" Describe about AI"],
#    n_results=2
#)