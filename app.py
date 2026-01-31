import streamlit as st
import pandas as pd

st.set_page_config(page_title="Multilingual Mandi AI", layout="wide")

LANG = {
    "English": {
        "title": "🌾 Multilingual Mandi AI",
        "subtitle": "AI assistant for Indian farmers & traders",
        "problem_title": "Problem",
        "problems": [
            "Mandi prices not available in local language",
            "No simple price trend understanding",
            "No decision support for farmers"
        ],
        "solution_title": "Solution",
        "solutions": [
            "Multilingual mandi price access",
            "AI-based trend explanation",
            "Simple sell / hold advice"
        ],
        "select_language": "🌐 Select Language",
        "select_state": "🏞 Select State",
        "select_district": "📍 Select District",
        "enter_crop": "🌱 Enter Crop Name",
        "button": "Get Mandi Info",
        "error": "Please enter a crop name",
        "trend_up": "Prices are rising 📈",
        "trend_down": "Prices are falling 📉",
        "advice_sell": "Good time to sell",
        "advice_hold": "Better to wait",
        "showing": "Showing mandi info for"
    },
    "Hindi": {
        "title": "🌾 बहुभाषी मंडी एआई",
        "subtitle": "भारतीय किसानों और व्यापारियों के लिए एआई सहायक",
        "problem_title": "समस्या",
        "problems": [
            "स्थानीय भाषा में मंडी भाव नहीं",
            "भाव का रुझान समझना कठिन",
            "निर्णय में सहायता नहीं"
        ],
        "solution_title": "समाधान",
        "solutions": [
            "बहुभाषी मंडी भाव",
            "एआई आधारित विश्लेषण",
            "सरल बिक्री सलाह"
        ],
        "select_language": "🌐 भाषा चुनें",
        "select_state": "🏞 राज्य चुनें",
        "select_district": "📍 जिला चुनें",
        "enter_crop": "🌱 फसल का नाम दर्ज करें",
        "button": "मंडी जानकारी प्राप्त करें",
        "error": "कृपया फसल का नाम दर्ज करें",
        "trend_up": "भाव बढ़ रहे हैं 📈",
        "trend_down": "भाव घट रहे हैं 📉",
        "advice_sell": "बेचने का अच्छा समय",
        "advice_hold": "रुकना बेहतर है",
        "showing": "मंडी जानकारी दिखा रहे हैं"
    }
}

st.markdown("""
<style>
body { background-color: #f4f6f8; }
.hero { text-align:center; padding:30px; }
.hero h1 { color:#2a7f3e; font-size:44px; }
.hero p { font-size:18px; color:#555; }
.card {
    background:white;
    padding:20px;
    border-radius:14px;
    box-shadow:0 6px 16px rgba(0,0,0,0.1);
}
.metric {
    background:#eaf7ee;
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:18px;
}
.stButton>button {
    background:#2a7f3e;
    color:white;
    font-size:18px;
    padding:12px 30px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

language = st.selectbox("🌐 Select Language", ["English", "Hindi"])
T = LANG[language]

st.markdown(f"""
<div class="hero">
    <h1>{T["title"]}</h1>
    <p>{T["subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='card'><h3>{T['problem_title']}</h3><ul>" +
                "".join([f"<li>{p}</li>" for p in T["problems"]]) +
                "</ul></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card'><h3>{T['solution_title']}</h3><ul>" +
                "".join([f"<li>{s}</li>" for s in T["solutions"]]) +
                "</ul></div>", unsafe_allow_html=True)

state = st.selectbox(T["select_state"], ["Maharashtra", "Karnataka", "Telangana"])
district = st.selectbox(T["select_district"], ["Pune", "Nagpur", "Mumbai"])
crop = st.text_input(T["enter_crop"])

if st.button(T["button"]):
    if crop.strip() == "":
        st.error(T["error"])
    else:
        data = {
            "crop": crop,
            "avg_price": 2200,
            "min_price": 1800,
            "max_price": 2600,
            "trend": "up"
        }

        st.success(f"{T['showing']} {crop} – {district}, {state}")

        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='metric'>₹ {data['min_price']}<br>Min Price</div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='metric'>₹ {data['avg_price']}<br>Avg Price</div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='metric'>₹ {data['max_price']}<br>Max Price</div>", unsafe_allow_html=True)

        if data["trend"] == "up":
            st.info(T["trend_up"])
            st.success(T["advice_sell"])
        else:
            st.warning(T["trend_down"])
            st.warning(T["advice_hold"])
