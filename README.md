# Semantic Search

We will be training a RAG model on a Nike 10-K filing dataset and then use it to perform semantic search on the dataset.

## First, let's install the necessary libraries

```bash
pip install -r requirements.txt
```

## Load Data

```bash
wget https://s1.q4cdn.com/806093406/files/doc_downloads/2021/08/Nike10k2021.pdf
```

## Install ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
```

Install an embedding model using the following command:

```bash
ollama pull bge-large
```

In `test.py`, put `MODEL = "bge-large"` and in the result put `result = query`, (update the file_path to the pdf file you want, Just use a file with text, as I have not put OCR in the code)

Save the file and run the following command:

```bash
python test.py
```
