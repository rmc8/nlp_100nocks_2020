def n_gram(target, n):
    range_num = len(target) - n + 1
    return [tuple(target[i: i + n]) for i in range(range_num)]


if __name__ == "__main__":
    # REF: https://qiita.com/kazmaw/items/4df328cba6429ec210fb
    txt = "I am an NLPer"
    print(n_gram(txt.split(), 2))
    print(n_gram(txt, 2))
