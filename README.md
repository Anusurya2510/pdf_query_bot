# PDF Query Bot

## Overview
PDF Query Bot is a Python-based document analysis tool that leverages advanced natural language processing techniques to extract and answer questions from PDF documents using machine learning.

## Key Features
- PDF Document Loading
- Semantic Text Chunking
- Vector-based Document Embedding
- Retrieval-based Question Answering
- Hugging Face Language Model Integration

## Technical Components
### Libraries Used
- LangChain: Document processing and QA framework
- HuggingFace: Transformer-based language models
- ChromaDB: Vector storage and retrieval
- Sentence Transformers: Document embedding generation

## Workflow
1. **Document Loading**: Reads PDF using PyPDFLoader
2. **Text Segmentation**: Splits document into manageable chunks
3. **Embedding Generation**: Converts text chunks to vector representations
4. **Vector Storage**: Stores embeddings in ChromaDB
5. **Retrieval Mechanism**: Finds most relevant document sections
6. **Question Answering**: Generates answers using language model

## Installation
```bash
pip install pypdf
pip install chromadb
pip install langchain_community
```
