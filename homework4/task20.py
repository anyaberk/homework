#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

f = open ("import_this.txt", "r")
lines = f.readlines()
print(lines)
for i in range(len(lines)):
    print(lines[len(lines)-i-1])