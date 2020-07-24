def gen_text(x, y, z):
    return f"{x}時の{y}は{z}"


if __name__ == "__main__":
    print(gen_text(12, "気温", 22.4))
