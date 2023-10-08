import streamlit as st

st.title("Chat Bot")
if st.button("Clear History"):
    st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter your message"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Bot: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)   
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


# Sidebar

with st.sidebar:
    st.sidebar.title("Sidebar Title")
    pdf_data = st.file_uploader("Upload your Document here", accept_multiple_files=True)

