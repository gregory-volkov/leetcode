# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.x2y, self.y2x = {}, {}
        self.point2amt = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
            
        if x not in self.x2y:
            self.x2y[x] = set()
        if y not in self.y2x:
            self.y2x[y] = set()
                    
        self.x2y[x].add(y)
        self.y2x[y].add(x)
        if (x, y) not in self.point2amt:
            self.point2amt[(x, y)] = 1    
        else:
            self.point2amt[(x, y)] += 1
            
    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point[0], point[1]
        for y1 in self.x2y.get(x, iter(())):
            for x1 in self.y2x.get(y1, iter(())):
                # x, y
                # x, y1
                # x1, y1
                # Looking for x1, y
                if y1 == y or x1 == x or (abs(x1 - x) != abs(y1 - y)):
                    continue
                res += self.point2amt.get((x1, y), 0) * self.point2amt.get((x1, y1), 0) * self.point2amt.get((x, y1), 0)
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
