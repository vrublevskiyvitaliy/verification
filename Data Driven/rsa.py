
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


class RSA():
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.modulus_n = p * q
        self.totient = (p - 1) * (q - 1)
        self.d = modinv(self.e, self.totient)

    def encrypt(self, number):
        return int((number ** self.e) % (self.modulus_n))

    def decrypt(self, number):
        return int(number ** self.d) % (self.modulus_n)

