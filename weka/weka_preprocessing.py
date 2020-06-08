import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading csv dataset
df = pd.read_csv('D:/learning/DM/weka/heart.csv')

df["sex"] = df["sex"].map({0: 'F', 1: 'M'})
df["cp"] = df["cp"].map({1: 'typical angina', 2: 'atypical angina',
                         3: 'non-anginal pain', 4: 'asymptomatic'})
# df["fbs"] = df["fbs"].map({0: 'N', 1: 'Y'})
df["restecg"] = df["restecg"].map(
    {0: 'normal', 1: 'STT wave abnormality', 2: 'left ventricular hypertrophy'})
# df["exang"] = df["exang"].map({0: 'N', 1: 'Y'})
df["slope"] = df["slope"].map({1: 'up', 2: 'flat', 3: 'down'})
df["ca"] = df["ca"].map({0: 'zero', 1: 'one', 2: 'two', 3: 'three'})
df["thal"] = df["thal"].map(
    {3: "normal", 6: "fixed defect", 7: "reversable defect"})
df['goal'] = df['goal'].map({0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'})

df.to_csv(path_or_buf="D:/learning/DM/weka/heart2.csv", index=False)
