from pdf_processor import process_pdf
from embeddings import index_docs

MODEL = "bge-large:latest"

file_path = "./Nike-10K.pdf"
docs = process_pdf(file_path)

index = index_docs(MODEL, docs)
results = index.similarity_search(
    "How many distribution centers does Nike have in the US?"
)

print(results[0])
