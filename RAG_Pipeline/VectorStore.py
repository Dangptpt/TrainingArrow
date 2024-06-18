from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import google.generativeai as genai

embeddings = HuggingFaceEmbeddings(model_name = 'VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')

loader = PyPDFLoader('RAG_Pipeline/Data/Rule.pdf')
document = loader.load()
splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        )
chunks = splitter.split_documents(document)
vector_store = FAISS.from_documents(chunks, embedding=embeddings)
vector_store.save_local("RAG_Pipeline/vectordb")
