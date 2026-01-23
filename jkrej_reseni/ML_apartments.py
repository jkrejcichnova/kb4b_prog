import csv

from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# intervals are by 200s, so 0-200 = 0, 200-400 = 1 and so on.
def num_to_interval(n) -> int:
    interval = 200
    i: int = 0 
    while n > interval:
        if i == 10:
            return i
        n -= interval
        i += 1
    return i

for i in range(0, 5000, 500):
    print(f"Apartment for a listed price of: {i} will be categorized as {num_to_interval(i)}")

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy
states = []

with open("./3. strojove_uceni/data/apartments_for_rent_filtered.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:

        raw_price = float(row["price"])
        price = num_to_interval(raw_price)

        bedrooms = float(row["bedrooms"])
        bathrooms = float(row["bathrooms"])
        sqft = float(row["square_feet"])

        raw_state = row["state"]
        if raw_state not in states:
            states.append(raw_state)
        state = states.index(raw_state)

        has_photo: int = 0
        match row["has_photo"]:
            case "Thumbnail":
                has_photo = 1
            case "Yes":
                has_photo = 2
        
        raw_pets: str = row["pets_allowed"]
        pets: float = 0
        if "Cats" in raw_pets:
            pets += 1
        if "Dogs" in raw_pets:
            pets += 1
        
        X.append([bathrooms, bedrooms, sqft, has_photo, pets, state])
        Y.append(price)


# ---------- Rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(128,64,32,16),
    activation="relu",
    max_iter=1000,
    verbose=True,
    random_state=None
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()