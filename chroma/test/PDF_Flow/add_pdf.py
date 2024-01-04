import chromadb
import PyPDF2

from datetime import datetime

#The PersistentClient provides an interface for interacting with Chromadb collections in a persistent manner.
client = chromadb.PersistentClient(path="../chroma_db_test")
chroma_collection = client.get_or_create_collection("simple_collection")

pdf_file=open("introduction_to_java.pdf", "rb")

pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""
# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()


chroma_collection.add(
    documents=[text],
    metadatas=[{"source": "https://introcs.cs.princeton.edu/","bookName":"introduction_to_java"}],
    ids=["id5"]
)

results = chroma_collection.query(
    query_texts=["What is JAVA ?", "Who created JAVA ?"],
    n_results=2
)

print("\n\n Q:What is JAVA ? & Who created JAVA ? \n\n", results)