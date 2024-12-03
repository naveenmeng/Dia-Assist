import streamlit as st
from Pages.prediction_data import predict_diabetes

def show():
    """Displays content for diabetes prediction with form fields."""
    st.title("Diabetes Prediction")
    st.subheader("Fill in the details")

    # Initialize default values in session state if not already set
    if "gender" not in st.session_state:
        st.session_state.gender = 0
    if "age" not in st.session_state:
        st.session_state.age = 1
    if "hypertension" not in st.session_state:
        st.session_state.hypertension = 0
    if "heart_disease" not in st.session_state:
        st.session_state.heart_disease = 0
    if "smoking_history" not in st.session_state:
        st.session_state.smoking_history = 'never'
    if "bmi" not in st.session_state:
        st.session_state.bmi = 10
    if "hba1c_level" not in st.session_state:
        st.session_state.hba1c_level = 4
    if "blood_glucose_level" not in st.session_state:
        st.session_state.blood_glucose_level = 50

    # Define a function to reset the form
    def reset_form():
        st.session_state.gender = 0
        st.session_state.age = 1
        st.session_state.hypertension = 0
        st.session_state.heart_disease = 0
        st.session_state.smoking_history = 'never'
        st.session_state.bmi = 0
        st.session_state.hba1c_level = 0
        st.session_state.blood_glucose_level = 50

    # Create a form for entering the data
    with st.form(key='prediction_form'):
        # Form fields for user input
        gender = st.selectbox(
            "Gender",
            [0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female",
            key="gender"
        )
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            key="age"
        )
        hypertension = st.selectbox(
            "Hypertension",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="hypertension"
        )
        heart_disease = st.selectbox(
            "Heart Disease",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="heart_disease"
        )
        smoking_history = st.selectbox(
            "Smoking History",
            ['never', 'No Info', 'current'],
            key="smoking_history"
        )
        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=50.0,
            key="bmi"
        )
        hba1c_level = st.number_input(
            "HbA1c Level",
            min_value=4.0,
            max_value=20.0,
            key="hba1c_level"
        )
        blood_glucose_level = st.number_input(
            "Blood Glucose Level",
            min_value=50.0,
            max_value=300.0,
            key="blood_glucose_level"
        )

        # Submit and Reset buttons
        submit_button = st.form_submit_button("Submit")
        reset_button = st.form_submit_button("Reset", on_click=reset_form)

        # Logic when form is submitted
        if submit_button:
            try:
                # Call the function from prediction_data.py to predict diabetes
                result = predict_diabetes(
                    gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level
                )
                # Display the prediction result below the form
                st.success(result)
            except ValueError:
                st.error("Please enter valid values.")
