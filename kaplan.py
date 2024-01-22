import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Read Excel file with pandas dataframe
df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drops rows where the "Years survived" column has missing values
df = df.dropna(subset=["Years survived"])

# Prints the data types of each column in the DataFrame
print(df.dtypes)

# Prints the unique values in the "Years survived" column.
print(df["Years survived"].unique())

# Create 2 dataframes to compare the 2 groups
# Filter data for ∆ mPAP <= -5
df_high_delta_mpap = df[df['∆ mPAP'] <= -5]

# Filter data for ∆ mPAP > -5
df_low_delta_mpap = df[df['∆ mPAP'] > -5]

# Create Kaplan-Meier estimators for each group
kmf_high_delta_mpap = KaplanMeierFitter()
kmf_low_delta_mpap = KaplanMeierFitter()

# Fit estimators to the data for each group
kmf_high_delta_mpap.fit(durations=df_high_delta_mpap["Years survived"])
kmf_low_delta_mpap.fit(durations=df_low_delta_mpap["Years survived"])

# Highlight: Print the number of data points in each group
num_points_high_delta_mpap = len(df_high_delta_mpap)
num_points_low_delta_mpap = len(df_low_delta_mpap)
print("Number of data points in ∆ mPAP <= -5 group:", num_points_high_delta_mpap)
print("Number of data points in ∆ mPAP > -5 group:", num_points_low_delta_mpap)

# Plot the Kaplan-Meier curves for each group
kmf_high_delta_mpap.plot_survival_function(label=f'∆ mPAP <= -5 (n={num_points_high_delta_mpap})')
kmf_low_delta_mpap.plot_survival_function(label=f'∆ mPAP > -5 (n={num_points_low_delta_mpap})')

# Add labels and legend
plt.title("Kaplan-Meier Curve by ∆ mPAP")
plt.xlabel("Time (years)")
plt.ylabel("Cumulative Survival")
plt.legend()

# Show the plot
plt.show()