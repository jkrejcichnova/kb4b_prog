import csv
from sklearn.neural_network import MLPClassifier
X = []
Y = []

with open("./3. strojove_uceni/data/bmi.csv", "r", encoding="UTF-8") as file:
    for line in csv.DictReader(file):
        Y.append(int(line["Index"]))
        gender = int(line["Gender"] == "Male")
        height: float = int(line["Height"])/100
        weight: float = int(line["Weight"])/10
        X.append([gender,height,weight])
   
X_train = X[:round(0.8*len(X))] 
Y_train = Y[:round(0.8*len(Y))]
X_test = X[round(0.8*len(X)):] 
Y_test = Y[round(0.8*len(Y)):]      
ml = MLPClassifier(
    hidden_layer_sizes=(3,2),
    activation="relu",
    max_iter=10000
)
ml.fit(X_train, Y_train)
prediction = ml.predict(X_test)

correct = 0
for i in range(len(prediction)):
    if prediction[i] == Y_test[i]:
        correct += 1
print(f"Spravne: {round(correct/len(prediction)*100)}%")