# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

import string

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
al = string.ascii_lowercase

for i in range(1, 26):
    d_text = ""
    for j in text:
        if j.isalpha():
            d_char = chr((ord(j) - ord('a') - i) % 26 + ord('a'))
            d_text += d_char
        else:
            d_text += j

    print(f"Расшифрованный текст при сдвиге {i}: {d_text}")