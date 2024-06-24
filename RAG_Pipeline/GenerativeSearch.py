from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import google.generativeai as genai
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank
import os
import gradio as gr
from IPython.display import Markdown
import textwrap

cohere_api_key = os.environ['COHERE_API_KEY']
google_api_key = os.environ['GOOGLE_API_KEY']
loader = PyPDFLoader('RAG_Pipeline/Data/quyche.pdf')
document = loader.load()

splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        )
chunks = splitter.split_documents(document)

retriever = BM25Retriever.from_documents(documents=chunks, k=100)
# result = retriever.invoke("quy định về đình chỉ học tập")

# Create the retriever
compressor = CohereRerank(cohere_api_key=cohere_api_key, top_n=3)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

#compressed_docs = compression_retriever.invoke("quy định về đình chỉ học tập")

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel(model_name='gemini-pro')

def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def gennerate(question, chat_history):
    compressed_docs = compression_retriever.invoke(question)
    context = format_docs(compressed_docs)
    
    prompt = f"""
    Bạn là trợ lý cho các nhiệm vụ trả lời câu hỏi, hãy trả lời bằng tiếng Việt, lịch sự và thân thiện.
    Hãy trả lời câu hỏi dựa trên dữ liệu có trong đoạn ngữ cảnh và lịch sử đoạn chat.
    Hãy trả lời không biết nếu như bạn không thấy thông tin trong đoạn ngữ cảnh, đừng cố gắng trả lời
    Lịch sử đoạn chat: {chat_history}
    Đoạn ngữ cảnh: {context}
    Câu hỏi: {question}
    Câu trả lời:
    """
    print (prompt)
    return model.generate_content(prompt).text

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height=600)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = gennerate(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()


