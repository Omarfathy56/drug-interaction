import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    data = pd.read_csv("drug_interactions.csv")

    return data


df = load_data()
# Streamlit navigation
st.title("Welcome to the Smart Drug Safety Assistant")
st.write("This app helps pharmacists quickly check drug interactions and ensure medication safety.")
<<<<<<< HEAD


=======
>>>>>>> 4823c96 (Initial commit)
