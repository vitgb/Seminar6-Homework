# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('Введите n: '))
list1 = list(map(int, input().split()))
mini, maxi = map(int, input('mini maxi').split())
for i in range(1, n-1):
    if maxi > list1[i] > mini:
        print(i, end=' ')
