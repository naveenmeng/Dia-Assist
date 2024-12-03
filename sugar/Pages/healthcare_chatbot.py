import streamlit as st
from serpapi.google_search import GoogleSearch


# Function to search Google using SerpAPI
def search_google(query, api_key,num_results=20):
    params = {
        "q": query,
        "hl": "en",  # Language (English)
        "gl": "us",  # Country (United States)
        "api_key": api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Get the first search result snippet
    if "organic_results" in results:
        return results["organic_results"][0]["snippet"]
    else:
        return "Sorry, I couldn't find any relevant information."


# Streamlit function to handle chatbot interface
def show():
    # Title for the Streamlit app
    st.title("Diabetes Chatbot")

    # Introduce the chatbot
    st.write("Hi! I can answer your questions about diabetes. Ask me anything (Type 'exit' to stop).")

    # Create a session state for storing the conversation
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # User input field
    user_query = st.text_input("You:", "")

    # API key for SerpAPI (replace with your actual key)
    api_key = "4e8edda58a1ebe22670b79a738fd0c743c1d7252a8ccbafdc5c68f83c85b8a74"

    # If the user enters a query
    if user_query:
        # Check if user wants to exit
        if user_query.lower() == "exit":
            st.session_state['messages'].append({"user": "Diabetes Chatbot: Goodbye! Stay healthy."})
        else:
            # Call the search function and get the response
            response = search_google(user_query, api_key)
            st.session_state['messages'].append({"user": user_query, "chatbot": response})

    # Display conversation history
    chat_container = st.empty()  # Container to hold the chat UI
    with chat_container:
        for message in st.session_state['messages']:
            if 'user' in message:
                # Display user message (align to the left)
                st.markdown(
                    f"<div style='padding: 10px; margin: 5px; background-color: #DCF8C6; border-radius: 10px; max-width: 100%; word-wrap: break-word;'>You: {message['user']}</div>",
                    unsafe_allow_html=True)
            if 'chatbot' in message:
                # Display chatbot response (align to the right)
                st.markdown(
                    f"<div style='padding: 10px; margin: 5px; background-color: #E4E6EB; border-radius: 10px; max-width: 100%; word-wrap: break-word; text-align:left;'>Diabetes Chatbot: {message['chatbot']}</div>",
                    unsafe_allow_html=True)

    # Scroll to the latest message automatically (using Streamlit's beta_expander)
    st.markdown('<style>div[data-testid="stTextInput"] {padding-top: 5px;}</style>', unsafe_allow_html=True)

