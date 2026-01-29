import csv
import statistics
from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# intervals are by 20k
def num_to_interval(n, interval=20000, max=10) -> int:
    i: int = 0 
    while n > interval:
        if i == max:
            return i
        n -= interval
        i += 1
    return i
# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy
states = []

with open("./3. strojove_uceni/data/crime_socioeconomic_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        gdp = float(row["GDP per Capita (INR)"])/1000
        literacy = float(row["Literacy Rate (%)"])
        poverty = float(row["Poverty Rate (%)"])
        unemployment = float(row["Unemployment Rate (%)"])

        violent_c = float(row["Violent Crimes"])
        property_c = float(row["Property Crimes"])
        cyber_c = float(row["Cyber Crimes"])
        total_c = float(row["Total Crimes Reported"])
        crime = float(row["Crime Rate per 100000"])

        year = int(row["Year"])
        population = float(row["Population"])
        high_crime = bool(crime < 650)
        #high_crime = num_to_interval(crime, 500, 3)
        X.append([gdp, poverty])
        #X.append([crime])
        Y.append(high_crime)


# ---------- Rozdělení na trénování a testování ----------
rows = len(X)
trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)
layers = (64, 48, 32, 24, 16)
accuracies = []
n = 1
for j in range(n):
    neural_network = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        max_iter=1000,
        random_state=None
    )
    neural_network.fit(trening_X, trening_Y)
    results = neural_network.predict(test_X)
    correct = 0
    for i in range(len(results)):
        if test_Y[i] == results[i]:
            correct += 1
    accuracy = round((correct / len(results))*100, 3)
    accuracies.append(accuracy)
    print(f"\n\n\n\n\n\n\nIteration {j}/{n} done ({accuracy}%)")
    if accuracy > 55:
        ConfusionMatrixDisplay.from_predictions(test_Y, results)
        plt.show()
out = f"LAYERS: {str(layers)}\n\nAverage result: {round(sum(accuracies)/len(accuracies), 3)}%\nMedian of results: {statistics.median(accuracies)}%\nMode of results: {statistics.mode(accuracies)}%\nBest result: {max(accuracies)}%\nWorst result: {min(accuracies)}%\nPopulation Variance: {round(statistics.pvariance(accuracies), ndigits=3)}\n\n"
print(out)
with open("./jkrej_reseni/crime_prediction_results.txt", mode="a", encoding="UTF-8") as file:
    file.write(out)