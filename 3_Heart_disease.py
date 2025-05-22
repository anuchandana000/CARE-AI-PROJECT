import joblib
import streamlit as st
from translate import Translator
import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

logo = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/happy.json")
logo1 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/sad.json")

st.set_page_config(page_title="Heart Attack Prediction", layout="centered")

heart = joblib.load('/Users/gayathriutla/Desktop/Projects/Sparks/Heart_disease.plk')

selected_language_code = st.session_state.get('selected_language', 'en')

translator = Translator(to_lang=selected_language_code)

def translate_text(text, lang_code):
    return translator.translate(text)

col1, col2, col3 = st.columns([2, 4, 5])
with col1:
    st.image("logo.jpeg", width=1000)

with col2:
    st.title(translate_text("Heart Attack Prediction", selected_language_code))

    Age = st.slider(translate_text("Select Your Age:", selected_language_code), min_value=30, max_value=100, value=50, step=1)

    gender_options = [translate_text("Male", selected_language_code), translate_text("Female", selected_language_code), translate_text("Other", selected_language_code)]
    Sex = st.radio(translate_text("Select Your Gender:", selected_language_code), gender_options)

    Education_options = [
        translate_text("Post Graduate", selected_language_code),
        translate_text("Under Graduate", selected_language_code),
        translate_text("Intermediate", selected_language_code),
        translate_text("School", selected_language_code)
    ]
    Education = st.selectbox(translate_text("Select Your Educational Level:", selected_language_code), Education_options)

    BMI = st.slider(translate_text("Select Your BMI:", selected_language_code), min_value=10.0, max_value=50.0, value=22.5, step=0.1)

    HighBP_options = [translate_text("Yes", selected_language_code), translate_text("No", selected_language_code)]
    HighBP = st.radio(translate_text("Do you have High Blood Pressure?", selected_language_code), HighBP_options)

    HighChol = st.radio(translate_text("Do you have High Cholesterol?", selected_language_code), HighBP_options)

    CholCheck = st.radio(translate_text("Have you had a Cholesterol Check?", selected_language_code), HighBP_options)

    Smoker = st.radio(translate_text("Do you smoke?", selected_language_code), HighBP_options)

    Stroke = st.radio(translate_text("Have you had a Stroke?", selected_language_code), HighBP_options)

    Diabetes_options = [
        translate_text("No Diabetes", selected_language_code),
        translate_text("Pre-Diabetes", selected_language_code),
        translate_text("Diabetes", selected_language_code)
    ]
    Diabetes = st.selectbox(translate_text("Diabetes Status:", selected_language_code), Diabetes_options)

    PhysActivity = st.radio(translate_text("Do you engage in physical activity?", selected_language_code), HighBP_options)

    Fruits = st.radio(translate_text("Do you consume fruits regularly?", selected_language_code), HighBP_options)

    HeavyAlcoholConsump = st.radio(translate_text("Do you consume heavy alcohol?", selected_language_code), HighBP_options)

    Veggies = st.radio(translate_text("Do you consume vegetables regularly?", selected_language_code), HighBP_options)

    AnyHealthcare = st.radio(translate_text("Do you have any healthcare?", selected_language_code), HighBP_options)

    NoDocbcCost = st.radio(translate_text("Do you avoid doctors due to cost?", selected_language_code), HighBP_options)

    GenHlth = st.slider(translate_text("Rate your general health:", selected_language_code), 1, 5, 3, step=1)

    MentHlth = st.slider(translate_text("Rate your mental health:", selected_language_code), 1, 40, 20, step=1)

    PhystHlth = st.slider(translate_text("Rate your Physical health:", selected_language_code), 1, 40, 20, step=1)

    DiffWalk = st.radio(translate_text("Do you have difficulty walking?", selected_language_code), HighBP_options)

    income = st.text_input(translate_text("Enter Your Monthly Income:", selected_language_code))

    button_col1, button_col2, button_col3 = st.columns([1, 2,2])
    with button_col2:
        predict_button = st.button(translate_text("Predict", selected_language_code))

with col3:
    if predict_button:
        encoding_map = {
            "Sex": {"Male": 1, "Female": 0, "Other": 2},
            "Education": {"Post Graduate": 4, "Under Graduate": 3, "Intermediate": 2, "School": 1},
            "HighBP": {"Yes": 1, "No": 0},
            "HighChol": {"Yes": 1, "No": 0},
            "CholCheck": {"Yes": 1, "No": 0},
            "Smoker": {"Yes": 1, "No": 0},
            "Stroke": {"Yes": 1, "No": 0},
            "Diabetes": {"No Diabetes": 0, "Pre-Diabetes": 1, "Diabetes": 2},
            "PhysActivity": {"Yes": 1, "No": 0},
            "Fruits": {"Yes": 1, "No": 0},
            "Veggies": {"Yes": 1, "No": 0},
            "HvyAlcoholConsump": {"Yes": 1, "No": 0},
            "AnyHealthcare": {"Yes": 1, "No": 0},
            "NoDocbcCost": {"Yes": 1, "No": 0},
            "DiffWalk": {"Yes": 1, "No": 0}
        }

        user_data = {
            "HighBP": encoding_map["HighBP"][HighBP],
            "HighChol": encoding_map["HighChol"][HighChol],
            "CholCheck": encoding_map["CholCheck"][CholCheck],
            "BMI": BMI,
            "Smoker": encoding_map["Smoker"][Smoker],
            "Stroke": encoding_map["Stroke"][Stroke],
            "Diabetes": encoding_map["Diabetes"][Diabetes],
            "PhysActivity": encoding_map["PhysActivity"][PhysActivity],
            "Fruits": encoding_map["Fruits"][Fruits],
            "Veggies": encoding_map["Veggies"][Veggies],
            "HvyAlcoholConsump": encoding_map["HvyAlcoholConsump"][HeavyAlcoholConsump],
            "AnyHealthcare": encoding_map["AnyHealthcare"][AnyHealthcare],
            "NoDocbcCost": encoding_map["NoDocbcCost"][NoDocbcCost],
            "GenHlth": GenHlth,
            "MentHlth": MentHlth,
            "PhysHlth": PhystHlth,
            "DiffWalk": encoding_map["DiffWalk"][DiffWalk],
            "Sex": encoding_map["Sex"][Sex],
            "Age": Age,
            "Education": encoding_map["Education"][Education],
            "Income": float(income) if income else 3
        }
        import pandas as pd
        df = pd.DataFrame([user_data])

        prediction = heart.predict(df)
        if prediction == 0 :
                st_lottie(logo, speed=1, width=400, height=400, key="happy_anim")
                st.warning(translate_text('Great! Keep maintaining a healthy lifestyle', selected_language_code))

        else:
            col1,col2 = st.columns([1,3])
            with col2:
                st_lottie(logo1, speed=1, width=150, height=300, key="sad_anim")
            st.warning(translate_text('Please take immediate medical advice and get a check-up.', selected_language_code))