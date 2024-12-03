import streamlit as st
import login
import main

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# App routing logic
if st.session_state.logged_in:
    main.show()
else:
    login.show()
