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







# SVR Model

from sklearn.svm import SVR
svr_reg = SVR()
svr_reg.fit(X,y)

#Testcase 1
svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)


#Testcase 2
from sklearn.svm import SVR
svr_reg = SVR(kernel='sigmoid',degree=4,C=10.0,gamma='auto')
svr_reg.fit(X,y)

svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)


# Testcase 3
from sklearn.svm import SVR
svr_reg = SVR(kernel='poly',degree=4,C=10.0)
svr_reg.fit(X,y)

svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)


#Testcase 4
from sklearn.svm import SVR
svr_reg = SVR(kernel='poly',degree=4,C=10.0,gamma='auto')
svr_reg.fit(X,y)

svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)



# KNN MODEL


#Testcase 1
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor()
knn_reg.fit(X,y)


knn_reg_pred = knn_reg.predict([[6.5]])
print(knn_reg_pred)



#Testcase 2
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(weights='distance')
knn_reg.fit(X,y)


knn_reg_pred = knn_reg.predict([[6.5]])
print(knn_reg_pred)



#Testcase 3
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(p = 1,n_neighbors=3)
knn_reg.fit(X,y)


knn_reg_pred = knn_reg.predict([[6.5]])
print(knn_reg_pred)




#Testcase 4
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(p = 1, weights='distance')
knn_reg.fit(X,y)


knn_reg_pred = knn_reg.predict([[6.5]])
print(knn_reg_pred)




#DECISION TREE


#Testcase 1
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X,y)

dt_reg_pred = dt_reg.predict([[6.5]])
print(dt_reg_pred)



#Testcase 2
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion='poisson',max_depth=5,min_samples_split=3)
dt_reg.fit(X,y)

dt_reg_pred = dt_reg.predict([[6.5]])
print(dt_reg_pred)



# Random Forest

#Testcase 1 
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor()
rf_reg.fit(X,y)

rf_reg_pred = rf_reg.predict([[6.5]])
print(rf_reg_pred)


# xgboost

from xgboost import XGBRFRegressor
xb_reg = XGBRFRegressor
xb_reg.fit(X,y)

xgb_reg_pred = XGBRFRegressor([[6.5]])
print(xgb_reg_pred)



