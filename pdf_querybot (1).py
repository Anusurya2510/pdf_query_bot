import os

from langchain import HuggingFaceHub
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


# Input your Hugging Face API key below
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'huggingface_api_token'


# Get the BLOOM Model from Hugging Face
llm = HuggingFaceHub(repo_id="bigscience/bloom",
                                        model_kwargs={"temperature":0.1,
                                                      "max_length":100})

# load document
loader = PyPDFLoader("your pdf path")
documents = loader.load()


# split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)


# select which embeddings we want to use
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2")


# create the vectorestore to use as the index
db = Chroma.from_documents(texts, embeddings)

# expose this index in a retriever interface
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":3})


qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

query = "what is the document about?"

result = qa({"query": query})
print(result['result'])



