import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Simple Data: Square Feet (X) and Price (y)
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([200000, 300000, 400000, 500000, 600000])

# 2. Initialize and Train Model
model = LinearRegression()
model.fit(X, y)

# 3. Predict price for a 2200 sq ft house
new_house = np.array([[2200]])
prediction = model.predict(new_house)

print(f"Predicted price for 2200 sq ft: ${prediction[0]:,.2f}")

# 4. Visualize the "Line of Best Fit"
plt.scatter(X, y, color='blue') # Actual data
plt.plot(X, model.predict(X), color='red') # The model's logic
plt.title('House Price Prediction (Linear Regression)')
plt.show()