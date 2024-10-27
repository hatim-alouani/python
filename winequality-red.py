import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pandas.read_csv('winequality-red.csv', sep=";")
print("dataset")
print(dataset)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print("x")
print(x)
print("y")
print(y)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print("x_train")
print(x_train)
print("x_test")
print(x_test)
print("y_train")
print(y_train)
print("y_test")
print(y_test)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print("x_train after transf")
print(x_train)
print("x_t after transf")
print(x_test)
print("y_train after transf")
print(y_train)
print("y_t after transf")
print(y_test)