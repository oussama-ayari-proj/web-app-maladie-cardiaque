import requests
import json
import streamlit as st


def envoyer_requete(data):
    payload=""
    l=list(data.values())
    n=len(l)
    for i in range(n-1):
        payload=payload+str(l[i])+", "
    payload=payload+str(l[n-1])
    Test_example = { "data": payload}
    Appended_url = f'https://qbv3csrmu3.execute-api.us-east-1.amazonaws.com/test-1/my-resource'
    st.write(Test_example)
    response = requests.post(Appended_url, json=Test_example).json()
    st.write(json.dumps(response, indent=4))