## Data Source

The chatbot retrieves information from the SOP document:

SOP_MASTER.docx

This document contains troubleshooting steps for VMware Horizon VDI issues.


# SOP RAG Chatbot

## Overview

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that answers troubleshooting questions using predefined Standard Operating Procedure (SOP) documents.

The chatbot retrieves relevant SOP sections using semantic search and generates responses using a local language model.

## Features

* Load SOP documents from `.docx`
* Chunk documents for efficient retrieval
* Generate embeddings using Ollama
* Store embeddings in a FAISS vector database
* Retrieve relevant SOP steps using semantic search
* Generate answers using a local LLM

## Tech Stack

* Python
* LangChain
* FAISS
* Ollama
* TinyLlama / Phi3

## How It Works

1. Load SOP document
2. Split document into chunks
3. Convert chunks into embeddings
4. Store embeddings in FAISS vector database
5. Retrieve relevant chunks based on user question
6. Send context to LLM to generate answer

## Run the Chatbot

Install dependencies:

```
pip install langchain langchain-community langchain-ollama faiss-cpu docx2txt
```

Run the chatbot:

```
python projchunk.py
```

Then ask questions like:

```
pairing key issue
agent unreachable symptoms
reset pairing key command
```

## Example Use Case

This chatbot helps IT support teams quickly retrieve troubleshooting procedures from internal SOP documentation.

