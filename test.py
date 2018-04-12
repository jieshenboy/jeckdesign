import copy
a = [1,2,[1,2,3],4]
b = a.copy()
c = copy.deepcopy(a)
a[2].append(9)

a.append('c')
print(a)
print(b)
print(c)

