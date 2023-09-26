#Social network adds

#import lib
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#load the data
data = pd.read_csv("snasep2023.csv")
print(data)

#check and handle the null data
print(data.isnull().sum())

#feature and target
features = data[["Gender", "Age", "EstimatedSalary"]]
target = data["Purchased"]

#check and handle the cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)

#model
model = GaussianNB()
model.fit(x_train, y_train)

#classification report
cr = classification_report(y_test, model.predict(x_test))
print(cr)

#predict
age = float(input("Enter your age : "))
es = float(input("Enter the salary : "))
g = int(input("1 F  2 M : "))
if g == 1:
	d = [[age, es, 1, 0]]
else:
	d = [[age, es, 0, 1]]

pur = model.predict(d)

print("Purchased = ", pur)


#internal working