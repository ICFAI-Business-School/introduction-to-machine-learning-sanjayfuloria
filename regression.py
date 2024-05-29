import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your dataset
# For example purposes, we will generate a simple dataset
data = pd.DataFrame({
    'feature1': range(100),
    'feature2': range(100, 200),
    'target': range(200, 300)
})

# Split the dataset into features and target variable
X = data[['feature1', 'feature2']]
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the testing set
Enter your code here
print(f'The Predicted Value:{y_pred}')

# Evaluate the model
Enter your code here
print(f'Mean Squared Error: {mse}')
