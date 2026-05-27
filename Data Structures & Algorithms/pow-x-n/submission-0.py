class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if n >= 0:
            for i in range(n):
                product *= x
        else:
            for i in range(-n):
                product *= (1/x)
                print("The product is:", product)

        return product
        