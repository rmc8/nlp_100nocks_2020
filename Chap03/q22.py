import re

import pandas as pd

df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
cat_list = re.findall(r"^\[\[Category:(.*?)(?:\|.*)?\]\]$", text, re.MULTILINE)
print(cat_list)
