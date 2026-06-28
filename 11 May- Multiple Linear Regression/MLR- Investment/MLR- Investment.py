import numpy as np
import matplotlib.pyplot as plt
import pandas as  pd

dataset =  pd.read_csv(r"E:\Machine learninng\11 May- Multiple Linear Regression\Investment.csv")

X = dataset.iloc[:, :-1]
y = dataset.iloc[:,4]

X = pd.get_dummies(X, dtype = int)

from sklearn.model_selection import train_test_split
X_train , X_test , y_train ,y_test = train_test_split(X,y, test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


y_pred = regressor.predict(X_test)

print(regressor.coef_)
print(regressor.intercept_)

X = np.append(arr=np.full((50,1), 42467).astype(int), values=X, axis=1)

# Till now we build ML multiplle Linear Regression
# We need to find out best attribute to grow bussiness

import statsmodels.api as sm
X_opt = X[:,[0,1,2,3,4,5]]

#OrdinaryLeastSquares
regressor_OLS = sm.OLS(endog=y ,exog=X_opt).fit()
regressor_OLS.summary()









