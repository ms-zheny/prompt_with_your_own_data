import utils
import urllib

import streamlit as st

try:

    st.set_page_config(
    page_title="Demo QnA Bot",
    )

    st.title("Demo QnA Bot")
    st.subheader("Power Platform Licence Guide")
    st.write("Author: [Zhen Yuan](https://www.linkedin.com/in/walleyuan/)")
    st.divider()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    utils.get_text()

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))








