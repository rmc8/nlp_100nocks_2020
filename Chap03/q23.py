import re

import pandas as pd

df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
sec_list = re.findall(r"={2,}.*={2,}", text)
for sec_raw in sec_list:
    name = sec_raw.strip("=")
    level = (len(sec_raw) - len(name)) / 2 - 1
    print(f"{name} ({int(level)})")
