"""Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком."""

import hashlib


def sum_p(str_1):
    res = set()  # чтобы не брать одинаковые хэши
    for i in range(len(str_1)):
        for j in range(len(str_1), i, -1):
            hstr = hashlib.sha1(str_1[i:j].encode('utf-8')).hexdigest()
            res.add(hstr)
    return len(res) - 1


print(sum_p('ABOBA'))
