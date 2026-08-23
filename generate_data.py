import pandas as pd
import numpy as np

np.random.seed(42)

n = 2000

payment_methods = ["UPI", "Card", "Netbanking", "Wallet"]
failure_reasons = [
    "Insufficient Funds",
    "Bank Declined",
    "Network Error",
    "Timeout",
    "Authentication Failed"
]

data = pd.DataFrame({
    "transaction_id": [f"TXN{i:05d}" for i in range(1, n + 1)],
    "amount": np.random.randint(100, 50000, n),
    "payment_method": np.random.choice(payment_methods, n),
    "failure_reason": np.random.choice(failure_reasons, n),
    "customer_attempts": np.random.randint(1, 6, n),
    "hour": np.random.randint(0, 24, n)
})

# Create realistic recovery probability based on transaction factors
base_probability = np.random.uniform(0.2, 0.9, n)

# Network and timeout failures are generally more recoverable
data["recovery_probability"] = base_probability

data.loc[
    data["failure_reason"].isin(["Network Error", "Timeout"]),
    "recovery_probability"
] += 0.10

data.loc[
    data["failure_reason"] == "Insufficient Funds",
    "recovery_probability"
] -= 0.15

data["recovery_probability"] = data["recovery_probability"].clip(0.05, 0.98)

# Create target column
data["recovered"] = (
    np.random.rand(n) < data["recovery_probability"]
).astype(int)

# Save dataset
data.to_csv("payment_failures.csv", index=False)

print("Dataset created successfully!")
print(f"Total transactions: {len(data)}")
print(data.head())