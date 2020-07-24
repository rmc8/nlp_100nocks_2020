s1 = "パトカー"
s2 = "タクシー"
ans = ""

for t1, t2 in zip(s1, s2):
    ans += (t1 + t2)
    
print(ans)
