n_chislo = input('Skolko nado? ')
new_chislo = int(n_chislo) // 2
list = []
for i in range(new_chislo):
    list.append(1)
    list.append(0)
if list[-1] == 0 and len(list) < int(n_chislo):
    list.append(1)
print(list)