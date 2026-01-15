import csv
import statistics
from sklearn.neural_network import MLPClassifier

X = []
Y = []

with open("./3. strojove_uceni/data/heart.csv", "r", encoding="UTF-8") as file:
    for line in csv.DictReader(file):
        Y.append(int(line["heart_disease"]))
        age: int = int(line["age"])
        sex: int = int(line["sex"])
        chest_pain: int = int(line["cp"])
        rest_heart_rate: int = int(line["trestbps"])
        cholesterol: int = int(line["chol"])
        max_heart_rate: int = int(line["thalach"])
        oldpeak: int = int(float(line["oldpeak"])*10)
        slope: int = int(line["slope"])
        X.append([age, sex, chest_pain, rest_heart_rate, max_heart_rate, cholesterol, oldpeak, slope])
X_train = X[:round(0.8*len(X))] 
Y_train = Y[:round(0.8*len(Y))]
X_test = X[round(0.8*len(X)):] 
Y_test = Y[round(0.8*len(Y)):]  

results = []
n = 50
layers = (40, 34, 22, 16, 12)
for i in range(n):
    ml = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        max_iter=3000,
        random_state=None
    )
    ml.fit(X_train, Y_train)
    prediction = ml.predict(X_test)
    correct = 0
    for j in range(len(prediction)):
        if prediction[j] == Y_test[j]:
            correct += 1
    result = round(correct/len(prediction)*100)
    results.append(result)
    print(f"Iteration {i}/{n} done ({result}%)")
out = f"LAYERS: {str(layers)}\n\nAverage result: {round(sum(results)/len(results), 3)}%\nMedian of results: {statistics.median(results)}%\nMode of results: {statistics.mode(results)}%\nBest result: {max(results)}%\nWorst result: {min(results)}%\nPopulation Variance: {round(statistics.pvariance(results), ndigits=3)}\n\n"
print(out)
with open("./jkrej_reseni/heart_prediction_results.txt", mode="a", encoding="UTF-8") as file:
    file.write(out)