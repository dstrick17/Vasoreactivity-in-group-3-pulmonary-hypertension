import pandas as pd
from lifelines import CoxPHFitter

# Load the dataset from the provided Excel file
file_path = "C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx"
df = pd.read_excel(file_path)

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Check for leading or trailing whitespace and remove it
df.columns = df.columns.str.strip()

# Adjust 'Age At Cath' to reflect a 10-year increase
df['Age At Cath (10-Year Increase)'] = df['Age At Cath'] / 10

# Adjust 'BNP level (pg/ml)' to reflect a 50 pg/ml increase
df['BNP level (50 pg/ml Increase)'] = df['BNP level (pg/ml)'] / 50


# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# One-hot encode the 'Sex' variable
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# One-hot encode the 'vasoreactive' variable 'vasoreactive_yes' will be the new column for patients who are vasoreactive
df = pd.get_dummies(df, columns=['Vasoreactive'], drop_first=True)


# Select the relevant columns for the initial analysis, including covariates
initial_vars = ['Time from start date to end date (days)', 'event_occurred', 'Age At Cath (10-Year Increase)', 'Sex_M', 
                'RAP', 'mPAP', 'PCWP', 'CO', 'CI', 'PVR', 
                'Post NO mPAP', 'Post NO PCWP', 'Post NO CO', 'Post NO CI', 'Post NO PVR', 
                '∆ mPAP', '∆ PCWP', '∆ CO', '∆ CI', '∆ PVR', 
                'BNP level (50 pg/ml Increase)', 'Vasoreactive_Yes']  # Add 'vasoreactive_yes' to the list

# Create a Cox Proportional Hazard model for the initial analysis
cph_initial = CoxPHFitter()

# Print the header for variable name
print("Univariate Analysis Summary:")

# Perform univariate analysis for each variable
for var in initial_vars[2:]:  # starting from the 3rd variable
    df_selected_univariate = df[['Time from start date to end date (days)', 'event_occurred', var]]
    cph_initial.fit(df_selected_univariate, duration_col="Time from start date to end date (days)", event_col="event_occurred")
    print(f"\n{var}:")
    print(cph_initial.summary)
