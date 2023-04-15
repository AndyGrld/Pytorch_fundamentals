from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import streamlit as st

st.markdown('# Page 2')

st.sidebar.markdown("# Page 2")


# Load the diabetes dataset
diabetes = load_diabetes()

diabetes

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=0)

# Train a linear regression model on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Use the trained model to make predictions on the testing set
y_pred = regressor.predict(X_test)

# Compute the regression evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
st.write("Mean squared error (MSE): {:.2f}".format(mse))
st.write("Mean absolute error (MAE): {:.2f}".format(mae))
st.write("R-squared (R^2): {:.2f}".format(r2))

# Convert the regression problem into a binary classification problem
threshold = .5
y_pred_class = np.zeros_like(y_pred)
y_pred_class[y_pred >= threshold] = 1

# Calculate the accuracy of the classification model
accuracy = np.mean(y_pred_class == y_test)
st.write("Accuracy:", accuracy)