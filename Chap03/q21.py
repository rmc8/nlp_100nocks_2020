import pandas as pd

df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
lines = text.splitlines()
cat_lines = [ln for ln in lines if "Category:" in ln]
print(cat_lines)
