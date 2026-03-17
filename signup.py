import streamlit as st
from api import signup

def signup_page():

    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        res = signup(name, email, password)

        if res.status_code == 200:
            st.success("User Created Successfully")

        else:
            st.error(res.text)