import streamlit as st
from prediction_helper import predict

# Set page config for a bright and fun UI
st.set_page_config(page_title="🎉 Health Insurance Predictor", layout="wide")

# Custom CSS for colorful styling
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
        }

        /* Title */
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #4A148C;
            margin-bottom: 20px;
        }

        /* Section headings */
        .subheading {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #D81B60;
            margin-top: 10px;
        }

        /* Container styling */
        .stContainer {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.2);
        }

        /* Sliders */
        .stSlider {
            color: #7B1FA2;
        }

        /* Select and input field styling */
        .stTextInput, .stNumberInput, .stSelectbox {
            background: #F3E5F5 !important;
            color: black !important;
            border-radius: 10px;
            border: 2px solid #D81B60;
        }

        /* Button Styling */
        .stButton>button {
            background: linear-gradient(45deg, #FF4081, #7B1FA2) !important;
            color: white !important;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            width: 100%;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #7B1FA2, #FF4081) !important;
        }

        /* Prediction Box */
        .prediction-box {
            background: linear-gradient(45deg, #4CAF50, #2E7D32);
            color: white;
            padding: 12px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title
st.markdown('<p class="title">🎉 Health Insurance Predictor</p>', unsafe_allow_html=True)

# Define dropdown categories
categorical_options = {
    'Gender': ['👨 Male', '👩 Female'],
    'Marital Status': ['💍 Married', '💔 Unmarried'],
    'BMI Category': ['✅ Normal', '⚠️ Obesity', '⚖️ Overweight', '🔹 Underweight'],
    'Smoking Status': ['🚭 No Smoking', '🔥 Regular', '⚠️ Occasional'],
    'Employment Status': ['💼 Salaried', '🚀 Self-Employed', '💻 Freelancer'],
    'Region': ['🌍 Northwest', '🏝️ Southeast', '🗺️ Northeast', '🏔️ Southwest'],
    'Medical History': [
        '🟢 No Disease', '🩸 Diabetes', '⚠️ High Blood Pressure', '🩸 Diabetes & High BP',
        '🦋 Thyroid', '❤️ Heart Disease', '⚠️ BP & Heart Disease', '🩸 Diabetes & Thyroid',
        '🩸 Diabetes & Heart Disease'
    ],
    'Insurance Plan': ['🥉 Bronze', '🥈 Silver', '🥇 Gold']
}

# 📊 Dashboard Container
with st.container():
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    # 📋 User Details Heading
    st.markdown('<p class="subheading">📋 Enter Your Details</p>', unsafe_allow_html=True)

    # 🎚️ Sliders for age & income
    age = st.slider('🎂 Age', min_value=18, max_value=100, value=25)
    income_lakhs = st.slider('💰 Income in Lakhs', min_value=0, max_value=200, value=10)

    # 🏷️ Arrange Inputs in Three-Column Layout
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('⚧️ Gender', categorical_options['Gender'])
        smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
        bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])
        employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

    with col2:
        number_of_dependants = st.number_input('👨‍👩‍👦 Number of Dependants', min_value=0, step=1, max_value=20)
        marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
        region = st.selectbox('🌎 Region', categorical_options['Region'])
        genetical_risk = st.slider('🧬 Genetical Risk', min_value=0, max_value=5, value=2)

    with col3:
        insurance_plan = st.selectbox('📜 Insurance Plan', categorical_options['Insurance Plan'])
        medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

    # Close Container Styling
    st.markdown('</div>', unsafe_allow_html=True)

# 📊 Collect user inputs in a dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# 🔮 Prediction Section
st.markdown('<p class="subheading">🔮 Prediction</p>', unsafe_allow_html=True)

# Prediction Button
if st.button('🎯 Predict Insurance Cost'):
    prediction = predict(input_dict)
    st.markdown(f'<p class="prediction-box">💰 Predicted Health Insurance Cost: {prediction} INR</p>', unsafe_allow_html=True)