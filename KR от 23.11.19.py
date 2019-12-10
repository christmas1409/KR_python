import numpy as np
import pandas as pd

df = pd.read_csv('group.tsv', sep='\t')
x = df.to_numpy()
df["Рейтинг"] = np.zeros(len(df))
df["Рейтинг20"] = np.zeros(len(df))
stepper = 0
for i in range(0, len(x)-1, 1):
    for j in range(6, 18, 1):
        if x[i, j] == "+":
            stepper += 2
        elif x[i, j] == "-":
            stepper -= 1
        elif x[i, j] == "+-":
            stepper += 1
    y = x[i, 18].split(',')
    for z in y:
        if z == "+":
            stepper += 2.5
        elif z == "+-":
            stepper += 2
        elif z == "-+":
            stepper += 1
    df.loc[i, "Рейтинг"] = stepper
    if stepper >= 20:
        df.loc[i, "Рейтинг20"] = 20
    stepper = 0

df.to_csv('group_result.tsv', decimal=',', sep='\t')
