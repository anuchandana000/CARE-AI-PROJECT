import joblib
import pandas as pd
import json
import requests
from translate import Translator
import streamlit as st
from streamlit_lottie import st_lottie

praga = joblib.load('/Users/gayathriutla/Desktop/Projects/Sparks/pregnancy_risk.plk')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

logo = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/happy.json")
logo1 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/sad.json")
logo2 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/neutral.json")

selected_language_code = st.session_state.get('selected_language', 'en')
translator = Translator(to_lang=selected_language_code)

def translate_text(text, lang_code):
    return translator.translate(text)

col1, col2, col3 = st.columns([1,4, 4])
with col1:
    st.image("logo.jpeg", width=1000)

with col2:
    st.title(translate_text("Maternal Health Prediction", selected_language_code))
    
    age = st.slider(translate_text("Select your age:", selected_language_code), 15, 50, 25)
    systolic_bp = st.slider(translate_text("Systolic Blood Pressure (mmHg):", selected_language_code), 80, 200, 120, 1)
    diastolic_bp = st.slider(translate_text("Diastolic Blood Pressure (mmHg):", selected_language_code), 50, 130, 80, 1)
    bs = st.slider(translate_text("Blood Sugar Level (mg/dL):", selected_language_code), 50, 300, 100, 1)
    body_temp = st.slider(translate_text("Body Temperature (°F):", selected_language_code), 95.0, 105.0, 98.6, 0.1)
    heart_rate = st.slider(translate_text("Heart Rate (bpm):", selected_language_code), 40, 150, 70, 1)
    
    col_center = st.columns([1, 2, 4])
    with col_center[1]:
        submit = st.button(translate_text("Submit", selected_language_code))

with col3:
    if submit:
        user_data = {
            "Age": age,
            "SystolicBP": systolic_bp,
            "DiastolicBP": diastolic_bp,
            "BS": bs,
            "BodyTemp": body_temp,
            "HeartRate": heart_rate
        }

        columns = [
            "Age","SystolicBP","DiastolicBP","BS","BodyTemp","HeartRate"
        ]
        data = [[23,90,60,7.01,98,76]]

        user_df1 = pd.DataFrame(data, columns=columns)

        user_df = pd.DataFrame([user_data])
        prediction = praga.predict(user_df1)
        
        if prediction[0] == "low risk":
            st_lottie(logo, speed=1, width=400, height=400, key="happy_anim")
            st.warning(translate_text("Great! Keep maintaining a healthy lifestyle.", selected_language_code))
        
        elif prediction[0] == "mid risk":
                st_lottie(logo2, speed=1, width=400, height=400, key="neutral_anim")
                st.warning(translate_text("You’re in the moderate risk category, which means it’s a good time to remain proactive about your health.", selected_language_code))
        
        else:
            col1, col2 = st.columns([1, 3])
            with col2:
                st_lottie(logo1, speed=1, width=150, height=300, key="sad_anim")
            st.warning(translate_text("Please take immediate medical advice and get a check-up.", selected_language_code))