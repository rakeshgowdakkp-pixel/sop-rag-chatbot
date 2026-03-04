from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("SOP_MASTER.docx")

documents = loader.load()

print(type(documents))