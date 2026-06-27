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


# Lets implement stats to this model

dataset.mean()
dataset.median()
dataset.mode()
dataset.var()
dataset.std()



# COEFFICIENT OF VARIANCE (CV)
# for calculating cv we have to import a LIBRARY first

from scipy.stats import variation
variation(dataset.values) #this will give cv for entire Dataframe

variation(dataset['Salary']) #this will give us cv of that particular column


# CORELATION !
dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])  # This will give us correlation between these two attribute


#SKEWNESS 

dataset.skew() # This will give Skewness of entire DATAFRAME
dataset['Salary'].skew()


#STANDARD ERROR 
dataset.sem()
dataset['Salary'].sem()  #This will give standard error of that particular column


# Z- Score
#For calculating Z-Score we have to import a library first

import scipy.stats as stats

dataset.apply(stats.zscore)  #this will give z-score of entire DATAFRAME


# ANOVA

#SSR
y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean)**2)
print(SSR)

#SSE
y = y[0:6]
SSE =  np.sum((y-y_pred)**2)
print(SSE)

#SST
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values - mean_total)**2)
print(SST)

#r2
r_square = 1 - SSR / SST
print(r_square)


#BIAS SCORE
bias = regressor.score (x_train , y_train)
print(bias)

#VARIANCE SCORE
variance = regressor.score(x_test,y_test)
print(variance)
