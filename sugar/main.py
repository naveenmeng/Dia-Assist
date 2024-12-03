import streamlit as st

from Pages.about import show as about
from Pages.Home import show as Home
from Pages.Prediction import show as prediction_page
from Pages.healthcare_chatbot import show as chatbot
from Display import display_data
from Pages.diabetes_ui import show as insulin


image_path = "images/ai-logo.webp"  # Path to your logo image


def show():
    # Example sidebar widgets
    st.sidebar.image(image_path, caption="Menu", width=150)  # Adjust width here
    # st.sidebar.title("Menu")

    # Update the sidebar to remove 'Chat' from options
    page = st.sidebar.radio("Choose a section:",
                            ["Home", "Diabetes Prediction", "Diabetes insulation","Data" , "Dia-Chat", "About"])

    # Handle the page navigation logic
    if page == "Home":
        Home()
    elif page == "Diabetes Prediction":
        prediction_page()
    elif page == "Diabetes insulation":
        insulin() # You are using this page to display the form and chat on the same page.
    elif page == "Dia-Chat":
        chatbot()
    elif page == "Data":
        display_data()
    elif page == "About":
        about()
    #
    # # Add a logout button in the sidebar
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.success("You have been logged out.")
