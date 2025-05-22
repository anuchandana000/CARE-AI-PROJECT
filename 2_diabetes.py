import streamlit as st
import pandas as pd
import joblib
from translate import Translator
import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

logo = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/happy.json")
logo1 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/sad.json")
logo2 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/neutral.json")



# Set page config first
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

selected_language_code = st.session_state.get('selected_language', 'en')

translator = Translator(to_lang=selected_language_code)

# Translate a message function
def translate_text(text, lang_code):
    return translator.translate(text)  # Corrected to use the Translator API properly

dia = joblib.load('/Users/gayathriutla/Desktop/Projects/Sparks/diabetes.plk')

# Create Two Columns
col1, col2, col3 = st.columns([2, 4, 5])  # Adjusting column widths
with col1:
    st.image("logo.jpeg", width=1000)

# Left Column - Input Form
with col2:
    # Title translated
    st.title(translate_text("Diabetes Prediction", selected_language_code))

    # Age Input using Slider
    Age = st.slider(translate_text("Select Your Age:", selected_language_code), min_value=30, max_value=100, value=50, step=1)

    Sex = st.radio(translate_text("Select Your Gender:", selected_language_code), options=[translate_text("Male", selected_language_code), translate_text("Female", selected_language_code), translate_text("Other", selected_language_code)])
    Education = st.selectbox(translate_text("Select Your Educational Level:", selected_language_code), options=[
        translate_text("Post Graduate", selected_language_code),
        translate_text("Under Graduate", selected_language_code),
        translate_text("Intermediate", selected_language_code),
        translate_text("School", selected_language_code)
    ])

    income = st.text_input(translate_text("Enter Your Monthly Income:", selected_language_code))

    # BMI Input using Slider
    BMI = st.slider(translate_text("Select Your BMI:", selected_language_code), min_value=10.0, max_value=50.0, value=22.5, step=0.1)

    # High Blood Pressure
    HighBP = st.radio(translate_text("Do you have High Blood Pressure?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # High Cholesterol
    HighChol = st.radio(translate_text("Do you have High Cholesterol?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Cholesterol Check
    CholCheck = st.radio(translate_text("Have you had a Cholesterol Check?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Smoking Status
    Smoker = st.radio(translate_text("Do you smoke?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Stroke
    Stroke = st.radio(translate_text("Have you had a Stroke?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Heart Disease
    heartDiseaseorAttack = st.radio(translate_text("Have you had a Heart Disease?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Physical Activity
    PhysActivity = st.radio(translate_text("Do you engage in physical activity?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Fruits Consumption
    Fruits = st.radio(translate_text("Do you consume fruits regularly?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Heavy Alcohol Consumption
    HeavyAlcoholConsump = st.radio(translate_text("Do you consume heavy alcohol?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Veggies Consumption
    Veggies = st.radio(translate_text("Do you consume vegetables regularly?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Any Healthcare
    AnyHealthcare = st.radio(translate_text("Do you have any healthcare?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # No Doctors Cost
    NoDocbcCost = st.radio(translate_text("Do you avoid doctors due to cost?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # General Health (1: Excellent Health - 5: Poor Health)
    GenHlth = st.slider(translate_text("Rate your general health:", selected_language_code), 1, 5, 3, step=1)

    # Mental Health (1 - 40 scale)
    MentHlth = st.slider(translate_text("Rate your mental health:", selected_language_code), 1, 40, 20, step=1)

    PhystHlth = st.slider(translate_text("Rate your Physical health:", selected_language_code), 1, 40, 20, step=1)

    # Difficulty in Walking
    DiffWalk = st.radio(translate_text("Do you have difficulty walking?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])

    # Add space before the button to simulate centering
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Center the button using st.columns by creating an empty column on both sides
    button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
    with button_col2:
        predict_button = st.button(translate_text("Diabetes Risk", selected_language_code))

# Right Column - Display the Prediction Result
with col3:
    if predict_button:
        # Encoding mappings
        encoding_map = {
            "Sex": {"Male": 1, "Female": 0, "Other": 2},
            "Education": {
                "Post Graduate": 4,
                "Under Graduate": 3,
                "Intermediate": 2,
                "School": 1
            },
            "HighBP": {"Yes": 1, "No": 0},
            "HighChol": {"Yes": 1, "No": 0},
            "CholCheck": {"Yes": 1, "No": 0},
            "Smoker": {"Yes": 1, "No": 0},
            "Stroke": {"Yes": 1, "No": 0},
            "HeartDisease": {"Yes": 1, "No": 0},
            "PhysActivity": {"Yes": 1, "No": 0},
            "Fruits": {"Yes": 1, "No": 0},
            "Veggies": {"Yes": 1, "No": 0},
            "HvyAlcoholConsump": {"Yes": 1, "No": 0},
            "AnyHealthcare": {"Yes": 1, "No": 0},
            "NoDocbcCost": {"Yes": 1, "No": 0},
            "DiffWalk": {"Yes": 1, "No": 0}
        }

        # Creating encoded input dictionary
        encoded_input = {
            "HighBP": encoding_map["HighBP"][HighBP],
            "HighChol": encoding_map["HighChol"][HighChol],
            "CholCheck": encoding_map["CholCheck"][CholCheck],
            "BMI": BMI,
            "Smoker": encoding_map["Smoker"][Smoker],
            "Stroke": encoding_map["Stroke"][Stroke],
            "HeartDiseaseorAttack": encoding_map["HeartDisease"][heartDiseaseorAttack],  # Correct key
            "PhysActivity": encoding_map["PhysActivity"][PhysActivity],
            "Fruits": encoding_map["Fruits"][Fruits],
            "Veggies": encoding_map["Veggies"][Veggies],
            "HvyAlcoholConsump": encoding_map["HvyAlcoholConsump"][HeavyAlcoholConsump],  # Fixed key name
            "AnyHealthcare": encoding_map["AnyHealthcare"][AnyHealthcare],
            "NoDocbcCost": encoding_map["NoDocbcCost"][NoDocbcCost],
            "GenHlth": GenHlth,
            "MentHlth": MentHlth,
            "PhysHlth": PhystHlth,
            "DiffWalk": encoding_map["DiffWalk"][DiffWalk],
            "Sex": encoding_map["Sex"][Sex],
            "Age": Age,
            "Education": encoding_map["Education"][Education],
            "Income": float(income) if income else 3  # Ensuring numeric input
        }

        columns = [
            "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke", 
            "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", 
            "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", 
            "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"
            ]

        user_df = pd.DataFrame([encoded_input])
        prediction = dia.predict(user_df)
        if prediction == 0 :
                st_lottie(logo, speed=1, width=400, height=400, key="happy_anim")
                st.warning(translate_text('Great! Keep maintaining a healthy lifestyle',selected_language_code))
        elif prediction == 1:
            st_lottie(logo2, speed=1, width=400, height=400, key="neural_anim")
            st.warning(translate_text('You’re in the moderate risk, which means it’s a good time to remain proactive about your health',selected_language_code)) 
        else:
            col1,col2,col3 = st.columns([1,2,1])
            with col2:
                st_lottie(logo1, speed=1, width=150, height=300, key="sad_anim")
            st.warning(translate_text('Please take immediate medical advice and get a check-up.', selected_language_code))