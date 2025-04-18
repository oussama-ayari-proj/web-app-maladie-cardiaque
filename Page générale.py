import pandas as pd 
import numpy as np 
import streamlit as st
import os



st.set_page_config(layout = "wide", page_title = "Proto")
st.session_state['database']=""
st.header("Prototype !!!")


st.subheader("Page d'acceuil de l'hopital ou bien qq stats !!")

st.header("Choisir la base de données à utiliser")
directory_path = "Data"
contents = os.listdir(directory_path)
database=st.selectbox('Les bases disponibles:',contents)
st.session_state['database']=directory_path+"/"+database
