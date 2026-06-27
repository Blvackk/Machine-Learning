import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"E:\Machine learninng\2 May - ML First Code\Data.csv")

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].to_numpy(dtype=object)


#SimpleImputer is a preprocessing tool in scikit-learn that is used to fill (impute) missing values (NaN) in a dataset.
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')

imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

# FIT & Transform --> FIT will fill the all empty values present in the data


#LabelEncoder --> LabelEncoder is a preprocessing tool in scikit-learn that converts categorical (text) values into numerical values.

from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()

x[:,0] = labelencoder_x.fit_transform(x[:,0])


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


from sklearn.model_selection import  train_test_split
x_train , x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,test_size=0.2 , random_state=0)
#random_state=0 is used to make your results reproducible. It ensures that every time you run your code, the "random" operations produce the same output.
#Agar random state =0 nai rega tho , har baar model ka training update hote rega jiss ke karan model ki accuracy me changes aate rhenege.

