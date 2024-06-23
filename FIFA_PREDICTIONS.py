import streamlit as st 
from sklearn import preprocessing
import pickle as pkl
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pkl.load(open('GradientBoostingRegressor.pkl', 'gbr'))

player_df = pd.read_csv('playerDataFrame.csv')

default_values = player_df.mean()

columns = ['potential', 'value_eur', 'wage_eur', 'movement_reactions', 'mentality_composure']

def main(): 
    st.title("FIFA Player Rating Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Player Rating Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    potential = st.number_input("Potential: ",min_value=0, value=0) 
    value_eur = st.number_input("Value (Euros): ", min_value=0, value=0) 
    wage_eur = st.number_input("Wage (Euros): ", min_value=0, value=0)
    movement_reactions = st.number_input("Movement Reaction: ", min_value=0, value=0)
    mentality_composure = st.number_input("Mentality Composure: ", min_value=0, value=0)
    
    
    ########----------------------TO DO----------------------########
    if st.button("Predict"):
        features = {
            'Potential': potential,
            'Value': value_eur,
            'Wage': wage_eur,
            'Movement Reactions': movement_reactions,
            'Mentality Composure': mentality_composure
        }
        
        # Create a DataFrame with user input
        df = pd.DataFrame([features])
        
        # Fill missing columns with default (mean) values
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = default_values[col]
        
        # Ensure the order of columns matches the model's expected order
        df = df[model.feature_names_in_]
        
        prediction = model.predict(df)
        output = prediction[0]
        st.success(f'Player Rating is {output:.0f}')

if __name__=='__main__': 
    main()