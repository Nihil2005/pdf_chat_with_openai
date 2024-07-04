import streamlit as st
import fitz  
from langchain_openai import OpenAI

# Initialize the LangChain OpenAI LLM
llm = OpenAI(api_key='')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Streamlit application
st.title("Chat with your PDF using LangChain")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Text:")
    st.write(text)
    
    st.write("### Chat with the PDF")
    user_input = st.text_input("Ask a question about the PDF:")
    
    if user_input:
        # Create the prompt
        prompt = f"Context: {text}\n\nQuestion: {user_input}\n\nProvide a clear and direct answer based on the context."
        
        # Use LangChain to generate the response
        response = llm(prompt)
        
        # Display the response
        st.write(f"Response: {response}")
