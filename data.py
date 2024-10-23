import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
dataset = pandas.read_csv('iris.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train)
print(X_test)