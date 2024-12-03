import streamlit as st


image_path = "images/img1.jpg"


def show():
    """Displays content for Type 1 page."""

    # Title of the page
    st.title("Diabetes Awareness")

    # Add a subtitle
    st.subheader("About Diabetes")

    # Brief Information about Diabetes
    st.write("""
        Diabetes is a chronic medical condition that occurs when the body is unable to 
        properly regulate blood sugar (glucose) levels. There are two main types:
        Type 1 diabetes, where the body does not produce insulin, and Type 2 diabetes, 
        where the body either resists insulin or doesn't produce enough.
    
        It is important to manage diabetes through diet, exercise, and medication to prevent 
        serious complications like heart disease, nerve damage, and kidney issues.
    """)


    st.image(image_path, caption="Diabetes Awareness")

    # Add some statistics or key facts about diabetes
    st.write("### Key Facts about Diabetes")
    st.write("""
    - Over 400 million people worldwide are affected by diabetes.
    - Type 2 diabetes accounts for around 90-95% of all diabetes cases.
    - Early diagnosis and proper management can significantly reduce the risks of complications.
    """)

    # Add a section with helpful resources or tips
    st.write("### Tips for Managing Diabetes")
    st.write("""
    - Eat a healthy, balanced diet rich in fiber and low in refined sugars.
    - Exercise regularly to maintain a healthy weight and improve insulin sensitivity.
    - Monitor blood glucose levels regularly and follow your healthcare provider's recommendations.
    """)

    # Footer with a message
    st.write("For more information, visit your healthcare provider or trusted diabetes resources.")













# Custom CSS to remove margins, borders, and paddings
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
            border: 0;
        }
        .block-container {
            padding: 0;
            margin: 0;
        }
        .css-1v3fvcr {
            padding: 0;
            margin: 0;
        }
        .css-18e3th9 {
            padding: 0;
            margin: 0;
        }
        .css-10trblm {
            margin: 0;
            padding: 0;
        }
        .css-14xtw13 {
            padding: 0;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)