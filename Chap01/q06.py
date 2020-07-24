import q05 as ng

x_str = "paraparaparadise"
y_str = "paragraph"

X = set(ng.n_gram(x_str, 2))
Y = set(ng.n_gram(y_str, 2))
target_bi_gram = {('s', 'e')}

print(f"和集合: {X|Y}")
print(f"積集合: {X&Y}")
print(f"差集合: {X-Y}")
print(f"bi-gram'se'がXに含まれるか: {target_bi_gram <= X}")
print(f"bi-gram'se'がYに含まれるか: {target_bi_gram <= Y}")