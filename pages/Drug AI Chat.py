import streamlit as st
import google.generativeai as genai
from main import load_data

api_key = st.secrets["general"]["GOOGLE_API_KEY"]

df = load_data()
# Set up Gemini API key
genai.configure(api_key=api_key)

# Load dataset (replace 'drugs.csv' with your actual file)

# Use the best free Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to get a short drug description
def get_drug_info(drug_name):
    prompt = f"Give a short medical description of the drug '{drug_name}'. Keep it under 3 sentences."
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to handle chatbot responses
def chat_with_ai(user_input, drug_name):
    response = model.generate_content(f"Regarding {drug_name}: {user_input}")
    return response.text.strip()

# Streamlit UI
st.title("💊 Drug Information & AI Chatbot")

# Drug Selection
selected_drug = st.selectbox("Select a drug:", df["Drug 1"].unique())

if st.button("Get Drug Info"):
    info = get_drug_info(selected_drug)
    st.subheader("Drug Information:")
    st.write(f"**{info}**")

# AI Chatbot Section
st.subheader("💬 Ask the AI about the drug")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input for chat
user_input = st.chat_input("Ask me anything about the drug...")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    ai_response = chat_with_ai(user_input, selected_drug)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
