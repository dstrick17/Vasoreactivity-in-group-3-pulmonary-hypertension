import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# Read Excel file with pandas dataframe
df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# Create two dataframes based on ∆ mPAP (mm Hg) values
df_small_change_mPAP = df[df['∆ mPAP (mm Hg)'] >= -5]
df_big_change_mPAP = df[df['∆ mPAP (mm Hg)'] < -5]

# Create Kaplan-Meier estimators for each group
kmf_small_change_mPAP = KaplanMeierFitter()
kmf_big_change_mPAP = KaplanMeierFitter()

# Fit estimators to the data for each group
kmf_small_change_mPAP.fit(durations=df_small_change_mPAP["Time in months"], event_observed=df_small_change_mPAP["event_occurred"])
kmf_big_change_mPAP.fit(durations=df_big_change_mPAP["Time in months"], event_observed=df_big_change_mPAP["event_occurred"])

# Perform log-rank test
results = logrank_test(durations_A=df_small_change_mPAP["Time in months"],
                       event_observed_A=df_small_change_mPAP["event_occurred"],
                       durations_B=df_big_change_mPAP["Time in months"],
                       event_observed_B=df_big_change_mPAP["event_occurred"])

# Plot the Kaplan-Meier curves for each group
kmf_small_change_mPAP.plot_survival_function(label=f'drop in mPAP by 5 mm Hg or less (n={len(df_small_change_mPAP)})')
kmf_big_change_mPAP.plot_survival_function(label=f'drop mPAP by more than 5 mm Hg (n={len(df_big_change_mPAP)})')

# Add labels and legend
plt.title("Kaplan-Meier Curve by ∆ mPAP (mm Hg)")
plt.xlabel("Time (months)")
plt.ylabel("Survival Probability")
plt.legend()

# Annotate the log-rank p-value on the plot
plt.text(60, 0.5, f'Log-rank p-value: {results.p_value:.4f}', ha='left', va='center', color='red', fontsize=12)

# Show the plot
plt.show()


