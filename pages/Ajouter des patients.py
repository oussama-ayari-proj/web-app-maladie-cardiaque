import streamlit as st
import time
import numpy as np
import pandas as pd


st.header('Ajouter des nouvelles entrées pour l\'entraînement')

integer_number = st.number_input("Enter an integer",
                                 min_value=-10,
                                 max_value=10,
                                 value=0)
st.write(integer_number, type(integer_number))

float_number = st.number_input("Enter a float",
                               min_value=-1.0,
                               max_value=1.0,
                               value=0.0)
st.write(float_number, type(float_number))
