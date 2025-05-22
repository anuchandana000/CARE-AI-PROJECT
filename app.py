import streamlit as st

main = st.Page(
    "pages/0_main.py",
    title="🏠 Mainpage ",
)

alzheimers = st.Page(
    "pages/1_alzheimers.py",
    title="🧠 Alzheimer's",
)

diabetes = st.Page(
    "pages/2_diabetes.py",
    title="🍭 Diabetes ",
)

heart_disease = st.Page(
    "pages/3_Heart_disease.py",
    title="❤️ Heart Disease ",
)

maternal = st.Page(
    "pages/4_Maternal.py",
    title="🤰 Maternal Care "
)

pg = st.navigation(pages=[main, alzheimers, diabetes, heart_disease, maternal])
pg.run()
