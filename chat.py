import streamlit as st
from api import chat

def chat_page():

    st.subheader("Chat with your Website")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    token = st.session_state.get("token")

    if not token:
        st.error("Please login first")
        return

    user_input = st.chat_input("Ask something...")

    if user_input:

        with st.chat_message("user"):
            st.write(user_input)

        res = chat(user_input, token)

        if res.status_code == 200:

            data = res.json()

            reply = data["reply"]
            mode = data["mode"]

            with st.chat_message("assistant"):

                if mode == "website":
                    st.caption("Answer from Website Data")

                else:
                    st.caption("General AI Answer")

                st.write(reply)

        else:
            st.error("Chat error")