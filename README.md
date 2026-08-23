# 💰 RecoverAI

## Autonomous AI Revenue Recovery Agent

RecoverAI is an AI-powered application designed to analyze failed payment transactions, predict the probability of revenue recovery, prioritize high-value recovery opportunities, and recommend the best action for recovering lost revenue.

## 🚀 Features

- 📊 Revenue Recovery Dashboard
- 🎯 High-Priority Payment Queue
- 🤖 AI-Powered Recovery Agent
- 📈 Recovery Probability Prediction
- 💰 Potential Recoverable Revenue Calculation
- 🔍 Failed Payment Analysis
- ⚡ Automated Recovery Recommendations

## 🧠 How It Works

The application analyzes failed payment transactions using features such as:

- Transaction Amount
- Payment Method
- Failure Reason
- Previous Customer Attempts
- Hour of Failure

A machine learning model predicts the probability that a failed transaction can be successfully recovered.

Based on the predicted recovery probability, RecoverAI categorizes transactions into priority levels:

- 🟢 **High Priority** – High probability of recovery and significant revenue opportunity
- 🟡 **Medium Priority** – Moderate probability of recovery
- 🔵 **Low Priority** – Low probability of recovery

The AI Recovery Agent then recommends an appropriate action, such as retrying the payment, sending a payment reminder, or monitoring the customer.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

## 📂 Project Structure

```text
RecoverAI/
│
├── app.py
├── generate_data.py
├── train_model.py
├── payment_failures.csv
├── recovery_model.pkl
├── requirements.txt
└── README.md
## 📸 Project Screenshots

### 📊 Recovery Dashboard

![Recovery Dashboard](screenshots/recovery%20dashboard.png)

### 🎯 Priority Queue

![Priority Queue](screenshots/priority%20queue.png)

### 🟢 Low Priority

![Low Priority](screenshots/LOW.png)

### 🟡 Medium Priority

![Medium Priority](screenshots/MEDIUM.png)

### 🔴 High Priority

![High Priority](screenshots/HIGH.png)