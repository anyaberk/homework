#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
from sqlite3 import dump


#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................


b="aeiouаеёиоуыюя"
f=open("dump.txt",'r', encoding="utf-8")
text=f.read().lower()
f.close()
print(text)
counts={}
for i in text:
    if i in b:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = counts.get(i,0)+1

for i in counts:
    print(f'Количество букв {i} - {counts[i]}')

print(counts)