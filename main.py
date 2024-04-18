import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import subprocess

# Function to display Prediksi_Stunting.py file
def display_prediksi_stunting():
    with open("Prediksi_Stunting.py", "r") as f:
        code = compile(f.read(), "Prediksi_Stunting.py", 'exec')
        exec(code, globals())
        
# Function to display Prediksi_Stunting_Page2.py file
def display_prediksi_stunting_2():
    with open("Prediksi_Stunting_Page2.py", "r") as f:
        code = compile(f.read(), "Prediksi_Stunting_Page2.py", 'exec')
        exec(code, globals())

# Sidebar navigation
sidebar_option = st.sidebar.radio("Navigation", ["Prediksi Satu Keluarga", "Prediksi Data Excel"])

if sidebar_option == "Prediksi Satu Keluarga":
    display_prediksi_stunting()
     
elif sidebar_option == "Prediksi Data Excel":
    display_prediksi_stunting_2()
