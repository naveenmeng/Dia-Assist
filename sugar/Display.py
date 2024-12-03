import streamlit as st
import pandas as pd


def display_data():
    # Load CSV files
    try:
        prediction_data = pd.read_csv('prediction_results.csv')
        actual_data = pd.read_csv('user_input_data.csv')

        # Display the dataframes
        st.title("User Data:")
        st.dataframe(actual_data)
        st.title("Adviced Medicine")
        st.dataframe(prediction_data)
    except FileNotFoundError:
        st.error("Error: One or both CSV files are missing!")

    # Form for weekly test status inputs
    st.subheader("Enter Recent Tested Status of Diabetes")

    # Create a form
    with st.form("weekly_status_form"):
        week_data = []
        for i in range(1, 9):
            week_data.append(
                st.number_input(f"Week {i} Test Status", min_value=50, max_value=800, step=10, key=f"week_{i}"))

        # Submit button
        submitted = st.form_submit_button("Submit")

        if submitted:
            # Calculate the average
            average_status = sum(week_data) / len(week_data)
            st.success(f"Average Diabetes Status: {average_status:.2f}")



