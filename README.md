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

![Recovery Dashboard](screenshots/recovery_dashboard.png)

### 🎯 Priority Queue

![Priority Queue](screenshots/priority%20queue.png)

### 🤖 AI Recovery Agent

#### 🟢 Low Priority

![AI Recovery Agent Low](screenshots/AI%20Recovery%20agent%201(LOW).png)

#### 🟡 Medium Priority

![AI Recovery Agent Medium](screenshots/AI%20Recovery%20agent%202(MEDIUM).png)

#### 🔴 High Priority

![AI Recovery Agent High](screenshots/AI%20Recovery%20agent%203(HIGH).png)

### 📈 Recovery Analysis

![Expected Recovery Analysis](screenshots/expected%20recovery%20by%20payment%20method%20and%20recovery%20pro...png)

