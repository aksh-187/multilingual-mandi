import streamlit as st

# Page config
st.set_page_config(page_title="Multilingual Mandi AI", layout="wide")

# Multilingual dictionary
translations = {
    "English": {
        "title": "🌾 Multilingual Mandi AI",
        "subtitle": "AI assistant for Indian farmers & traders",
        "select_language": "🌐 Select Language",
        "select_state": "🏞 Select State",
        "select_district": "📍 Select District",
        "enter_crop": "🌱 Enter Crop Name",
        "button": "Get Mandi Info",
        "landing_desc": "Get live mandi prices in your local language. Understand trends and make informed decisions.",
        "problem": "Problem",
        "solution": "Solution",
        "problem_items": ["Get mandi prices in local language", "Understand price trends", "Access simple AI tools"],
        "solution_items": ["Multilingual price queries", "Easy explanations", "Farmer-friendly UI"],
        "error_crop": "Please enter a crop name!",
        "info_placeholder": "Price data integration coming next 🚜📈",
    },
    "Hindi": {
        "title": "🌾 बहुभाषी मंडी एआई",
        "subtitle": "भारतीय किसानों और व्यापारियों के लिए एआई सहायक",
        "select_language": "🌐 भाषा चुनें",
        "select_state": "🏞 राज्य चुनें",
        "select_district": "📍 जिला चुनें",
        "enter_crop": "🌱 फसल का नाम दर्ज करें",
        "button": "मंडी जानकारी प्राप्त करें",
        "landing_desc": "अपनी स्थानीय भाषा में मंडी की कीमतें प्राप्त करें। रुझानों को समझें और सूचित निर्णय लें।",
        "problem": "समस्या",
        "solution": "समाधान",
        "problem_items": ["स्थानीय भाषा में मंडी की कीमतें प्राप्त करें", "कीमत रुझान समझें", "सरल एआई उपकरणों तक पहुँच"],
        "solution_items": ["बहुभाषी मूल्य प्रश्न", "सरल व्याख्याएँ", "किसान-मित्र इंटरफ़ेस"],
        "error_crop": "कृपया फसल का नाम दर्ज करें!",
        "info_placeholder": "कीमत डेटा एकीकरण जल्द आ रहा है 🚜📈",
    }
    # Add more languages here...
}

# CSS styling
st.markdown("""
<style>
body {background-color: #f9f9f9;}
.title {color: #2a7f3e; font-size: 42px; font-weight: bold; text-align: center; margin-bottom: 0;}
.subtitle {color: #555555; font-size: 18px; text-align: center; margin-top: 0; margin-bottom: 40px;}
.card {background-color: white; border-radius: 12px; padding: 25px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
.stButton>button {background-color: #2a7f3e; color: white; font-size: 16px; padding: 10px 24px; border-radius: 8px; border: none;}
.stTextInput>div>div>input {padding: 10px; font-size: 16px;}
.stSelectbox>div>div>div>div {padding: 8px;}
</style>
""", unsafe_allow_html=True)

# Landing Page
st.markdown('<div class="title">🌾 Multilingual Mandi AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI assistant for Indian farmers & traders</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px;">Get live mandi prices in your local language. Understand trends and make informed decisions.</p>', unsafe_allow_html=True)

st.markdown("---")

# Language selection
language = st.selectbox("🌐 Select Language", list(translations.keys()))
t = translations[language]

# Problem & Solution
st.markdown(f'<div class="card"><b>{t["problem"]}</b><ul>' + "".join([f"<li>{i}</li>" for i in t["problem_items"]]) + '</ul></div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><b>{t["solution"]}</b><ul>' + "".join([f"<li>{i}</li>" for i in t["solution_items"]]) + '</ul></div>', unsafe_allow_html=True)

# State & District (dummy data)
states = ["Maharashtra", "Karnataka", "Tamil Nadu"]
districts = {
    "Maharashtra": ["Pune", "Nagpur", "Mumbai"],
    "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"]
}

state = st.selectbox(t["select_state"], states)
district = st.selectbox(t["select_district"], districts[state])

# Crop input
crop_name = st.text_input(t["enter_crop"], placeholder="e.g. Tomato, Paddy, Onion")

# Button
if st.button(t["button"]):
    if crop_name.strip() == "":
        st.error(t["error_crop"])
    else:
        st.success(f"Showing mandi info for {crop_name} in {district}, {state} [{language}]")
        st.info(t["info_placeholder"])
