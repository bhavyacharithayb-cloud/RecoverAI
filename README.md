# RecoverAI – AI Revenue Recovery Agent

## Project Overview

RecoverAI is an AI-powered failed payment recovery system. It analyzes failed transactions and predicts the probability that a payment can be successfully recovered.

The system helps businesses identify high-value recovery opportunities and prioritize failed payments based on their recovery potential.

## Features

- Analyze failed payment transactions
- Predict recovery probability using Machine Learning
- Identify high-value recovery opportunities
- Calculate potential recoverable revenue
- Recommend recovery actions
- Priority-based transaction queue
- Interactive Streamlit dashboard
- AI Recovery Agent for payment analysis

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Project Structure

recoverai/

- app.py – Streamlit dashboard and AI recovery interface
- generate_data.py – Generates synthetic failed payment data
- train_model.py – Trains the machine learning model
- payment_failures.csv – Generated transaction dataset
- recovery_model.pkl – Trained machine learning model
- requirements.txt – Required Python libraries
- README.md – Project documentation

## How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
### 2. Train the Machine Learning Model

```bash
python train_model.py
```

This will train the recovery prediction model and generate the trained model file.

### 3. Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal to access the RecoverAI dashboard.

## How It Works

1. Failed payment transaction data is generated using a synthetic dataset.
2. The machine learning model analyzes factors such as:
   - Transaction amount
   - Payment method
   - Failure reason
   - Previous customer attempts
   - Hour of failure
3. The model predicts the probability that a failed payment can be recovered.
4. RecoverAI calculates the potential recoverable revenue.
5. Transactions are prioritized into:
   - High Priority
   - Medium Priority
   - Low Priority
6. The AI Recovery Agent recommends an appropriate recovery action.

## Recovery Actions

Examples of recommended actions include:

- Retry payment automatically after a short interval
- Send an instant payment reminder with a secure payment link
- Monitor the customer and avoid excessive retries
- Prioritize high-value transactions with high recovery probability

## Dashboard Features

### Recovery Dashboard

Provides an overview of:

- Total failed transactions
- Total revenue at risk
- Expected recovery amount
- Number of high-priority recovery cases
- Revenue distribution by failure reason
- Expected recovery by payment method
- Recovery probability distribution
- Recovery priority distribution

### Priority Queue

Displays high-value recovery opportunities ranked based on predicted recovery probability and expected recovery value.

### AI Recovery Agent

Allows users to manually enter details of a failed transaction and receive:

- Predicted recovery probability
- Potential recoverable revenue
- Recommended recovery action
- Priority level for the transaction

## Project Objective

The objective of RecoverAI is to demonstrate how machine learning and intelligent decision logic can help payment platforms identify failed transactions with high recovery potential and recommend targeted actions to recover lost revenue.

## Future Improvements

- Integration with real payment gateway transaction data
- Real-time recovery predictions
- Automated payment reminders
- Customer behavior analysis
- Advanced machine learning models
- Integration with payment APIs for automated retry workflows

## Author

Bhavya Charitha

B.Tech Student | Artificial Intelligence and Data Science