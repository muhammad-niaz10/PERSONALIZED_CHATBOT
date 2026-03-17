import streamlit as st
from login import login_page
from signup import signup_page
from add_website import add_website_page
from chat import chat_page

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🤖 AI Website Chatbot")

menu = ["Login", "Signup", "Add Website", "Chat"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    login_page()
elif choice == "Signup":
    signup_page()
elif choice == "Add Website":
    add_website_page()
elif choice == "Chat":
    chat_page()