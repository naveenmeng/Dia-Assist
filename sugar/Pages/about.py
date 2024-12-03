import streamlit as st

def show():
    st.title("About This Chatbot")
    st.write("""
    Welcome to the Diabetes Management Chatbot! This tool is designed to assist individuals in managing their diabetes by providing:

    - **Answers to Diabetes-Related Questions**: Ask any question related to diabetes management, nutrition, exercise, or emergency care.
    - **Personal Reminders**: Set custom reminders for important tasks like medication, meal times, or glucose monitoring.

    ### Features:
    - **Interactive Chat**: Uses OpenAI’s advanced GPT model to generate accurate, informative responses.
    - **Custom Reminders**: Helps users manage daily routines for effective diabetes care.
    - **Simple and Intuitive Interface**: Built with Streamlit for ease of use.

    ### How to Use:
    1. **Chat with Assistant**: Type your questions in the provided input box.
    2. **Set Reminders**: Use the "Manage Reminders" section to create personalized reminders.
    3. **View Reminders**: Access a list of all upcoming reminders.

    ### Disclaimer:
    - This chatbot is an educational tool and should not replace medical advice. Always consult with a healthcare professional for medical concerns.
    """)
    st.markdown("---")
    st.subheader("About the Technology")
    st.write("""
    - **Framework**: Built using [Streamlit](https://streamlit.io/), a Python-based framework for building interactive web applications.
    - **AI Model**: Powered by OpenAI's GPT-3.5/4, ensuring state-of-the-art conversational capabilities.
    - **Design Philosophy**: Focused on simplicity and user-friendliness for non-technical users.
    """)
