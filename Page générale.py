import pandas as pd 
import numpy as np 
import streamlit as st

st.set_page_config(layout = "wide", page_title = "Proto")

st.header("Prototype !!!")



message = """
        __Fonctionnalités disponibles__
        """
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Options:',
        ['Analyse exploratoire',
        'Ajouter des données pour l\'entraînement', 
        'Faire des predictions'])

