class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)


        while b != 0:
            xor = a ^ b
            carry = (a & b) << 1
            a = xor
            b = carry
        return bin(a)[2:]