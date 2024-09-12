import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load('insurance.pkl')
# Streamlit interface
st.title("Insurance Cost Prediction")

# # Collect user input
# age = st.number_input("Age", min_value=1.0,max_value=120.0, value = 1.0,key='person_age')
# bmi = st.number_input("BMI", min_value=0.0,max_value=60.0,value = 0.0)
# children = st.number_input("Number of Children", min_value = 0.0,value= 0.0)
# sex_male = st.selectbox("Gender", ["Female", "Male"])
# smoker_yes = st.selectbox("Smoker", ["No", "Yes"])
# region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# # Encode inputs to match the model's expected format
# sex_male = 1 if sex_male == "Male" else 0
# smoker_yes = 1 if smoker_yes == "Yes" else 0
# region_northwest = region_southeast = region_southwest = 0

# if region == "Northwest":
#     region_northwest = 1
# elif region == "Southeast":
#     region_southeast = 1
# elif region == "Southwest":
#     region_southwest = 1

# # Create a DataFrame with the input data
# input_data = pd.DataFrame({
#     'age': [age],
#     'bmi': [bmi],
#     'children': [children],
#     'sex_male': [sex_male],
#     'smoker_yes': [smoker_yes],
#     'region_northwest': [region_northwest],
#     'region_southeast': [region_southeast],
#     'region_southwest': [region_southwest],
# })

# # Make predictions
# # prediction = model.predict(input_data)[0]
# # Prediction and reset
# if st.button("Predict insurance"):
#     prediction = model.predict(input_data)
#     st.success(f"Predicted Insurance Cost: ${prediction[0]:.2f}")
    
    # st.session_state.person_age = 1.0

# Function to reset all inputs
# Function to reset all inputs
def reset_inputs():
    st.session_state['reset'] = True

# Check if the 'reset' flag is in session state
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

# Collect user input using default values
age = st.number_input("Age", min_value=0.0, max_value=120.0, value=0.0 if st.session_state.reset else st.session_state.get('age', 0.0), key='age')
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=0.0 if st.session_state.reset else st.session_state.get('bmi', 0.0), key='bmi')
children = st.number_input("Number of Children", min_value=0.0, value=0.0 if st.session_state.reset else st.session_state.get('children', 0.0), key='children')
sex_male = st.selectbox("Gender", ["Female", "Male"], index=0 if st.session_state.reset else ["Female", "Male"].index(st.session_state.get('sex_male', "Female")), key='sex_male')
smoker_yes = st.selectbox("Smoker", ["No", "Yes"], index=0 if st.session_state.reset else ["No", "Yes"].index(st.session_state.get('smoker_yes', "No")), key='smoker_yes')
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"], index=0 if st.session_state.reset else ["Northeast", "Northwest", "Southeast", "Southwest"].index(st.session_state.get('region', "Northeast")), key='region')

# Encode inputs to match the model's expected format
sex_male = 1 if sex_male == "Male" else 0
smoker_yes = 1 if smoker_yes == "Yes" else 0
region_northwest = region_southeast = region_southwest = 0

if region == "Northwest":
    region_northwest = 1
elif region == "Southeast":
    region_southeast = 1
elif region == "Southwest":
    region_southwest = 1

import random
# Create a DataFrame with the input data
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'sex_male': [sex_male],
    'smoker_yes': [smoker_yes],
    'region_northwest': [region_northwest],
    'region_southeast': [region_southeast],
    'region_southwest': [region_southwest],
})

# Prediction
if st.button("Predict insurance"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Insurance Cost: ${prediction[0]:.2f}")
    
    # Reset the flag after prediction
    st.session_state.reset = True

    reset_inputs()

# Button to reset the inputs manually
# if st.button("Reset"):
#     reset_inputs()
    