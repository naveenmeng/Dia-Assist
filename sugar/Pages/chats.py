import streamlit as st


def show():
    """Displays the Chat page with data from the Type 1 form."""

    # Retrieve the data from session state
    ppbs = st.session_state.get("ppbs", None)
    hbaic = st.session_state.get("hbaic", None)
    bmi = st.session_state.get("bmi", None)
    age = st.session_state.get("age", None)

    # Display the data on the Chat page
    if ppbs is not None and hbaic is not None and bmi is not None and age is not None:
        st.title("Chat - Data Overview")
        st.write(f"**PPBS:** {ppbs}")
        st.write(f"**HBAIC:** {hbaic}")
        st.write(f"**BMI:** {bmi}")
        st.write(f"**Age:** {age}")

        # Here, you can display or process data further (e.g., chat functionality or analytics)
    else:
        st.warning("No data submitted yet. Please fill out the form on the Type 1 page.")
