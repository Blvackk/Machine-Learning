import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"E:\Machine learninng\14 May - Polynomial Regression\emp_sal.csv")


X = dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values

# Linear Regression Model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

plt.scatter(X,y, color ='red')
plt.plot(X, lin_reg.predict(X),color='blue')
plt.title('Linear Regression Graph')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Prediction
lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)


# Polynomial Regression Model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(X)


poly_reg.fit(X_poly,y)

lin_reg_2 =LinearRegression()
lin_reg_2.fit(X_poly,y)

plt.scatter(X,y,color ='red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)))
plt.title("Truth or Bluff (Ploynomioal Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred



















