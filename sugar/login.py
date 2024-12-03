import streamlit as st
image_path = "images/ai-logo.webp"
def show():
    """Displays the login page."""
    st.image(image_path, caption="Diabetes Awareness", width=200)  # Adjust width here
    st.title("Login Page")

    # Initialize session states for managing login
    if "login_attempt" not in st.session_state:
        st.session_state.login_attempt = False
    if "processing" not in st.session_state:
        st.session_state.processing = False  # Prevents concurrent login attempts

    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Button click logic
    if st.button("Login"):
        if not st.session_state.processing:  # Allow login processing only if not already processing
            st.session_state.processing = True  # Lock further interactions

            # Simulate login validation
            if username == "admin" and password == "password":  # Replace with actual authentication
                st.session_state.logged_in = True
                st.success("Login successful! Redirecting...")
            else:
                st.error("Invalid username or password.")

            # Reset processing state to allow new attempts
            st.session_state.processing = False
