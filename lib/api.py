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
    Appended_url = f'https://f39q29puw2.execute-api.us-east-1.amazonaws.com/testing-stage'
    st.write(Test_example)
    response = requests.post(Appended_url, json=Test_example).json()
    st.write(json.dumps(response, indent=4))