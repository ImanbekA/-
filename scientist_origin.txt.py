import csv
'''Импортирование библиотеки csv'''
a = []
'''Пустой массив а'''
with open('scientist.txt', 'r', encoding='UTF-8') as file: '''Открыли файл для чтения с кодировкой UTF-8'''
    for i in file:
        a.append(i.split("#"))
for i in range(1, len(a)):
    for j in range(1, len(a)-1):
        if int(a[i][2][0:3]) > int(a[j][2][0:3]):
            a[j], a[i] = a[i], a[j]
for i in range (1,6): '''Вывести 5 самых первых припаратов'''
    print(a[i][0], a[i][1])



