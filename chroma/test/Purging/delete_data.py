import chromadb,json
from datetime import datetime, timedelta

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")

chroma_collection = client.get_or_create_collection("simple_collection")


#documents = chroma_collection.query(query_texts=["*"])
#for document in documents:
#    print("all documents ",document)
today = datetime.today()
two_days_ago = today - timedelta(days=1)
formatted_date = two_days_ago.strftime("%d-%m-%Y")
#03-01-2024
print("formatted_date ",formatted_date)
filter_by_date = {"field": "timestamp", "operator": "$lt", "value": formatted_date}

#today = datetime.today()
#formatted_date = today.strftime("%d-%m-%Y")
result = chroma_collection.delete(
    where = {
    "date": {
        "$eq": formatted_date
        }
    }
)

print("\n\n With data comparison \n\n", result)
