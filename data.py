import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Data.csv')
print("\n*dataset*\n")
print(dataset)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print("\n*x*\n")
print(x)
print("\n*y*\n")
print(y)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print("\n*x after handeling missing data*\n")
print(x)

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough') #One-hot encoding transforms categorical data into a binary matrix where each category gets its own column
x = np.array(ct.fit_transform(x)) #remainder='passthrough': This tells the ColumnTransformer to leave the remaining columns unchanged (without any transformation).
print("\n*x after transformation*\n")
print(x)

le = LabelEncoder() #This is useful for categorical target variables, where the labels are strings, and you want to convert them into integers
y = le.fit_transform(y)
print("\n*y after transformation*\n")
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
print("\n*x_train*\n")
print(x_train)
print("\n*x_test*\n")
print(x_test)
print("\n*y_train*\n")
print(y_train)
print("\n*y_test*\n")
print(y_test)

sc = StandardScaler()
x_train[:,3:] = sc.fit_transform(x_train[:,3:])
x_test[:,3:] = sc.transform(x_test[:,3:])
print("\n*x_train after scaling*\n")
print(x_train)
print("\n*x_test after scaling*\n")
print(x_test)