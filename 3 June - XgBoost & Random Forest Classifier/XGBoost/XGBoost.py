# XGBoost

# Importing the Libraries
import numpy as np
import pandas as pd


#Importing the DATASET
dataset = pd.read_csv(r"E:\Machine learninng\3 June - XgBoost\XGBoost\Churn_Modelling.csv")
X = dataset.iloc[:,3:-1].values
y= dataset.iloc[:,-1].values

print(X)
print(y)

#Encoding Categorical Data
#Label Encoding the "Gender" column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,2] = le.fit_transform(X[:,2])

print(X)

# One Hot Encoding the "Geography" column

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])], remainder= 'passthrough')

X = np.array(ct.fit_transform(X))


# Splitting the dataset into the Training set  & Test set
from sklearn.model_selection import train_test_split
X_train ,X_test , y_train ,y_test = train_test_split(X,y, test_size=0.2, random_state=0)

#Training XGBoost on the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train,y_train)

#Predicting the Test set results
y_pred = classifier.predict(X_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)


#Accuracy
from sklearn.metrics import accuracy_score
ac =accuracy_score(y_test, y_pred)
print(ac)


#Bias
bias = classifier.score(X_train , y_train)
print(bias)


#Variance
variance =classifier.score(X_test,y_test)
print(variance)