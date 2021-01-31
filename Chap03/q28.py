import re
import pprint
from collections import OrderedDict

import pandas as pd


def rm_emphasis_markups(txt):
    return re.sub(
        r"(\'{2,5})(.*?)(\1)",
        r"\2",
        txt,
        flags=re.MULTILINE + re.VERBOSE
    )


def rm_internal_links(txt):
    return re.sub(
        r"\[\[(?:[^|]*?\|)*?((?!Category:)([^|]*?))\]\]",
        r"\1",
        txt,
        flags=re.MULTILINE + re.VERBOSE
    )


def rm_external_links(txt):
    return re.sub(
        r"\[https?://(?:[^\s]*?/s)?([^]]*?)\]",
        r"\1",
        txt,
        flags=re.MULTILINE + re.VERBOSE
    )


def rm_lang_labels(txt):
    return re.sub(
        r"{{lang(?:[^|]*?\|)*?([^|]*?)\}\}",
        r"\1",
        txt,
        flags=re.MULTILINE + re.VERBOSE
    )


def rm_html_tag(txt):
    return re.sub(
        r"<.+?>",
        "",
        txt,
        flags=re.MULTILINE + re.VERBOSE
    )


def composite_fx(*fx_list):
    fx, *fxs = fx_list
    if len(fxs) == 1:
        return lambda *args, **kwargs: fxs[0](fx(*args, **kwargs))
    return lambda *args, **kwargs: composite_fx(*fxs)(fx(*args, **kwargs))


def rm_markups(txt):
    fxs = [rm_emphasis_markups, rm_internal_links, rm_external_links,
           rm_lang_labels, rm_html_tag, lambda t: t.strip()]
    rm_fx = composite_fx(*fxs)
    return rm_fx(txt)


df = pd.read_json("./jawiki-country.json", lines=True)
text = df[df["title"] == "イギリス"].text.tolist()[0]
basic = re.search(r"^{{基礎情報.*?\n(.*?)\}\}$", text, re.MULTILINE + re.VERBOSE + re.DOTALL)
templates = OrderedDict(
    re.findall(
        r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))",
        basic.group(1),
        re.MULTILINE + re.VERBOSE + re.DOTALL
    )
)

for key, val in templates.items():
    rm_markup_txt = rm_markups(val)
    templates[key] = rm_markup_txt
    if val != rm_markup_txt:
        print(f"Key:{key}")
        print(f"Before:{val}")
        print(f"After:{rm_markup_txt}")

pprint.pprint(templates)
