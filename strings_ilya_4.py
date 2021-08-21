# Сгенерировать список [[[[[..[1]...]]] в котором n уровней вложенности
#
# a = [1, 2, [3, 4]]
# b = a[2]
#
# # b[0] = 1
# print(b)
# print(a)

levels = input('skok?')
list = []
for i in levels:
    list.append(i)

print(list)