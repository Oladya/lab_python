
s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
L=s.split()
r= []
print(L)
for i in L:
    if i.startswith("М") == False and not i.startswith("м"):
        r.append(i)


print(" ".join(r))
