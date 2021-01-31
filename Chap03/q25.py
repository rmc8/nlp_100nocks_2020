import re
import pprint
from collections import OrderedDict

import pandas as pd

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

pprint.pprint(templates)
