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
    Appended_url = f'https://f39q29puw2.execute-api.us-east-1.amazonaws.com/testing-stage/mt-resource'
    st.write(Test_example)
    response = requests.post(Appended_url, json=Test_example).json()
    res=json.dumps(response, indent=4)
    if res=="1":
        st.error("Patient a une probabilité de plus de 50% d\'avoir un Rétrécissement du diamètre des artères", icon="🚨")
    else:
        st.success("Patient a une probabilité moins de 50% d\'avoir un Rétrécissement du diamètre des artères", icon="✅")
