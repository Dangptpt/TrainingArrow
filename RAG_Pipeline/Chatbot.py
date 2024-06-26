from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
import gradio as gr

import os
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=api_key,
                             temperature=0.2,convert_system_message_to_human=True)

embeddings = HuggingFaceEmbeddings(model_name='VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')

vector_store = FAISS.load_local("RAG_Pipeline/vectordb", embeddings, allow_dangerous_deserialization=True)

prompt_template = """
Bạn là trợ lý cho các nhiệm vụ trả lời câu hỏi, hãy trả lời bằng tiếng Việt, lịch sự và thân thiện.
Hãy trả lời không biết nếu như bạn không thấy thông tin trong đoạn ngữ cảnh, đừng cố gắng trả lời
Đoạn ngữ cảnh: {context}
Câu hỏi: {question}
Câu trả lời:
"""

question = "quy định về đình chỉ học tập"

print(vector_store)

QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt_template)
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 5}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

def gennerate(question):
    response = qa_chain({"query": question}, return_only_outputs=True)
    return response['result']

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height=600)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = gennerate(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()

