import streamlit as st
import joblib 
import pandas as pd
import json
import requests
from translate import Translator
from streamlit_lottie import st_lottie

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

logo = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/happy.json")
logo1 = load_lottiefile("/Users/gayathriutla/Desktop/Projects/Sparks/sad.json")

st.set_page_config(page_title="Alzheimer's Prediction", layout="centered")

alzheimers = joblib.load('/Users/gayathriutla/Desktop/Projects/Sparks/alzheimers.plk')

selected_language_code = st.session_state.get('selected_language', 'en')

translator = Translator(to_lang=selected_language_code)

def translate_text(text, lang_code):
    return translator.translate(text)

label_mappings = {
    "Gender": {"Male": 0, "Female": 1, "Other": 2},
    "Education Level": {"School": 0, "Intermediate": 1, "Under Graduate": 2, "Post Graduate": 3},
    "Physical Activity Level": {"Low": 0, "Medium": 1, "High": 2},
    "Smoking Status": {"Never": 0, "Former": 1, "Current": 2},
    "Alcohol Consumption": {"None": 0, "Moderate": 1, "Heavy": 2},
    "Diabetes": {"No": 0, "Yes": 1},
    "Hypertension": {"No": 0, "Yes": 1},
    "Cholesterol Level": {"Low": 0, "High": 1},
    "Family History of Alzheimer’s": {"No": 0, "Yes": 1},
    "Depression Level": {"Low": 0, "Medium": 1, "High": 2},
    "Sleep Quality": {"Poor": 0, "Average": 1, "Good": 2},
    "Dietary Habits": {"Unhealthy": 0, "Average": 1, "Healthy": 2},
    "Air Pollution Exposure": {"Low": 0, "Medium": 1, "High": 2},
    "Employment Status": {"Unemployed": 0, "Employed": 1},
    "Marital Status": {"Single": 0, "Married": 1},
    "Social Engagement Level": {"Low": 0, "Medium": 1, "High": 2},
    "Income Level": {"Low": 0, "Medium": 1, "High": 2},
    "Stress Levels": {"Low": 0, "Medium": 1, "High": 2},
    "Urban vs Rural Living": {"Rural": 0, "Urban": 1},
}

col1, col2, col3 = st.columns([2, 4, 5])
with col1:
    st.image("logo.jpeg", width=1000)

