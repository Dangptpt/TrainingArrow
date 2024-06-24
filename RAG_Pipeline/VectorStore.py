from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import google.generativeai as genai
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

# embeddings = HuggingFaceEmbeddings(model_name = 'VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')

loader = PyPDFLoader('RAG_Pipeline/Data/quyche.pdf')
document = loader.load()
splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        )
chunks = splitter.split_documents(document)
# vector_store = FAISS.from_documents(chunks, embedding=embeddings)
# vector_store.save_local("RAG_Pipeline/vectordb")

retriever = BM25Retriever.from_documents(documents=chunks, k=100)
result = retriever.invoke("quy định về đình chỉ học tập")

# Create the retriever
compressor = CohereRerank(cohere_api_key='KntpaI7xnyYkVU2HtLD9CgTOdBPAVWgF4uBZwB4d', top_n=5)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

compressed_docs = compression_retriever.invoke("quy định về đình chỉ học tập")
print (compressed_docs)