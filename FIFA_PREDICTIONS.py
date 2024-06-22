
pip install joblib
import streamlit as st
import joblib
import pandas as pd

# Load the model and fitted scaler
model = joblib.load('best_ensemble_model.pkl')
scalar = joblib.load('scaler.pkl')

# App title and description
st.title('FIFA Player Rating Prediction')
st.write('This app predicts a FIFA player\'s rating based on their attributes.')

# Function to get user inputs
def get_user_inputs():
    height_cm = st.number_input('Height (cm)')
    weight_kg = st.number_input('Weight (kg)')
    age = st.number_input('Age')
    physic = st.number_input('Physic')
    power_strength = st.number_input('Power Strength')
    power_jumping = st.number_input('Power Jumping')
    movement_agility = st.number_input('Movement Agility')
    movement_balance = st.number_input('Movement Balance')
    dribbling = st.number_input('Dribbling')
    skill_dribbling = st.number_input('Skill Dribbling')
    skill_ball_control = st.number_input('Skill Ball Control')
    shooting = st.number_input('Shooting')
    passing = st.number_input('Passing')
    skill_long_passing = st.number_input('Skill Long Passing')
    skill_fk_accuracy = st.number_input('Skill FK Accuracy')
    attacking_crossing = st.number_input('Attacking Crossing')
    attacking_finishing = st.number_input('Attacking Finishing')
    attacking_heading_accuracy = st.number_input('Attacking Heading Accuracy')
    attacking_short_passing = st.number_input('Attacking Short Passing')
    attacking_volleys = st.number_input('Attacking Volleys')
    mentality_aggression = st.number_input('Mentality Aggression')
    mentality_interceptions = st.number_input('Mentality Interceptions')
    mentality_positioning = st.number_input('Mentality Positioning')
    mentality_vision = st.number_input('Mentality Vision')
    mentality_penalties = st.number_input('Mentality Penalties')
    mentality_composure = st.number_input('Mentality Composure')
    movement_reactions = st.number_input('Movement Reactions')
    pace = st.number_input('Pace')
    movement_acceleration = st.number_input('Movement Acceleration')
    movement_sprint_speed = st.number_input('Movement Sprint Speed')
    power_stamina = st.number_input('Power Stamina')
    power_shot_power = st.number_input('Power Shot Power')
    power_long_shots = st.number_input('Power Long Shots')
    defending = st.number_input('Defending')

    inputs = {
        'height_cm': [height_cm], 
        'weight_kg': [weight_kg], 
        'age': [age], 
        'physic': [physic], 
        'power_strength': [power_strength], 
        'power_jumping': [power_jumping], 
        'ovement_agility': [movement_agility], 
        'ovement_balance': [movement_balance], 
        'dribbling': [dribbling], 
        'kill_dribbling': [skill_dribbling], 
        'kill_ball_control': [skill_ball_control], 
        'hooting': [shooting], 
        'passing': [passing], 
        'kill_long_passing': [skill_long_passing], 
        'kill_fk_accuracy': [skill_fk_accuracy], 
        'attacking_crossing': [attacking_crossing], 
        'attacking_finishing': [attacking_finishing], 
        'attacking_heading_accuracy': [attacking_heading_accuracy], 
        'attacking_short_passing': [attacking_short_passing], 
        'attacking_volleys': [attacking_volleys], 
        'entality_aggression': [mentality_aggression], 
        'entality_interceptions': [mentality_interceptions], 
        'entality_positioning': [mentality_positioning], 
        'entality_vision': [mentality_vision], 
        'entality_penalties': [mentality_penalties], 
        'entality_composure': [mentality_composure], 
        'ovement_reactions': [movement_reactions], 
        'pace': [pace], 
        'ovement_acceleration': [movement_acceleration], 
        'ovement_sprint_speed': [movement_sprint_speed], 
        'power_stamina': [power_stamina], 
        'power_shot_power': [power_shot_power], 
        'power_long_shots': [power_long_shots], 
        'defending': [defending]
    }

    return pd.DataFrame(inputs)

# Use the scalar and model to display the output to the user
user_inputs = get_user_inputs()
scaled_inputs = scalar.transform(user_inputs)
prediction = model.predict(scaled_inputs)

st.write('Predicted Rating:', prediction[0])