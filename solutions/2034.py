# 2034. Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice:

    def __init__(self):
        self.time2price = {}
        self.price2amt = {}
        self.max_time = 0
        self.min = 10 ** 9
        self.max = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.max_time:
            self.max_time = timestamp
        oldprice = None
        if timestamp in self.time2price:
            oldprice = self.time2price[timestamp]
            self.price2amt[oldprice] -= 1
            if self.price2amt[oldprice] == 0:
                del self.price2amt[oldprice]
        
        if price not in self.price2amt:
            self.price2amt[price] = 0

        self.time2price[timestamp] = price
        self.price2amt[price] += 1

        if oldprice is not None:
            if oldprice == self.max:
                self.max = max(self.price2amt.keys())
            if oldprice == self.min:
                self.min = min(self.price2amt.keys())

        if price > self.max:
            self.max = price
        if price < self.min:
            self.min = price
        
        
    def current(self) -> int:
        return self.time2price[self.max_time]

    def maximum(self) -> int:
        return self.max

    def minimum(self) -> int:
        return self.min


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
