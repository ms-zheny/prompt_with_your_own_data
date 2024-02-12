import streamlit as st
import json
import utils
import urllib.request
from streamlit_chat import message
import os
import ssl

from dotenv import load_dotenv
load_dotenv()

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

url = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")


def get_text():

    if prompt := st.chat_input("Ask me anything"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):

             data = {
            'chat_history': [],
            'question': prompt
            }

        body = str.encode(json.dumps(data))

        # The azureml-model-deployment header will force the request to go to a specific deployment.
        # Remove this header to have the request observe the endpoint traffic rules
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'proj-demo-aoai-qna-deploy-01' }
        req = urllib.request.Request(url, body, headers)


        response = urllib.request.urlopen(req)
        output = response.read()
        json_output = json.loads(output)
        response = st.markdown(json_output["chat_output"])

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": json_output["chat_output"]})