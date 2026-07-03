import pandas as pd
import matplotlib.pyplot as plt

# Importing CSV File
dataset = pd.read_csv(r"E:\Machine learninng\26 May- Logistic Regression\logit classification.csv")

# Independent and Dependent Variables
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Splitting the Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVM Model
from sklearn.svm import SVC

classifier = SVC()
classifier.fit(X_train, y_train)

# Predicting the Test Set Results
y_pred = classifier.predict(X_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Accuracy
from sklearn.metrics import accuracy_score

ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Training Accuracy (Bias)
bias = classifier.score(X_train, y_train)
print("Training Accuracy (Bias):", bias)

# Testing Accuracy (Variance)
variance = classifier.score(X_test, y_test)
print("Testing Accuracy (Variance):", variance)


# This is to get the Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)