with col2:
    st.title(translate_text("Alzheimer's Prediction", selected_language_code))

    age = st.slider(translate_text("Select Your Age:", selected_language_code), min_value=30, max_value=100, value=50, step=1)
    gender = st.radio(translate_text("Select Your Gender:", selected_language_code), options=[translate_text("Male", selected_language_code), translate_text("Female", selected_language_code), translate_text("Other", selected_language_code)])
    education = st.selectbox(translate_text("Select Your Educational Level:", selected_language_code), options=[
        translate_text("Post Graduate", selected_language_code),
        translate_text("Under Graduate", selected_language_code),
        translate_text("Intermediate", selected_language_code),
        translate_text("School", selected_language_code)
    ])
    bmi = st.slider(translate_text("Select Your BMI:", selected_language_code), min_value=10.0, max_value=50.0, value=22.5, step=0.1)
    physical_activity = st.radio(translate_text("Physical Activity Level:", selected_language_code), options=[
        translate_text("Low", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("High", selected_language_code)
    ])
    smoking_status = st.radio(translate_text("Smoking Status:", selected_language_code), options=[
        translate_text("Never", selected_language_code),
        translate_text("Former", selected_language_code),
        translate_text("Current", selected_language_code)
    ])
    alcohol_consumption = st.radio(translate_text("Alcohol Consumption:", selected_language_code), options=[
        translate_text("None", selected_language_code),
        translate_text("Moderate", selected_language_code),
        translate_text("Heavy", selected_language_code)
    ])
    diabetes = st.radio(translate_text("Diabetes:", selected_language_code), options=[
        translate_text("No", selected_language_code),
        translate_text("Yes", selected_language_code)
    ])
    hypertension = st.radio(translate_text("Do You Have Hypertension?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])
    cholesterol = st.radio(translate_text("Cholesterol Level:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    family_history = st.radio(translate_text("Family History of Alzheimer's?", selected_language_code), options=[
        translate_text("Yes", selected_language_code),
        translate_text("No", selected_language_code)
    ])
    depression = st.radio(translate_text("Depression Level:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    sleep_quality = st.radio(translate_text("Sleep Quality:", selected_language_code), options=[
        translate_text("Good", selected_language_code),
        translate_text("Average", selected_language_code),
        translate_text("Poor", selected_language_code)
    ])
    diet = st.radio(translate_text("Dietary Habits:", selected_language_code), options=[
        translate_text("Healthy", selected_language_code),
        translate_text("Average", selected_language_code),
        translate_text("Unhealthy", selected_language_code)
    ])
    air_pollution = st.radio(translate_text("Air Pollution Exposure:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    employment_status = st.radio(translate_text("Employment Status:", selected_language_code), options=[
        translate_text("Employed", selected_language_code),
        translate_text("Unemployed", selected_language_code)
    ])
    marital_status = st.radio(translate_text("Marital Status:", selected_language_code), options=[
        translate_text("Single", selected_language_code),
        translate_text("Married", selected_language_code)
    ])
    social_engagement = st.radio(translate_text("Social Engagement Level:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    income_level = st.radio(translate_text("Income Level:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    stress_level = st.radio(translate_text("Stress Levels:", selected_language_code), options=[
        translate_text("High", selected_language_code),
        translate_text("Medium", selected_language_code),
        translate_text("Low", selected_language_code)
    ])
    place_of_living = st.radio(translate_text("Place of Living:", selected_language_code), options=[
        translate_text("Urban", selected_language_code),
        translate_text("Rural", selected_language_code)
    ])
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        submit = st.button(translate_text("Submit", selected_language_code))

with col3:
    if submit:
        encoded_input = {
            "Age": age,
            "Gender": label_mappings["Gender"][gender],
            "Education Level": label_mappings["Education Level"][education],
            "BMI": bmi,
            "Physical Activity Level": label_mappings["Physical Activity Level"][physical_activity],
            "Smoking Status": label_mappings["Smoking Status"][smoking_status],
            "Alcohol Consumption": label_mappings["Alcohol Consumption"][alcohol_consumption],
            "Diabetes": label_mappings["Diabetes"][diabetes],
            "Hypertension": label_mappings["Hypertension"][hypertension],
            "Cholesterol Level": label_mappings["Cholesterol Level"][cholesterol],
            "Family History of Alzheimer’s": label_mappings["Family History of Alzheimer’s"][family_history],
            "Depression Level": label_mappings["Depression Level"][depression],
            "Sleep Quality": label_mappings["Sleep Quality"][sleep_quality],
            "Dietary Habits": label_mappings["Dietary Habits"][diet],
            "Air Pollution Exposure": label_mappings["Air Pollution Exposure"][air_pollution],
            "Employment Status": label_mappings["Employment Status"][employment_status],
            "Marital Status": label_mappings["Marital Status"][marital_status],
            "Social Engagement Level": label_mappings["Social Engagement Level"][social_engagement],
            "Income Level": label_mappings["Income Level"][income_level],
            "Stress Levels": label_mappings["Stress Levels"][stress_level],
            "Urban vs Rural Living": label_mappings["Urban vs Rural Living"][place_of_living],
        }

        user_df = pd.DataFrame([encoded_input])
        prediction = alzheimers.predict(user_df)
        if prediction == 0 :
            st_lottie(logo, speed=1, width=400, height=400, key="happy_anim")
            st.warning(translate_text('Great! Keep maintaining a healthy lifestyle.', selected_language_code))
        else:
            col1,col2,col3 = st.columns([1,2,1])
            with col2:
                st_lottie(logo1, speed=1, width=150, height=300, key="sad_anim")
            st.warning(translate_text('Please take immediate medical advice and get a check-up.', selected_language_code))