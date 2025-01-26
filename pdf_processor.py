from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def process_pdf(pdf_path):
    """
    Process a PDF file and return a list of Document objects.
    """

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, add_start_index=True
    )
    all_docs = text_splitter.split_documents(docs)

    return all_docs
