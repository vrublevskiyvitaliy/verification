import unittest
from ddt import ddt, data, unpack
from rsa import RSA

@ddt
class RSATest(unittest.TestCase):

    @data((3, 11, 7, 5), (3, 11, 3, 5), (11, 13, 11, 7))
    @unpack
    def test_decrypt_encrypt(self, p, q, e, m):
        rsa = RSA(p, q, e)
        self.assertEqual(m, rsa.decrypt(rsa.encrypt(m)))

    @data((3, 11, 7, 5, 16), (5, 11, 3, 9, 14), (7, 11, 17, 8, 57))
    @unpack
    def test_encrypt(self, p, q, e, m, encrypted):
        rsa = RSA(p, q, e)
        self.assertEqual(encrypted, rsa.encrypt(m))
