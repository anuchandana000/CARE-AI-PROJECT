
import streamlit as st
from translate import Translator

st.markdown("<h1 style='text-align: center;'>Welcome to CARE-AI</h1>", unsafe_allow_html=True)

col1, col2, = st.columns([2, 4])

with col1:
    st.image("logo.jpeg", width=300)

with col2:
    languages = {
        "en": "English",
        "hi": "हिन्दी",
        "bn": "বাংলা",
        "te": "తెలుగు",
        "mr": "मराठी",
        "ta": "தமிழ்",
        "ur": "اردو",
        "gu": "ગુજરાતી",
        "ml": "മലയാളം",
        "kn": "ಕನ್ನಡ",
        "or": "ଓଡିଆ",
        "pa": "ਪੰਜਾਬੀ",
        "as": "অসমীয়া",
        "ne": "नेपाली",
        "kok": "कोंकणी",
        "mni": "মণিপুরি",
        "ks": "کشميري"
    }

    selected_language_code = st.selectbox(
        "Select your Language", 
        options=list(languages.keys()), 
        format_func=lambda x: languages[x]
    )

    st.session_state.selected_language = selected_language_code
    
    translator = Translator(to_lang=selected_language_code)

    def translate_text(text):
        return translator.translate(text)

    description = """
    It helps individuals, especially in rural areas with limited healthcare access, by predicting potential health issues based on symptoms. The app offers early-stage predictions for diseases like heart attacks, diabetes, Alzheimer's, and maternal health. It supports local languages for easier interaction, making it more user-friendly. Timely disease predictions help identify health issues early, potentially reducing 30% of deaths caused by late-stage diagnoses.
    """

    translated_description = translate_text(description)

    st.write(translated_description)

    symptom_options = {
        "Memory loss that disrupts daily life": "Memory loss that disrupts daily life",
        "Severe chest pain or discomfort": "Severe chest pain or discomfort",
        "Pregnancy": "Pregnancy",
        "Frequent urination and excessive thirst": "Frequent urination and excessive thirst"
    }

    translated_symptoms = {key: translate_text(value) for key, value in symptom_options.items()}

    symptom = st.selectbox(
        translate_text("Select Your Symptom"),
        options=list(translated_symptoms.values())
    )

    selected_symptom = next(key for key, value in translated_symptoms.items() if value == symptom)

    st.session_state.symptom = selected_symptom

button_col1, button_col2 = st.columns([2, 2])

with button_col2:
    predict_button = st.button("Let's predict")

if predict_button:
    selected_symptom = st.session_state.get('symptom', '')
    if selected_symptom == "Memory loss that disrupts daily life":
        st.switch_page("pages/1_alzheimers.py")
    elif selected_symptom == "Severe chest pain or discomfort":
        st.switch_page("pages/3_Heart_disease.py")
    elif selected_symptom == "Pregnancy":
        st.switch_page("pages/4_Maternal.py")
    elif selected_symptom == "Frequent urination and excessive thirst":
        st.switch_page("pages/2_diabetes.py")
