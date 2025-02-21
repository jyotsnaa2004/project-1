import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_customers = 1000
data = {
    'CustomerID': np.arange(1, n_customers + 1),
    'Age': np.random.randint(18, 70, size=n_customers),
    'Gender': np.random.choice(['Male', 'Female'], size=n_customers),
    'Tenure': np.random.randint(1, 72, size=n_customers),  # Months
    'MonthlyCharges': np.random.uniform(20, 100, size=n_customers).round(2),
    'TotalCharges': np.random.uniform(100, 5000, size=n_customers).round(2),
    'PaymentMethod': np.random.choice(['Credit Card', 'Bank Transfer', 'PayPal'], size=n_customers),
    'Churn': np.random.choice([0, 1], size=n_customers)  # 0 = No, 1 = Yes
}

# Convert to DataFrame
data = pd.DataFrame(data)

# Save to CSV
data.to_csv('customer_data.csv', index=False)

# Load the dataset
data = pd.read_csv('customer_data.csv')  # Use a relative path

# Display the first few rows
print(data.head())