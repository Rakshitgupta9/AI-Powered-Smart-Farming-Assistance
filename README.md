# AI-Powered-Smart-Farming-Assistance

# 🌾 AI-Powered Smart Farming Assistance Portal

## 🔍 Problem Statement

Small and marginal farmers face numerous agricultural challenges, including:

* Climate change impacts
* Soil degradation and poor fertility
* Limited access to real-time information and technology
* Outdated farming practices
* Difficulty in detecting plant diseases early
* Inability to access up-to-date market prices

These issues lead to low crop productivity, financial instability, and economic losses.

## ✅ Proposed Solution

Our AI-Powered Smart Farming Assistance Portal is a holistic, tech-enabled solution aimed at empowering farmers by leveraging Artificial Intelligence (AI) and Machine Learning (ML).

### 🌟 Key Features:

* **🌱 Crop Recommendations:** Personalized suggestions based on soil and environmental data
* **🧪 Soil Health Analysis:** Image-based analysis for moisture, fertility, and nutrient deficiency
* **🌿 Plant Disease Detection:** AI model diagnoses crop diseases from uploaded images
* **💰 Market Price Insights:** Real-time pricing data to help farmers make profitable decisions
* **🤖 AI Chatbot:** 24/7 assistance and guidance using GPT-4 and Rasa
* **🔐 Secure Authentication:** Ensures data privacy using bcrypt

## ⚙️ How It Works

1. **User Authentication:** Secure login and registration for farmers
2. **Crop Recommendation:** Suggests optimal crops using ML model
3. **Soil Analysis:** Farmers upload soil images for condition evaluation
4. **Disease Detection:** Upload images of crops to detect diseases and get remedies
5. **Market Insights:** Displays up-to-date crop prices
6. **AI Chatbot:** Provides conversational support and farming help

## 🛠️ Technology Stack

| Component        | Technology Used          |
| ---------------- | ------------------------ |
| Frontend         | HTML, CSS                |
| Backend          | Flask (Python)           |
| Database         | MongoDB                  |
| Image Processing | OpenCV                   |
| ML/AI Models     | TensorFlow, Scikit-learn |
| Chatbot          | GPT-4, Rasa              |
| Security         | bcrypt                   |

## 🌐 Folder Structure

```
Farming/
├── data/
│   └── Crop_recommendation.csv
├── instance/
│   └── users.db
├── static/
│   ├── css/
│   │   ├── index.css
│   │   └── style.css
│   └── images/
│       └── rakshit.jpg
├── templates/
│   ├── base.html
│   ├── chatbot.html
│   ├── help.html
│   ├── home.html
│   ├── index.html
│   ├── predict.html
│   ├── profile.html
│   └── signup.html
├── app.py
├── model_crop.pkl
├── model.py
└── notebooks/
    └── crop_prediction/
        ├── Agriculture.ipynb
        └── Crop_recommendation.csv
```

## 🎯 Alignment with UN SDG Goals

* **SDG 8 – Decent Work and Economic Growth:** Increases productivity and financial outcomes for farmers using AI insights.
* **SDG 9 – Industry, Innovation, and Infrastructure:** Promotes sustainable agriculture through cutting-edge technologies.
