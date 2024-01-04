import PyPDF2
import weaviate
import weaviate.classes as wvc

client = weaviate.connect_to_local(
    port=8080,
    grpc_port=50051,
    headers={
        "X-OpenAI-Api-Key": "#####" # Replace with your inference API key
    }
)

print("is weaviate ready : ",client.is_ready())

#resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
#data = json.loads(resp.text)  # Load data

pdf_file=open("introduction_to_java.pdf", "rb")

pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""
# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

questions = client.collections.get("Question")
#questions.data.insert({"IntoductionToJava" : text})\
questions.add_documents_with_openai()

response = questions.query.near_text(
    query="java",
    limit=2
)

print(response.objects[0].properties)