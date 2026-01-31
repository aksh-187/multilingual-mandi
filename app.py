import streamlit as st

st.set_page_config(page_title="Multilingual Mandi AI", layout="wide")

LANG = {
    "English": {
        "title": "🌾 Multilingual Mandi AI",
        "subtitle": "AI assistant for Indian farmers & traders",
        "select_language": "🌐 Select Language",
        "select_state": "🏞 Select State",
        "select_district": "📍 Select District",
        "enter_crop": "🌱 Enter Crop Name",
        "button": "Get Mandi Info",
        "error": "Please enter a crop name",
        "showing": "Showing mandi info for",
        "trend": "Prices are rising 📈",
        "advice": "Good time to sell"
    },
    "Hindi": {
        "title": "🌾 बहुभाषी मंडी एआई",
        "subtitle": "भारतीय किसानों और व्यापारियों के लिए एआई सहायक",
        "select_language": "🌐 भाषा चुनें",
        "select_state": "🏞 राज्य चुनें",
        "select_district": "📍 जिला चुनें",
        "enter_crop": "🌱 फसल का नाम दर्ज करें",
        "button": "मंडी जानकारी प्राप्त करें",
        "error": "कृपया फसल का नाम दर्ज करें",
        "showing": "मंडी जानकारी दिखा रहे हैं",
        "trend": "भाव बढ़ रहे हैं 📈",
        "advice": "बेचने का अच्छा समय"
    },
    "Telugu": {
        "title": "🌾 బహుభాషా మండీ AI",
        "subtitle": "భారత రైతులు మరియు వ్యాపారుల కోసం AI సహాయకుడు",
        "select_language": "🌐 భాషను ఎంచుకోండి",
        "select_state": "🏞 రాష్ట్రాన్ని ఎంచుకోండి",
        "select_district": "📍 జిల్లాను ఎంచుకోండి",
        "enter_crop": "🌱 పంట పేరు నమోదు చేయండి",
        "button": "మండీ సమాచారం పొందండి",
        "error": "దయచేసి పంట పేరును నమోదు చేయండి",
        "showing": "మండీ సమాచారం చూపిస్తోంది",
        "trend": "ధరలు పెరుగుతున్నాయి 📈",
        "advice": "అమ్మడానికి మంచి సమయం"
    }
}

STATE_DISTRICTS = {
    "Maharashtra": ["Pune", "Nagpur", "Nashik"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubli"],
    "Telangana": ["Hyderabad", "Warangal", "Karimnagar"]
}

# ---------- HEADER FIRST ----------
st.markdown(
    "<h1 style='text-align:center;color:#2a7f3e;'>🌾 Multilingual Mandi AI</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>AI assistant for Indian farmers & traders</p>",
    unsafe_allow_html=True
)

# ---------- LANGUAGE SELECTOR ----------
language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Telugu"])
T = LANG[language]

st.markdown("---")

# ---------- MAIN CONTROLS ----------
state = st.selectbox(T["select_state"], list(STATE_DISTRICTS.keys()))
district = st.selectbox(T["select_district"], STATE_DISTRICTS[state])
crop = st.text_input(T["enter_crop"])

if st.button(T["button"]):
    if crop.strip() == "":
        st.error(T["error"])
    else:
        st.success(f"{T['showing']} {crop} in {district}, {state}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Min Price", "₹1800")
        c2.metric("Avg Price", "₹2200")
        c3.metric("Max Price", "₹2600")
        st.info(T["trend"])
        st.success(T["advice"])
