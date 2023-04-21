from typing import Tuple
import numpy as np

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьяюя"
open_text = "криптологи"
m = 33
keys = np.array([[26, 30], [20, 32]])

size = len(open_text)
y = [None] * size

for i in range(0, size - 1, 2):
    a = np.array([alphabet.find(open_text[i]), alphabet.find(open_text[i + 1])])
    temp = a.dot(keys)
    y[i], y[i + 1] = alphabet[temp[0] % m], alphabet[temp[1] % m]
encrypted_text = ''.join(y)
print(encrypted_text)

def simple_decryption(alphabet: str, key: str, message: str) -> str:
    if len(alphabet) != len(key):
        raise ValueError(
            f'Alphabet and key expected to have same length. But got alphabet: {len(alphabet)}, key: {len(key)} '
        )
    return "".join([alphabet[key.find(i)] for i in message])



print(
    simple_decryption(
        alphabet="абвгдеёжзийклмнопрстуфхцчшщъыьяюя",
        key="ЪЗЙЩЛШУИРДЧЁСФЕТЦЭМАВПЯБЫЖЮОХНЬГК".lower(),
        message="ЪЗЭДЁТМ".lower(),
    )
)
