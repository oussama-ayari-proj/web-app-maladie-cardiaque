import streamlit as st
import time
import numpy as np
import pandas as pd
from lib import api

st.header('Faire des predictions !!')
st.subheader('Data d\'entraînement actuelle')
data=pd.read_csv(st.session_state['database'])
if "output" in data.columns:
    data.drop(columns=['output'],inplace=True)
else:
    data.drop(columns=['target'],inplace=True)
st.write(data)
with st.form("my_form"):
    st.write("Saisir données d\'un patient:")
    inputs={}
    for col in data.columns:
        if not col in ["age","resting_blood_pressure","cholesterol","max_heart_rate_achieved","st_depression"]:
            inputs[col] = st.selectbox("Donner"+col+" du patient",data[col].unique())
            continue
        inputs[col] = st.number_input("Donner "+col+" du patient")

    submitted = st.form_submit_button("Envoyer")
    if submitted:
        api.envoyer_requete(inputs)
