
s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
L=s.split()
r= []
print(L)
for i in L:
    if i.startswith("М") == False and i.startswith("м") == False:
        r.append(i)


print(" ".join(r))
