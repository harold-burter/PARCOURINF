from sklearn.ensemble import RandomForestClassifier
import random

def generate_prepa_dataset(n=200):
    data = []

    for _ in range(n):
        math = round(random.gauss(10, 10), 1)
        physique = round(random.gauss(10, 10), 1)
        moyenne = round((math + physique) / 2, 1)
        classement = random.randint(1, 40)

        if moyenne >= 16 and classement <= 5:
            avis = 3
            admis = 1
        elif moyenne >= 14:
            avis = 2
            admis = random.choice([0, 1])
        elif moyenne >= 12:
            avis = 1
            admis = random.choice([0, 0, 1])
        else:
            avis = 0
            admis = 0

        data.append({
            "math": math,
            "physique": physique,
            "moyenne": moyenne,
            "classement": classement,
            "avis": avis,
            "admis": admis
        })

    return data

prepa_data = generate_prepa_dataset(300)

X = [[d["math"], d["physique"], d["classement"], d["avis"]] for d in prepa_data]
Y = [d["admis"] for d in prepa_data]

model=RandomForestClassifier()
model.fit(X,Y)

def predict_prepa(maths,physique,classement,avis):
    proba=model.predict_proba([[maths,physique,classement,avis]])[0][1]
    proba*=100
    return round(float(proba))