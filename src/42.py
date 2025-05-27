import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = {
    'age': [18, 20, 22, 24, 26],
    'income': [50000, 55000, 57000, 60000, 63000],
    'education': ['Bachelor', 'Master', 'PhD', 'Doctorate', 'Masters']
}
df = pd.DataFrame(data)

X = df[['age', 'income']]
y = df['income']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict the income for the testing set
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean squared error: {mse}')
