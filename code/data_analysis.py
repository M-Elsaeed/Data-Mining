# Dataset: https://archive.ics.uci.edu/ml/datasets/heart+Disease

# age: age in years
# sex: sex (1 = male; 0 = female)
# cp: chest pain type
# -- Value 1: typical angina
# -- Value 2: atypical angina
# -- Value 3: non-anginal pain
# -- Value 4: asymptomatic
# trestbps: resting blood pressure (in mm Hg on admission to the hospital)
# chol: serum cholestoral in mg/dl
# fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)
# restecg: resting electrocardiographic results
# -- Value 0: normal
# -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST
#             elevation or depression of > 0.05 mV)
# -- Value 2: showing probable or definite left ventricular hypertrophy
#             by Estes' criteria
# thalach: maximum heart rate achieved
# exang: exercise induced angina (1 = yes; 0 = no)
# oldpeak: ST depression induced by exercise relative to rest
# slope: the slope of the peak exercise ST segment
# -- Value 1: upsloping
# -- Value 2: flat
# -- Value 3: downsloping
# ca: number of major vessels (0-3) colored by flourosopy
# thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
# goal : diagnosis of heart disease (angiographic disease status)
# -- Value 0: < 50% diameter narrowing
# -- Value 1: > 50% diameter narrowing
# (in any major vessel)


# age           int
# sex           bool
# cp            "category"
# trestbps      int
# chol          int
# fbs           bool
# restecg       "category"
# thalach       int
# exang         bool
# oldpeak       float
# slope         int
# ca            "category"
# thal          "category"
# goal          "category"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Reading csv dataset
heartDataFrame = pd.read_csv('D:/learning/DM/code/heart.csv')

# Setting datatypes
heartDataFrame = heartDataFrame.astype({

    "age":           int,
    "sex":           bool,
    "cp":            "category",
    "trestbps":      int,
    "chol":          int,
    "fbs":           bool,
    "restecg":       "category",
    "thalach":       int,
    "exang":         bool,
    "oldpeak":       float,
    "slope":         int,
    "ca":            "category",
    "thal":          "category",
    "goal":          "category"

})

print(heartDataFrame)

# Removing Outliers and saving box plotes
for i in heartDataFrame:
    if heartDataFrame.dtypes[i] == "int32" or heartDataFrame.dtypes[i] == "float64":
        heartDataFrame.boxplot(column=i)
        plt.savefig("./code/images/before_" + i)
        plt.close()
        heartDataFrame = heartDataFrame[np.abs(heartDataFrame[i]-heartDataFrame[i].mean()) <= (3*heartDataFrame[i].std())]

print(heartDataFrame)

# Saving box plotes after removing Outliers
for i in heartDataFrame:
    if heartDataFrame.dtypes[i] == "int32" or heartDataFrame.dtypes[i] == "float64":
        heartDataFrame.boxplot(column=i)
        plt.savefig("./code/images/after_" + i)
        plt.close()

print("mode(s)")
print(heartDataFrame.mode())
print("Standard Deviation")
print(heartDataFrame.std(ddof=0, numeric_only=True))
print("Variance")
print(heartDataFrame.var(ddof=0, numeric_only=True))
print("Skewness")
print(heartDataFrame.skew())


for i in heartDataFrame:
    print(heartDataFrame[i].describe())
    if i == "sex" or i == "cp" or i == "fbs" or i == "restecg" or i == "exang"  or i == "slope" or i == "ca" or i == "thal" or i == "goal":
        heartDataFrame[i].value_counts().plot(kind='bar')
    else:
        pd.DataFrame.hist(heartDataFrame, column=i)
    plt.savefig("./code/images/bar_" + i)
    plt.close()
    print()
