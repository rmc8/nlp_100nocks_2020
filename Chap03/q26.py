import re
import pprint
from collections import OrderedDict

import pandas as pd


def rm_emphasis_markups(text):
    return re.sub(
        r"(\'{2,5})(.*?)(\1)",
        r"\2",
        text,
        flags=re.MULTILINE + re.VERBOSE
    )


df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
basic = re.search(r"^\{\{基礎情報.*?\n(.*?)\}\}$", text, re.MULTILINE + re.VERBOSE + re.DOTALL)
templates = OrderedDict(
    re.findall(
        r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))",
        basic.group(1),
        re.MULTILINE + re.VERBOSE + re.DOTALL
    )
)
for key, val in templates.items():
    rm_markup_txt = rm_emphasis_markups(val)
    templates[key] = rm_markup_txt
    if val != rm_markup_txt:
        print(f"Key:{key}\tBefore:{val},\tAfter:{rm_markup_txt}")

pprint.pprint(templates)
