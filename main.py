import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    data = pd.read_csv("drug_interactions.csv")

    return data


df = load_data()
# --- Styling ---
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 42px;
        color: #6C63FF;
        margin-bottom: 0;
    }
    .sub-text {
        text-align: center;
        font-size: 18px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Main UI ---
st.markdown("<h1 class='main-title'>💊 Smart Drug Safety Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Helping pharmacists ensure medication safety and avoid harmful interactions.</p>", unsafe_allow_html=True)

# Optional visual element
st.image("medecine.jpg", use_container_width=True)

# Add quick stats or guide
st.markdown("### 📋 How it works:")
st.markdown("""
1. Use the **sidebar** to search for drugs or check interactions.
2. The app will highlight **known interactions** from the dataset.
3. For unknown pairs, our AI assistant will help with real-time analysis.
""")
