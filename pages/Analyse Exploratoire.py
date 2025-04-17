import streamlit as st
import time
import numpy as np
import pandas as pd 
from lib import anaExp,preprocess,plot2D

st.set_page_config(page_title="Analyse Exploratoire", page_icon="📈")

if st.session_state['database']=="":
    st.write("Veuillez choisir le fichier à traiter !!")
else:
    data=pd.read_csv(st.session_state['database'])
    data=preprocess.preprocess(data)
    if st.button("Exporter"):
        preprocess.export(data)
    anaExp.afficherDimensions(data)
    with st.sidebar:
        section=st.multiselect('Afficher',['details colonnes','les types de colonnes','les premiéres lignes','par colonnes','les valeurs uniques par colonne','résumé statistique','distribution de la valeur cible','distribution des colonnes','pair plot','reg plots'],default=[],key='4')

    if 'details colonnes' in section:
        anaExp.afficherLesDetailsColonnes()
    if 'les types de colonnes' in section:
        anaExp.afficherTypeColonnes(data)
    if 'les premiéres lignes' in section:
        anaExp.afficherPremiersLignes(data)
    if 'par colonnes' in section:
        anaExp.afficherParColonnes(data)
    if 'les valeurs uniques par colonne' in section:
        anaExp.afficherValeursUniquesParColonnes(data)
    if 'résumé statistique' in section:
        anaExp.ResumeStatistique(data)
    if 'distribution de la valeur cible' in section:
        plot2D.distribution_de_target(data)
    if 'distribution des colonnes' in section:
        plot2D.distribution_cols(data)
    if 'pair plot' in section:
        plot2D.pairplot(data)
    if 'reg plots' in section:
        plot2D.regplots(data)
