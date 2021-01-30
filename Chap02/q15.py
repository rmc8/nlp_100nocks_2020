import sys

import pandas as pd

_, n = sys.argv
df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
print(df.tail(int(n)))
