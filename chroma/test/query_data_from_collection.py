import chromadb,json
from datetime import datetime, timedelta

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")

chroma_collection = client.get_or_create_collection("simple_collection")


#documents = chroma_collection.query(query_texts=["*"])
#for document in documents:
#    print("all documents ",document)
#today = datetime.today()
#two_days_ago = today - timedelta(days=0)
#print(two_days_ago)
#formatted_date = two_days_ago.strftime("%d-%m-%Y")
#filter_by_date = {"field": "timestamp", "operator": "$eq", "value": formatted_date}

result = chroma_collection.peek() 
# returns a list of the first 10 items in the collection
print("\n Top 10 frequently used records in chroma db \n",result)
result = chroma_collection.query(
    query_texts=["Decribe JPMC"],
    n_results=2,
    #where = {"timestamp" : formatted_date}
)

total_data=chroma_collection.get()
print("\n\n Total data from the db \n\n", total_data)

# json.dumps(result, indent=1) // print formatted json 

print("\n\n Decribe JPMC \n\n",result)

result = chroma_collection.query(
    query_texts=["What is AI"],
    n_results=2,
    #where = {"timestamp" : formatted_date}
)

# json.dumps(result, indent=1) // print formatted json 

print("\n\n What is AI \n\n",result)


result = chroma_collection.query(
    query_texts=["Hyderabad"],
    n_results=2,
    #where = {"timestamp" : formatted_date}
)

# json.dumps(result, indent=1) // print formatted json 

print("\n\n Hyderabad \n\n",result)

result = chroma_collection.query(
    query_texts=["llamaIndex"],
    n_results=2,
    #where = {"timestamp" : formatted_date}
)

# json.dumps(result, indent=1) // print formatted json 

print("\n\n What is llamaIndex \n\n",result)

result = chroma_collection.query(
    query_texts=["Where do arun stay ?"],
    n_results=2,
    #where = {"timestamp" : formatted_date}
)

# json.dumps(result, indent=1) // print formatted json 

print("\n\n Where do arun stay \n\n",result)