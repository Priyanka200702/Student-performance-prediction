import streamlit as st
import pickle


with open("linear.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Predictor")

hours = st.number_input(
    "Hours Studied",
    min_value=0,
    max_value=24,
    value=5,
    step=1
)

previous_score = st.number_input(
    "Previous Scores",
    min_value=0,
    max_value=100,
    value=50
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

sleep = st.number_input(
    "Sleep hours",
    min_value=0,
    max_value=24,
    value=7,
    step=1
)
ques= st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    max_value=10,
    value=5,
    step=1
)

if st.button("Predict Performance"):
    
    extracurricular_value = 1 if extracurricular == "Yes" else 0

    prediction = model.predict([[
        hours,
        previous_score,
        extracurricular_value,
        sleep,
        ques
    ]])

    st.success(f"Predicted Performance Index: {prediction[0]:.2f}")