import streamlit as st
from pdf_reader import read_pdfs_from_folder
from embeddings import create_embeddings, search_similar
from llm_integration import chat_with_llm
import os

st.set_page_config(page_title="法律訴訟聊天機器人", page_icon="⚖️")

st.title("法律訴訟聊天機器人")
st.markdown("將PDF文件放入pdfs/資料夾以嵌入領域知識，然後與LLM聊天關於訴訟。")

pdf_folder = "pdfs"
if os.path.exists(pdf_folder) and os.listdir(pdf_folder):
    text = read_pdfs_from_folder(pdf_folder)
    st.write("PDF內容已讀取。")
    embeddings = create_embeddings(text)
    st.session_state['embeddings'] = embeddings
    st.session_state['text'] = text
else:
    st.write("請將PDF文件放入pdfs/資料夾。")

user_input = st.text_input("輸入您的問題：")

if st.button("發送"):
    if 'embeddings' in st.session_state:
        relevant_docs = search_similar(user_input, st.session_state['embeddings'], st.session_state['text'])
        response = chat_with_llm(user_input, relevant_docs)
        st.write("回應：", response)
    else:
        st.write("請先將PDF文件放入pdfs/資料夾。")
