# Gemini-Bot-Demo-model
### Explanation of the Code:

This project demonstrates how to build a chatbot using Google Generative AI (Gemini model) with Streamlit as the user interface. Here's a breakdown of the code:

---

#### **1. Importing Required Libraries**
```python
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
```
- **dotenv**: To load environment variables from the `.env` file.
- **streamlit**: To build a web-based UI for the chatbot.
- **os**: To access environment variables.
- **google.generativeai**: To interact with Google Generative AI models.

---

#### **2. Loading Environment Variables**
```python
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found! Please set GEMINI_API_KEY in the .env file.")
```
- The `load_dotenv()` function loads the `.env` file and retrieves the `GEMINI_API_KEY` API key.
- The code ensures that the key exists and raises an error if it’s missing.

---

#### **3. Configuring Google Generative AI**
```python
genai.configure(api_key=api_key)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro", 
    generation_config=generation_config,
)
chat = model.start_chat(history=[])
```
- **Configuration**:
  - `temperature`, `top_p`, and `top_k` control the randomness and creativity of responses.
  - `max_output_tokens` defines the maximum number of tokens in the output.
- The chatbot model is initialized with `start_chat`.

---

#### **4. Chat Function**
```python
def get_gemini_response(question):
    response = chat.send_message(question)
    return response
```
- This function sends the user’s input (`question`) to the Gemini model and retrieves its response.

---

#### **5. Streamlit Page Setup**
```python
st.set_page_config(page_title="CHATBOT-DEMO", page_icon="🔮")
st.header("Gemini Chatbot")
```
- Configures the Streamlit page title, icon, and header.

---

#### **6. Managing Chat History**
```python
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
```
- Chat history is stored in `st.session_state` so it persists across user interactions.

---

#### **7. Handling User Input and Responses**
```python
user_input = st.text_input("Ask a question:", key="input")
submit = st.button("ASK ME QUESTION")

if submit and user_input:
    try:
        response = get_gemini_response(user_input)
        st.session_state["chat_history"].append({"role": "You", "text": user_input})
        
        response_text = response.text if hasattr(response, "text") else "No response text available."
        st.write(response_text)
        
        st.session_state["chat_history"].append({"role": "BOT", "text": response_text})
    except Exception as e:
        st.error(f"An error occurred: {e}")
```
- **Input Handling**:
  - User enters a question in the input box and clicks the button.
  - The input is sent to the chatbot using `get_gemini_response`.
- **Response Handling**:
  - The bot's response is displayed on the page and stored in the chat history.

---

#### **8. Displaying Chat History**
```python
st.subheader("Chat History")
for message in st.session_state["chat_history"]:
    st.write(f"{message['role']}: {message['text']}")
```
- Displays the entire chat history in a conversational format.

---

### README.md for GitHub:

```markdown
# Gemini-Bot-Demo-Model

A demo chatbot built using Google Generative AI (Gemini Model) and Streamlit. This project demonstrates how to integrate the Gemini model into a user-friendly web interface for conversational AI.

---

## Features

- **Conversational AI**: Interact with the Gemini model to ask questions and get AI-generated responses.
- **Streamlit UI**: Clean and simple web interface for a seamless chatbot experience.
- **Customizable**: Configure model parameters like `temperature`, `top_p`, and `max_output_tokens`.

---

## Prerequisites

- Python 3.8 or above
- A valid Google Generative AI API key
- Installed dependencies (`python-dotenv`, `streamlit`, `google-generative-ai`)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Gemini-Bot-Demo-Model.git
cd Gemini-Bot-Demo-Model
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File
Create a `.env` file in the project root and add your API key:
```plaintext
GEMINI_API_KEY=your_google_api_key_here
```

### 4. Run the Application
```bash
streamlit run chatbot_app.py
```

### 5. Access the App
Open your browser and navigate to:
```
http://localhost:8501
```

---

## Project Structure

```
Gemini-Bot-Demo-Model/
│
├── chatbot_app.py       # Main application file
├── requirements.txt     # Dependencies for the project
├── .env                 # API key file (not included in GitHub)
└── README.md            # Project documentation
```

---

## Configuration Parameters

- **Temperature**: Controls response randomness. Higher values (e.g., 1) produce more creative responses.
- **Top-p**: Nucleus sampling for diversity. Lower values make responses more focused.
- **Max Output Tokens**: Limits the response length.
- **Model Name**: Ensure compatibility with your API (e.g., `chat-bison-001`).

---

## Troubleshooting

1. **Missing API Key**:
   - Ensure the `.env` file exists and contains a valid `GEMINI_API_KEY`.
2. **Invalid Model Name**:
   - Check if the `model_name` used in the code matches the available models in your API plan.
3. **Streamlit Errors**:
   - Ensure all dependencies are installed and run the app in a compatible Python environment.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.

---

## Author

**Mohit Pathak**  
GitHub: [yourusername](https://github.com/yourusername)
```

---

Let me know if you need help refining this further! 😊
