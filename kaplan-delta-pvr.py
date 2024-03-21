import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# Read Excel file with pandas dataframe
df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drop rows with NaN values in relevant columns
df = df.dropna(subset=["Time from start date to end date (days)", "∆ PVR"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# Create two dataframes based on ∆ PVR values
df_low_delta_pvr = df[df['∆ PVR'] <= 1.2]
df_high_delta_pvr = df[df['∆ PVR'] > 1.2]

# Create Kaplan-Meier estimators for each group
kmf_low_delta_pvr = KaplanMeierFitter()
kmf_high_delta_pvr = KaplanMeierFitter()

# Fit estimators to the data for each group
kmf_low_delta_pvr.fit(durations=df_low_delta_pvr["Time in months"], event_observed=df_low_delta_pvr["event_occurred"], label='Reduction in PVR by ≤ 1.2 Wood units')
kmf_high_delta_pvr.fit(durations=df_high_delta_pvr["Time in months"], event_observed=df_high_delta_pvr["event_occurred"], label='Reduction in PVR by > 1.2 Wood units')

# Perform log-rank test
results = logrank_test(durations_A=df_low_delta_pvr["Time in months"],
                       event_observed_A=df_low_delta_pvr["event_occurred"],
                       durations_B=df_high_delta_pvr["Time in months"],
                       event_observed_B=df_high_delta_pvr["event_occurred"])

# Plot the Kaplan-Meier curves for each group
kmf_low_delta_pvr.plot_survival_function(label=f'Reduction in PVR by ≤ 1.2 Wood units (n={len(df_low_delta_pvr)})')
kmf_high_delta_pvr.plot_survival_function(label=f'Reduction in PVR by > 1.2 Wood units (n={len(df_high_delta_pvr)})')

# Add labels and legend
plt.title("Kaplan-Meier Curve by ∆ PVR (Wood Units)")
plt.xlabel("Time (months)")
plt.ylabel("Survival Probability")
plt.legend()

# Annotate the log-rank p-value on the plot
plt.text(60, 0.5, f'Log-rank p-value: {results.p_value:.4f}', ha='left', va='center', color='red', fontsize=12)

# Show the plot
plt.show()
