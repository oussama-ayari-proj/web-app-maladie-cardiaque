import streamlit as st
import pandas as pd

def afficherDimensions(data):
    dimensions=data.shape
    st.header('Taille des données d\'entraînement actuelle:')
    st.metric(label="Nombre de ligne",value=dimensions[0])
    st.metric(label="Nombre de colonnes",value=dimensions[1])

def afficherPremiersLignes(data):
    st.header('Premiers Lignes')
    st.dataframe(data.head(5))

def afficherParColonnes(data):
    st.header('Selectionner les colonnes que vous voulez consultez ensemble')
    cols = st.multiselect('select colonne(s):', data.columns, default = [])
    st.dataframe(data[cols])

def afficherValeursUniquesParColonnes(data):
    st.header('Valeurs qui composent chaque colonnes')
    col = st.selectbox('selectionner colonne(s):', data.columns)
    st.dataframe(data[col].unique())

def afficherLesDetailsColonnes():
    st.header('Description des colonnes:')
    st.html(
    "<ol><li>age: age in years</li><li>sex: sex <ul><li>1 = male</li><li>0 = female</li></ul></li><li>cp: chest pain type<ul><li>Value 0: typical angina</li><li>Value 1: atypical angina</li><li>Value 2: non-anginal pain</li><li>Value 3: asymptomatic</li></ul></li><li>trestbps: resting blood pressure (in mm Hg on admission to the hospital)</li><li>chol: serum cholestoral in mg/dl</li><li>fbs: (fasting blood sugar &gt; 120 mg/dl) <ul><li>1 = true; </li><li>0 = false</li></ul></li><li>restecg: resting electrocardiographic results<ul><li>Value 0: normal</li><li>Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of &gt; 0.05 mV)</li><li>Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria</li></ul></li><li>thalach: maximum heart rate achieved</li><li>exang: exercise induced angina <ul><li>1 = yes</li><li>0 = no</li></ul></li><li>oldpeak = ST depression induced by exercise relative to rest</li><li>slope: the slope of the peak exercise ST segment<ul><li>Value 0: upsloping</li><li>Value 1: flat</li><li>Value 2: downsloping</li></ul></li><li>ca: number of major vessels (0-3) colored by flourosopy</li><li>thal: <ul><li>0 = <code>error (in the original dataset 0 maps to NaN's)</code></li><li>1 = fixed defect</li><li>2 = normal </li><li>3 = reversable defect </li></ul></li><li>target (the lable): <ul><li>0 = no disease, </li><li>1 = disease</li></ul></li></ol>"
    )

def afficherTypeColonnes(data):
    st.header('Colonnes et ses types')
    st.dataframe(data.dtypes)

def ResumeStatistique(data):
    st.header('Résumé statistique')
    st.dataframe(data.describe())


