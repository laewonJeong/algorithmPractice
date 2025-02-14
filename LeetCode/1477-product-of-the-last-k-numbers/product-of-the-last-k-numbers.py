class ProductOfNumbers:

    def __init__(self):
        self.prefix = []
        self.n = 0

    def add(self, num: int) -> None:
        if not self.prefix and num != 0:
            self.prefix.append(num)
        elif num == 0:
            self.prefix = []
            self.n = -1
        else:
            self.prefix.append(self.prefix[-1] * num)
        
        self.n+=1

    def getProduct(self, k: int) -> int:
        #print(self.prefix, k, self.n)
        if self.n > k:
            return self.prefix[-1] // self.prefix[self.n - k - 1]
        elif self.n == k:
            return self.prefix[-1]
        else:
            return 0

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)