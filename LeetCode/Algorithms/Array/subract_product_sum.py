class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_n = 0
        while n > 0:
            temp = n % 10
            n = int(n / 10)
            #print(temp, n)
            product = product * temp
            sum_n = sum_n + temp
        return product - sum_n