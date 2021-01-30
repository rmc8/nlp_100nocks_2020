import pandas as pd

df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
df.to_csv("./q11.txt", sep=" ", index=False, header=None)
