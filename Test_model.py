import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.tree import DecisionTreeClassifier
dataset = pd.read_csv('Combined_Moods.csv')
X = dataset.iloc[:,2:]
Y = dataset.iloc[:,0]
Y = pd.get_dummies(Y)
X = X.values
Y = Y.values
X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
classifier = DecisionTreeClassifier()
classifier.fit(X_train,Y_train)
y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test,y_pred))
filename = 'Finalized_Model.sav'
pickle.dump(classifier, open(filename,'wb'))







