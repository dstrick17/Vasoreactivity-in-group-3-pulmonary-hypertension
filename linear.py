import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset from the provided Excel file
file_path = "C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx"
df = pd.read_excel(file_path)

# Select the relevant columns for the analysis
X = df[['∆ mPAP']]
y = df['Years survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Print the coefficients of the linear regression model
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R-squared:", r2_score(y, model.predict(X)))

# Visualize the regression line
plt.scatter(X, y, color='black', label='Data Points')
plt.plot(X, model.predict(X), color='blue', linewidth=3, label='Regression Line')

plt.title('Linear Regression: ∆ mPAP vs Years survived')
plt.xlabel('∆ mPAP')
plt.ylabel('Years survived')
plt.legend()
plt.show()

