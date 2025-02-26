class ProductOfNumbers:

    def __init__(self):
        self.store = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.store = [1]
        else:
            self.store.append(num * self.store[-1])  

    def getProduct(self, k: int) -> int:
        if k >= len(self.store):
            return 0
        return self.store[-1] // self.store[-k-1]
        

            
       


        
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)