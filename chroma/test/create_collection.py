import chromadb

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="./chroma_db_test")
client.delete_collection("simple_collection")
chroma_collection = client.get_or_create_collection("simple_collection")
#heartbeat = client.heartbeat() # returns a nanosecond heartbeat. Useful for making sure the client remains connected.
#print("Heartbeat ", heartbeat)

count =chroma_collection.count()
print("\n Total Records in Collection : \n", count, "\n")

#collection.modify(name="new_collection_name") # Modify the collection name
#my_collection = client.get_collection(name="my_information_2")
