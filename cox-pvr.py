import pandas as pd
from lifelines import CoxPHFitter

# Load the dataset from the provided Excel file
file_path = "C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx"
df = pd.read_excel(file_path)

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# Count the number of censored events
num_censored = df[df['event_occurred'] == 0].shape[0]
print(f'Number of censored events: {num_censored}')

# One-hot encode the 'Sex' variable
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# Select the relevant columns for the initial analysis, including covariates
initial_vars = ['Time in months', 'event_occurred', 'Age At Cath', 'Sex_M',
                'PVR','∆ PVR (WU)']
# 'PVR',

df_selected_initial = df[initial_vars]

# Create a Cox Proportional Hazard model for the initial analysis
cph_initial = CoxPHFitter()
cph_initial.fit(df_selected_initial, duration_col="Time in months", event_col="event_occurred")

# Print the summary of the initial analysis
print("Initial Analysis Summary:")
print(cph_initial.summary)

# Variable selection based on univariate analysis
selected_vars = ['Age At Cath', 'Sex_M']

# Loop over the variables for variable selection
for var in initial_vars[4:]:  # starting from the 5th variable
    # Check the p-value of the variable
    p_value = cph_initial.summary.loc[var, 'p']
    # If the p-value is less than 0.2, add the variable to the selected_vars list
    if p_value < 0.2:
        selected_vars.append(var)

# Refit the model using the selected variables
cph_selected = CoxPHFitter()
df_selected_final = df[['Time in months', 'event_occurred'] + selected_vars]
cph_selected.fit(df_selected_final, duration_col='Time in months', event_col='event_occurred')

# Print the summary of the final model after variable selection
print("Final Model Summary:")
print(cph_selected.summary)
