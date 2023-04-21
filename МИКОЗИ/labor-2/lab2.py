import numpy as np
from collections import deque


def to_dec(message):
    res = 0
    for i in range(len(message)):
        res += message[len(message) - 1 - i] * (2 ** i)
    return res


def to_4bin(x):
    if x >= 16:
        raise ValueError('Can not convert; binary representation has more than 4 digits')
    if x < 0:
        raise ValueError('Can not convert; x should be positive int < 6')
    res = []
    while x:
        res.append(x % 2)
        x = x // 2

    for i in range(4 - len(res)):
        res.insert(0, 0)

    return np.array(res, dtype=np.uint8)


def s_block(message, s):
    message = to_4bin(s[to_dec(message)])
    return message


def p_block(message):
    d = deque(message)
    d.rotate(-5)
    return np.array(d)


def sp_round(message, round_key, s1, s2):
    x = message ^ round_key
    t1 = x[:4]
    t2 = x[4:]
    n1 = s_block(t1, s1)
    n2 = s_block(t2, s2)
    x = np.concatenate((n1, n2))
    return p_block(x)


def sp_sub(message, key, round_keys, s1, s2, silent=True):
    x = message
    for n_it, round_key in enumerate(round_keys, start=1):
        rk = key[round_key]
        x = sp_round(x, rk, s1, s2)
        if not silent:
            print(f'Результат {n_it} итерации: {x}')
    return x


X = np.array([int(i) for i in "01111110"], dtype=np.uint8)
key = np.array([int(i) for i in "110111100101"], dtype=np.uint8)
round_keys = np.array([
    [1, 3, 5, 7, 2, 4, 6, 8],
    [5, 7, 9, 11, 6, 8, 10, 12],
    [12, 10, 4, 2, 1, 3, 9, 11]
]) - 1

s7 = [1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14]
s2 = [3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1]

print(f'Сообщение до шифрования: {X}')
print(f'Результат шифрования: {sp_sub(message=X, key=key, s1=s7, s2=s2, round_keys=round_keys, silent=False)}')

print()
print('Пример лавинного эффекта')
print()

X = np.array([int(i) for i in "11000111"], dtype=np.uint8)
print(f'Сообщение до шифрования: {X}')
print(f'Результат шифрования: {sp_sub(message=X, key=key, s1=s7, s2=s2, round_keys=round_keys, silent=False)}')
