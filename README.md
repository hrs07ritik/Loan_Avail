

# 🏦 LoanDekho – Loan Approval Prediction App

LoanDekho is a Machine Learning-based web application that predicts whether a loan application is likely to be approved based on applicant details such as income, credit score, employment status, and more.

🌐 **Live App:**
👉 [https://loandekho.streamlit.app/](https://loandekho.streamlit.app/)

---

## 🚀 Project Overview

This project uses a **Random Forest Classifier** trained on loan-related data to predict loan approval outcomes.

The application provides an interactive web interface built with **Streamlit**, allowing users to enter their details and instantly receive a prediction along with approval probability.

---

## 🎯 Features

* User-friendly web interface
* Real-time loan approval prediction
* Probability score visualization
* Clean dashboard layout
* Deployed on Streamlit Cloud

---

## 🛠 Tech Stack

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**
* **Git & GitHub**

---

## 📊 Input Parameters

The model considers the following features:

* Age
* Gender
* Marital Status
* Annual Income
* Loan Amount
* Credit Score
* Number of Dependents
* Existing Loans Count
* Employment Status

---

## 🧠 Machine Learning Model

* Model Used: **Random Forest Classifier**
* Type: Supervised Classification
* Output:

  * 1 → Loan Approved
  * 0 → Loan Not Approved

The model predicts both:

* Loan approval status
* Probability of approval

---

## 📂 Project Structure

```
Loan_Avail/
│
├── main.py              # Streamlit application
├── loan_modell.pkl      # Trained ML model
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation (Run Locally)

1. Clone the repository:

```bash
git clone https://github.com/hrs07ritik/Loan_Avail.git
```

2. Navigate into the project folder:

```bash
cd Loan_Avail
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run main.py
```

---

## 📈 What I Learned

* Data preprocessing and feature encoding
* Handling categorical variables
* Training and evaluating ML models
* Model deployment using Streamlit
* Version control using Git & GitHub

---

## 👨‍💻 Author

**Ritik Raj**
Final Year – Computer Science & Engineering 
Aspiring Machine Learning Engineer

---

