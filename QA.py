from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Retrieve API key from the environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found! Please set GEMINI_API_KEY in the .env file.")

# Step 3: Configure Google Generative AI
genai.configure(api_key=api_key)

# Step 4: Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # Ensure this model name is valid for your API
    generation_config=generation_config,
)
chat = model.start_chat(history=[])

# Function to get a response from the chatbot
def get_gemini_response(question):
    response = chat.send_message(question)
    return response

# Step 5: Configure Streamlit page
st.set_page_config(page_title="CHATBOT-DEMO", page_icon="🔮")
st.header("Gemini Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input field and button for user interaction
user_input = st.text_input("Ask a question:", key="input")
submit = st.button("ASK ME QUESTION")

# Handle the input and generate a response
if submit and user_input:
    try:
        response = get_gemini_response(user_input)
        st.session_state["chat_history"].append({"role": "You", "text": user_input})
        
        response_text = response.text if hasattr(response, "text") else "No response text available."
        st.write(response_text)
        
        st.session_state["chat_history"].append({"role": "BOT", "text": response_text})
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display the chat history
st.subheader("Chat History")
for message in st.session_state["chat_history"]:
    st.write(f"{message['role']}: {message['text']}")
