import chromadb
client = chromadb.Client()

collection = client.get_collection("sample_collection")

if collection is None:
    print("Collection does not exist")
else:
    print("Using existing collection")

results = collection.query()

for result in results:
    print(result)