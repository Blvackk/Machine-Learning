import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load Dataset
dataset = pd.read_csv(r"E:\Machine learninng\4 May - Simple Linear Regression\Salary_Data.csv")

# x--> INDEPENDENT VARIABLE
# y--> DEPENDENT VARIABLE

x = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 


y_pred = regressor.predict(x_test)
print(y_pred)

# BUILDING COMPARSION TABLE
comparision = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})
print(comparision)

plt.scatter(x_test, y_test, color = 'Red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary of employee based on experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()


# validataion or future data 

model_coef = regressor.coef_
print(model_coef)

model_const = regressor.intercept_
print(model_const)

y_12 = model_coef * 12 + model_const
print(y_12)

