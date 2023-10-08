import streamlit as st
# Add a title
st.title("My First Streamlit App")

# Add text
st.write("Welcome to my Streamlit app!")

# Add a button
if st.button("Say Hello"):
    st.write("Hello, Streamlit!")

# Add a slider
age = st.slider("Select your age", 0, 100, 25)

# Display user input
st.write(f"You selected age: {age}")
