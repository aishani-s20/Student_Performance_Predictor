import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("model1.pkl")
st.title("Student Exam Score Predictor")

study_hours = st.slider ("Study Hours per Day", 0.0, 12.0, 2.0)
social_media_hours = st.slider ("Social Media Hours", 0.0, 12.0, 2.0)
netflix_hours = st.slider ("Netflix Hours", 0.0, 12.0, 2.0)
attendance = st. slider ("Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider ("Mental Health Rating (1-10)", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours per Night", 0.0, 12.0, 7.0)
exercise = st.slider("Exercise Hours", 0.0, 12.0, 7.0)

diet = st.selectbox("Diet quality", ["Good","Fair", "Poor"])
extra = st.selectbox("Extracurricular participation", ["Yes","No"])
part_time_job = st.selectbox("Part-Time Job",["Yes","No"])

ptj_encoded = 1 if part_time_job == "Yes" else 0
extra_encoded = 1 if extra == "Yes" else 0
diet_encoded = 0
if (diet == "Good"):
    diet_encoded = 3
elif (diet == "Fair"):
    diet_encoded = 2
else:
    diet_encoded = 1

if st.button("Predict Exam Score"):
    input_data = np.array([[study_hours, social_media_hours, netflix_hours, ptj_encoded, attendance, sleep_hours, diet_encoded, exercise, mental_health, extra_encoded]])   
    prediction = model.predict(input_data)[0]
    prediction = max(0 , min(100, prediction))
    # print(prediction, type(prediction))


    st.success(f"Predicted exam score: {float(prediction): .2f}")
