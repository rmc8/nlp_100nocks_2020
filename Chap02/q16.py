import sys
import pandas as pd

_, n = sys.argv
N = int(n)
df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
div_num = - (-len(df) // N)
for num in range(N):
    cdf = df.loc[div_num * num: div_num * (num + 1)]
    cdf.to_csv(f"./q16_{num + 1}.txt", sep="\t", index=False, header=None)
