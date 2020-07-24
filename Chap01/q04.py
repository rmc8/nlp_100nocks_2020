s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans = {}
for n, wd in enumerate(s.split(), 1):
    end = 1 if n in [1, 5, 6, 7, 8, 9, 15, 16, 19] else 2
    ans[wd[:end]] = n
print(ans)
