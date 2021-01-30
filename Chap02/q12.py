import pandas as pd

df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
for num in range(2):
    df[num].to_csv(f"./col{num+1}.txt", index=False, header=None)
