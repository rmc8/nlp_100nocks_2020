import re

import pandas as pd

df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
print(*re.findall(r"(?:File|ファイル):(.+?)\|", text, re.MULTILINE), sep="\n")
