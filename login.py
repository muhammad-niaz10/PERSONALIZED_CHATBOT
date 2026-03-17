import streamlit as st
from api import login

def login_page():

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        res = login(email, password)

        if res.status_code == 200:

            token = res.json()["access_token"]

            st.session_state.token = token

            st.success("Login Successful")

        else:
            st.error("Invalid Credentials")