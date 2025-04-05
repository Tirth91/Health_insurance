import streamlit as st
from prediction_helper import predict

# Set page config and background color
st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #e6f7ff;
    }
    .main {
        background-color: #e6f7ff;
    }
    div.stButton > button {
        background-color: #1890ff;
        color: white;
        border-radius: 12px;
        font-size: 16px;
    }
    div.stNumberInput > div > input, div.stTextInput > div > input {
        border-radius: 8px;
    }
    div.stSelectbox > div {
        border-radius: 8px;
    }
    .prediction-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Name Input
st.title('🏥 Health Insurance Cost Predictor')
name = st.text_input("📝 Name", placeholder="Enter your full name")

# Categorical options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Layout with columns
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Input fields
with row1[0]:
    age = st.slider('🎂 Age', min_value=18, max_value=100, value=25)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧 Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.slider('💸 Income in Lakhs', min_value=0, max_value=200, value=5)

with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('📜 Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('👥 Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('🌎 Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
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

# Prediction button
if st.button('PREDICT'):
    if name.strip() == "":
        st.warning("⚠️ Please enter your name before predicting!")
    else:
        prediction = predict(input_dict)
        st.markdown(
            f"""
            <div class="prediction-box">
                ✅ {name}'s Health Insurance Prediction: ${prediction:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )
