import pandas as pd

df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
cnt = df.groupby(0).count()[1].sort_values(ascending=False)
print(cnt.sort_values(ascending=False))
