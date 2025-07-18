import streamlit as st
import pandas as pd
import joblib
from PIL import Image
from sklearn.preprocessing import LabelEncoder

# Load model
model = joblib.load("asthma_prediction_pipeline.pkl")

# Load header image
image = Image.open("asthma_banner.png")

# App Title + Branding
st.set_page_config(page_title="Asthma Risk Predictor", layout="centered")
st.image(image, use_container_width=True)
st.markdown("<h2 style='text-align: center; color: teal;'>Asthma Risk Prediction Tool</h2>", unsafe_allow_html=True)
st.markdown("This tool uses a trained machine learning model to estimate asthma likelihood based on synthetic health data.", unsafe_allow_html=True)
st.markdown("---")

# Input Fields
st.subheader("🔎 Enter Patient Information")

# Streamlit input fields for asthma prediction
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
smoking_status = st.selectbox("Smoking Status", ["Never Smoked", "Former Smoker", "Current Smoker"])
family_history = st.selectbox("Family History of Asthma", ["Yes", "No"])
allergies = st.selectbox("Allergies", ["None", "Dust", "Pollen", "Pet Dander", "Food", "Other"])
air_pollution = st.selectbox("Air Pollution Level", ["Low", "Moderate", "High"])
activity_level = st.selectbox("Physical Activity Level", ["Sedentary", "Moderate", "Active"])
occupation = st.selectbox("Occupation Type", ["Desk Job", "Outdoor Work", "Medical", "Education", "Other"])
comorbidities = st.selectbox("Comorbidities", ["None", "Diabetes", "Hypertension", "Obesity", "Other"])

age = st.slider("Age", 1, 90, 25)
bmi = st.slider("BMI", 10.0, 50.0, 22.0)
feno = st.slider("FeNO Level (ppb)", 0, 100, 25)
er_visits = st.slider("Number of ER Visits in Past Year", 0, 10, 0)
med_adherence = st.slider("Medication Adherence (%)", 0, 100, 75)
pef = st.slider("Peak Expiratory Flow (L/min)", 100, 600, 400)

# Assemble user input into a DataFrame for prediction
input_dict = {
    "Age": age,
    "Gender": gender,
    "BMI": bmi,
    "Smoking_Status": smoking_status,
    "Family_History": family_history,
    "Allergies": allergies,
    "Air_Pollution_Level": air_pollution,
    "Physical_Activity_Level": activity_level,
    "Occupation_Type": occupation,
    "Comorbidities": comorbidities,
    "Medication_Adherence": med_adherence,
    "Number_of_ER_Visits": er_visits,
    "Peak_Expiratory_Flow": pef,
    "FeNO_Level": feno
}
input_df = pd.DataFrame([input_dict])
prediction = model.predict(input_df)[0]

# Prediction Button
if st.button("🔍 Predict Asthma Risk"):
    prediction = model.predict(input_df)[0]
    st.markdown("---")
    if prediction == 1:
        st.markdown("<h4 style='color: red;'>High likelihood of asthma detected.</h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h4 style='color: green;'>Low likelihood of asthma detected.</h4>", unsafe_allow_html=True)

    st.markdown("⚠️ This result is based on synthetic data and should not replace medical advice.")

# Credits
st.markdown("---")
st.markdown("📌 **Project Author:** Eric Inkoom Ayitey<br>"
            "🧠 **Focus Areas:** Data Science | Healthcare Analytics | ML for Social Impact<br>"
            "📅 **Version:** v1.0 — July 2025", unsafe_allow_html=True)