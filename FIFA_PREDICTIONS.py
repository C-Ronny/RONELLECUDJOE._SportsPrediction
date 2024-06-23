import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model_file.pkl')

# Define the expected feature names used during training
expected_features = ['movement_reactions', 'mentality_composure', 'passing', 'dribbling', 'physic',
                     'attacking_short_passing', 'mentality_vision', 'skill_long_passing', 'shooting',
                     'power_shot_power', 'age']

def main():
    st.title("FIFA Player Rating Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Player Rating Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)