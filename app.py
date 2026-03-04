from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("Sample_SOP.docx")

documents = loader.load()

print(type(documents))
