# -*- coding: utf-8 -*-
"""ANN(Breast_Cancer).ipynb


pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
data = fetch_ucirepo(id=17)
x = data.data.features
y = data.data.targets

print(x)

print(y)

x.columns

y.columns

x.isnull().sum()

x.isna().any()

#label encodeing for dependant variable
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
y=le.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=0)

print(x_train)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

x_train

x_test

#Using Keras for ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

#input & first hidden layers:
classifier = Sequential()
classifier.add(Dense(units=16, activation='relu', input_dim=30))

#2nd input layers:
classifier.add(Dense(units=16, activation='relu'))

#output layers:
classifier.add(Dense(units=1, activation='sigmoid'))

classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
classifier.fit(x_train, y_train, epochs= 100, batch_size=50, validation_data=(x_test,y_test))

loss, accuracy = classifier.evaluate(x_test, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')

