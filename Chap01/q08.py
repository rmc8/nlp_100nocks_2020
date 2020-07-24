def cipher(txt):
    def helper(s):
        if s.islower():
            return chr(219 - ord(s))
        return s
    
    return "".join(map(helper, txt))


if __name__ == "__main__":
    text = "genius is one percent inspiration, ninety-nine percent perspiration"
    ans = cipher(text)
    print(ans)
    ans = cipher(ans)
    print(ans)
