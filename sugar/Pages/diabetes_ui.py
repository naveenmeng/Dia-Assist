import sys
import os

# Append the current directory to the system path
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pandas as pd
from diabetes_functions import predict_and_suggest


# Define a function to map smoking history to numeric values
def map_smoking_history(smoking_history):
    mapping = {
        'never': 0,  # 0 for 'never'
        'No Info': 1,  # 1 for 'No Info'
        'current': 2  # 2 for 'current'
    }
    return mapping.get(smoking_history, -1)  # Default to -1 if not found


def show():
    st.title("Diabetes Prediction and Insulin Dosage")

    # Input fields for user data
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    age = st.number_input("Age", min_value=1, max_value=120)
    hypertension = st.selectbox("Hypertension", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    heart_disease = st.selectbox("Heart Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    # Map smoking history to numeric values
    smoking_history = st.selectbox("Smoking History", ['never', 'No Info', 'current'])
    smoking_history_encoded = map_smoking_history(smoking_history)

    bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, step=0.1)
    hba1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, step=0.1)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=10.0, max_value=800.0)
    weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=200.0, step=0.1)

    # When the user clicks 'Submit'
    if st.button("Submit"):
        # Prepare the input data
        user_input = pd.DataFrame({
            'gender': [gender],
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'smoking_history': [smoking_history_encoded],  # Use the encoded value for smoking history
            'bmi': [bmi],
            'HbA1c_level': [hba1c_level],
            'blood_glucose_level': [blood_glucose_level]
        })

        # Call the function to predict diabetes and insulin dosage
        diabetes_type, insulin_dosage, basal_dosage, bolus_dosage, insulin_type, medications_info = predict_and_suggest(
            user_input, weight)

        # Display the results
        st.write(f"**Diabetes Type**: Type {diabetes_type}")
        st.write(f"**Suggested Total Insulin Dosage**: {insulin_dosage:.2f} units")
        st.write(f"**Basal Insulin**: {round(basal_dosage)} units")
        st.write(f"**Bolus Insulin**: {round(bolus_dosage)} units")

        if medications_info:
            st.subheader("Suggested Medications for Type 2 Diabetes:")
            for med in medications_info:
                st.write(f"**Brand Name**: {med['Brand Name']}")
                st.write(f"**Generic Name**: {med['Generic Name']}")
                st.write(f"**Suggested Dosage**: {med['Suggested Dosage']}")
                st.write("**Usage**: ")
                for i, point in enumerate(med["Usage"], 1):
                    st.write(f"{i}. {point}")
                st.write("-" * 40)


if __name__ == "__main__":
    show()