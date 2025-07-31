import fitz  # PyMuPDF
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os

# Step 1: Load the PDF
pdf_path = os.path.expanduser("~/Downloads/nwt.pdf")
doc = fitz.open(pdf_path)

# Step 2: Extract text from each page
text = ""
for page in doc:
    text += page.get_text()

# Step 3: Convert the text into LangChain document format
documents = [Document(page_content=text)]

# Step 4: Split the document into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_documents(documents)

# Step 5: Embed and store in Chroma vector DB
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(docs, embedding, persist_directory="bible_db")

print("✅ Bible text processed and stored successfully.")
