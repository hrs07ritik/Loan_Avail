import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Loan Approval Dashboard", layout="wide")
st.title("💰 Loan Approval Prediction Dashboard")
st.write("Enter applicant details below to predict loan approval status.")

# -----------------------------
# Applicant Name
# -----------------------------
name = st.text_input("Applicant Name", "")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Applicant Details")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
annual_income = st.sidebar.number_input("Annual Income (₹)", min_value=10000, value=500000, step=5000)
loan_amount = st.sidebar.number_input("Loan Amount (₹)", min_value=1000, value=200000, step=5000)
credit_score = st.sidebar.slider("Credit Score", 300, 850, 700)
num_dependents = st.sidebar.slider("Number of Dependents", 0, 10, 0)
existing_loans_count = st.sidebar.slider("Existing Loans Count", 0, 10, 0)
employment_status = st.sidebar.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])

# -----------------------------
# Feature Engineering
# -----------------------------
loan_income_ratio = loan_amount / annual_income

# -----------------------------
# Load Random Forest Model
# -----------------------------
try:
    rf_model = pickle.load(open("loan_modell.pkl", "rb"))
    st.sidebar.success("Model loaded successfully ✅")
except FileNotFoundError:
    st.sidebar.error("Model file 'loan_modell.pkl' not found! Please place it in the same folder.")

# -----------------------------
# Prepare user input (13 features)
# -----------------------------
if 'rf_model' in locals():
    user_input = np.array([[
        age,                                 # 1. age
        1 if gender == "Male" else 0,        # 2. gender_Male
        0 if gender == "Male" else 1,        # 3. gender_Female
        annual_income,                        # 4. annual_income
        loan_amount,                          # 5. loan_amount
        credit_score,                         # 6. credit_score
        num_dependents,                       # 7. num_dependents
        existing_loans_count,                 # 8. existing_loans_count
        1 if employment_status == "Salaried" else 0,       # 9. employment_Salaried
        1 if employment_status == "Self-employed" else 0, # 10. employment_Self-employed
        1 if employment_status == "Unemployed" else 0,    # 11. employment_Unemployed
        loan_income_ratio,                     # 12. loan_income_ratio
        0                                     # 13. placeholder/fill zero
    ]])

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Loan Approval"):

    if 'rf_model' in locals():
        prediction = rf_model.predict(user_input)[0]
        probability = rf_model.predict_proba(user_input)[0][1]

        # Two columns layout
        col1, col2 = st.columns(2)

        # Left column: Prediction + Name
        with col1:
            if name:
                st.subheader(f"Applicant: {name}")
            else:
                st.subheader("Applicant: [Not provided]")

            if prediction == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

            st.progress(int(probability * 100))
            st.info(f"Approval Probability: {probability*100:.2f}%")

        # Right column: Dashboard/Table + Graphs
        with col2:
            st.subheader("Applicant Overview")
            data = {
                "Feature": ["Age", "Annual Income", "Loan Amount", "Credit Score",
                            "Dependents", "Existing Loans", "Loan/Income Ratio"],
                "Value": [age, annual_income, loan_amount, credit_score,
                          num_dependents, existing_loans_count, round(loan_income_ratio, 2)]
            }
            df = pd.DataFrame(data)
            st.table(df)

            st.subheader("Employment & Gender")
            st.write(f"Gender: {gender}")
            st.write(f"Employment Status: {employment_status}")

            # Visual indicators in grid style
            st.subheader("Visual Indicators")

            chart_data1 = pd.DataFrame({
                "Amount": [annual_income, loan_amount]
            }, index=["Annual Income", "Loan Amount"])

            chart_data2 = pd.DataFrame({
                "Score": [credit_score]
            }, index=[f"Credit Score"])

            col3, col4 = st.columns(2)
            with col3:
                st.bar_chart(chart_data1, use_container_width=True)
                st.caption("💵 Annual Income vs Loan Amount")
            with col4:
                st.bar_chart(chart_data2, use_container_width=True)
                st.caption("💳 Credit Score")