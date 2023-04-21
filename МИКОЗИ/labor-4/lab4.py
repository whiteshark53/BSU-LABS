class RSA:
    def __init__(self, p: int, q: int, e: int):
        self.n = p * q
        self.e = e
        self.d = self._generate_private_key(p, q)

    def euclid_ext(self, a: int, b: int):
        if a == 0:
            return b, 0, 1

        gcd, x, y = self.euclid_ext(b % a, a)
        return gcd, y - (b // a) * x, x

    def mod_inverse(self, a: int, n: int):
        g, x, _ = self.euclid_ext(a, n)
        if g == 1:
            return x % n
        return None

    def _generate_private_key(self, p: int, q: int) -> int:
        phi = (p - 1) * (q - 1)
        return self.mod_inverse(self.e, phi)

    def encrypt(self, message: int) -> int:
        return pow(message, self.e, self.n)

    def decrypt(self, message: int) -> int:
        return pow(message, self.d, self.n)


if __name__ == '__main__':
    p = 950226133300007
    q = 973747816218557
    e = 272205786540380931859823391349
    X1 = 487590396324873679144487947752
    Y2 = 371209390170967767404608751313

    rsa = RSA(p, q, e)
    print(f'Исходное сообщение X1: {X1}')
    Y1 = rsa.encrypt(X1)
    print(f'Зашифрованное сообщение Y1: {Y1}')
    X1_dec = rsa.decrypt(Y1)
    print(f'После расшифровки: {X1_dec}')

    print(f'Зашифрованное сообщение Y2: {Y2}')
    X2_dec = rsa.decrypt(Y2)
    print(f'После расшифровки: {X2_dec}')
