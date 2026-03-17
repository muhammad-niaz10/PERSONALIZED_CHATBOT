import streamlit as st
from api import add_website

def add_website_page():

    st.subheader("Add Website")

    url = st.text_input("Website URL")

    if st.button("Add Website"):

        token = st.session_state.get("token")

        if not token:
            st.error("Please login first")
            return

        res = add_website(url, token)

        if res.status_code == 200:
            st.success("Website Added and Scraped")

        else:
            st.error(res.text)