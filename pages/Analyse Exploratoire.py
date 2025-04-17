import streamlit as st
import time
import numpy as np
import pandas as pd 
from lib import anaExp,preprocess,plot2D

st.set_page_config(page_title="Analyse Exploratoire", page_icon="📈")


data=pd.read_csv('Data/heart.csv')
data=preprocess.preprocess(data)
st.session_state['data']=data

anaExp.afficherDimensions(data)
anaExp.afficherLesDetailsColonnes()
anaExp.afficherTypeColonnes(data)
anaExp.afficherPremiersLignes(data)
anaExp.afficherParColonnes(data)
anaExp.afficherValeursUniquesParColonnes(data)
anaExp.ResumeStatistique(data)

plot2D.distribution_de_target(data)
plot2D.distribution_cols(data)
plot2D.pairplot(data)
plot2D.regplots(data)
