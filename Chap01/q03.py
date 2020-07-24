import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = re.sub("[,\.]", "", s)
ans = [len(t) for t in s.split()]
print(ans)
