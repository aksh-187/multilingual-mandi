import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="🌾 Multilingual Mandi AI", layout="wide")

# Load CSV
df = pd.read_csv("mandi_data.csv")

# --- CSS Styling ---
st.markdown("""
<style>
/* Body */
body {
    background-color: #f9f9f9;
}

/* Main title */
.title {
    color: #2a7f3e;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle {
    color: #555555;
    font-size: 18px;
    text-align: center;
    margin-top: 0;
    margin-bottom: 40px;
}

/* Card style */
.card {
    background-color: white;
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Button */
.stButton>button {
    background-color: #2a7f3e;
    color: white;
    font-size: 16px;
    padding: 10px 24px;
    border-radius: 8px;
    border: none;
}

/* Input box */
.stTextInput>div>div>input {
    padding: 10px;
    font-size: 16px;
}

/* Selectbox padding */
.stSelectbox>div>div>div>div {
    padding: 8px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .title { font-size: 32px; }
    .subtitle { font-size: 16px; }
    .stButton>button { width: 100%; }
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">🌾 Multilingual Mandi AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI assistant for Indian farmers & traders</div>', unsafe_allow_html=True)

# --- Language selection ---
language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Telugu", "Tamil", "Kannada"])

# --- Problem & Solution Cards ---
st.markdown('<div class="card"><b>Problem</b><ul><li>Get mandi prices in local language</li><li>Understand price trends</li><li>Access simple AI tools</li></ul></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><b>Solution</b><ul><li>Multilingual price queries</li><li>Easy explanations</li><li>Farmer-friendly UI</li></ul></div>', unsafe_allow_html=True)

# --- Crop input ---
crop_name = st.text_input("🌱 Enter Crop Name", placeholder="e.g. Tomato, Paddy, Onion")

# --- State dropdown ---
state = st.selectbox("Select State", df['State'].unique())

# --- District dropdown (dependent) ---
districts = df[df['State'] == state]['District'].unique()
district = st.selectbox("Select District", districts)

# --- Market dropdown (dependent) ---
markets = df[(df['State'] == state) & (df['District'] == district)]['Market'].unique()
market = st.selectbox("Select Market", markets)

# --- Get Mandi Info Button ---
if st.button("Get Mandi Info"):
    if crop_name.strip() == "":
        st.error("Please enter a crop name!")
    else:
        filtered = df[
            (df['Crop'].str.lower() == crop_name.strip().lower()) &
            (df['State'] == state) &
            (df['District'] == district) &
            (df['Market'] == market)
        ]
        if filtered.empty:
            st.error("Data not found! Try another crop or market.")
        else:
            price = filtered['Price'].values[0]
            st.success(f"{crop_name} price in {market}, {district}, {state}: ₹{price} per kg ({language})")
