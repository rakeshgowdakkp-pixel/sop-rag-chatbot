from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

# Load document
loader = Docx2txtLoader("Sample_SOP.docx")
documents = loader.load()

# Chunk document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Create vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# Load LLM
llm = OllamaLLM(model="tinyllama")

print("\nVMware Horizon SOP Chatbot Ready\n")

while True:

    query = input("\nAsk your question (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = vectorstore.similarity_search(query, k=1)

    context = "\n\n".join([doc.page_content for doc in results])

    # Debug: show retrieved chunks
    for doc in results:
        print("\nSOURCE:", doc.metadata)
        print(doc.page_content)

    prompt = f"""
You are a VMware Horizon support assistant.

Answer ONLY using the provided context, Dont PUT anything extra.
Do NOT invent information.
If the answer is not clearly in the context, say:

"I cannot find the answer in the SOP."

Context:
{context}

Question:
{query}

Provide a clear and concise answer.
"""

    response = llm.invoke(prompt)

    print("\nAI Answer:\n")
    print(response)
