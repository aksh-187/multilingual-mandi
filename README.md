# 🌾 Multilingual Mandi AI

An AI-powered multilingual mandi information system built using **Streamlit** to help Indian farmers and traders access crop market information in their preferred language.

## 🚀 Features

* 🌐 **Multilingual Support**

  * English
  * Hindi (हिन्दी)
  * Telugu (తెలుగు)

* 🏞 **State Selection**

  * Maharashtra
  * Karnataka
  * Telangana

* 📍 **District Selection**

  * Dynamically updates based on selected state

* 🌱 **Crop Search**

  * Enter any crop name to view mandi-related information

* 📊 **Price Dashboard**

  * Minimum Price
  * Average Price
  * Maximum Price

* 📈 **Market Trend Insights**

  * Price trend indication
  * Basic selling recommendation

* 🎨 **Clean Streamlit UI**

  * Simple and farmer-friendly interface
  * Responsive layout using Streamlit columns

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Requests**
* **Pillow**
* **Altair**

---

## 📂 Project Structure

```text
Multilingual-Mandi-AI/
│
├── app.py                 # Main Streamlit application
├── data.csv               # Crop/market data source
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
└── assets/                # Optional images/icons
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multilingual-Mandi-AI.git
cd Multilingual-Mandi-AI
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser at:

```text
http://localhost:8501
```

---

## 📋 Requirements

```text
streamlit==1.30.0
pandas
numpy
requests
Pillow
altair
```

---

## 💡 How It Works

1. Select your preferred language.
2. Choose a state.
3. Select a district.
4. Enter the crop name.
5. Click **Get Mandi Info**.
6. View:

   * Minimum Price
   * Average Price
   * Maximum Price
   * Market Trend
   * Selling Recommendation

---

## 🔮 Future Enhancements

* Real-time mandi prices using government APIs
* Support for additional Indian languages
* Price prediction using Machine Learning
* Voice-based crop search
* Weather integration
* Historical price analytics and charts
* Farmer-specific recommendations

---

## 🎯 Use Cases

* Farmers checking crop prices before selling
* Traders monitoring mandi trends
* Agricultural market awareness
* Regional language accessibility for rural users

---

## 👨‍💻 Contributors

Developed as a multilingual agricultural market information platform to improve accessibility and decision-making for Indian farmers and traders.

---

## 📄 License

This project is licensed under the MIT License.

```text
MIT License © 2026
```
