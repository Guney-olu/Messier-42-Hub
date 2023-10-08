import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import langchain
langchain.verbose = False
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplate import bot_template,css,user_template
from langchain.llms import HuggingFaceHub

def pdf_crawl(data):
    raw_text = ""
    for det in data:
        det_reader = PdfReader(det)
        for page in det_reader.pages:
            raw_text+=page.extract_text()
    return raw_text

def get_data_chunk(raw_data):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=100,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_data)
    return chunks
def get_vectorstore(data_chunk):
    embedding = OpenAIEmbeddings()
    #embedding = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorStore =FAISS.from_texts(texts=data_chunk,embedding=embedding)
    return vectorStore

def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    #llm = HuggingFaceHub(repo_id="",model_kwargs={"temperature":0.5,"max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history',return_message=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm,retriever=vector_store.as_retriever(),memory=memory)
    return conversation_chain

def handle_inputquestion(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}",message.content),unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content),unsafe_allow_html=True)

def init():
    load_dotenv()
    st.set_page_config(page_title="pdf_extractor", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("Chat with pdf")
    user_question = st.text_input("Ask for information related to the pdf")

    if user_question:
        handle_inputquestion(user_question)

    with st.sidebar:
        st.subheader("Your document")
        pdf_data = st.file_uploader("Upload your pdf here", accept_multiple_files=True)

        if st.button("process"):
            with st.spinner("Processing..."):
                raw_data = pdf_crawl(pdf_data)
                data_chunk = get_data_chunk(raw_data)
                vector_store = get_vectorstore(data_chunk)
                if st.session_state.conversation_chain is None:
                    st.session_state.conversation_chain = get_conversation_chain(vector_store)

                st.session_state.conversation_chain()


if __name__ == '__main__':
    init()

