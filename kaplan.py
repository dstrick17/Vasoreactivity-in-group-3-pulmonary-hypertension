import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Read Excel file with pandas dataframe
df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# Create Kaplan-Meier estimator
kmf = KaplanMeierFitter()

# Fit estimator to the data
kmf.fit(durations=df["Time in months"], event_observed=df["event_occurred"])

# Plot the Kaplan-Meier curve
kmf.plot_survival_function(label=f'All Patients (n={len(df)})')

# Add labels and legend
plt.title("Kaplan-Meier Curve for All Patients")
plt.xlabel("Time (months)")
plt.ylabel("Survival Probability")
plt.legend()

# Show the plot
plt.show()
