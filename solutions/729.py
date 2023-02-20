# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:
    def bsearch_lower(self, item):
        lst = self.starts
        i, j = 0, len(lst)
        while i < j:
            mid = (i + j) // 2
            if item <= lst[mid]:
                j = mid
            else:
                i = mid + 1
        return i

    def __init__(self):
        self.start2end = {}
        self.starts = []

    def no_conflict(self, p1, p2):
        print(f"Conflict check for {p1} and {p2}")
        st1, en1 = p1
        st2, en2 = p2
        if st1 > st2:
            st1, st2 = st2, st1
            en1, en2 = en2, en1
        return en1 <= st2

    def book(self, start: int, end: int) -> bool:
        if not self.starts:
            self.starts.append(start)
            self.start2end[start] = end
            return True
        
        st_pos = self.bsearch_lower(start)
        st1 = self.starts[st_pos - 1 if st_pos > 0 else 0]
        en1 = self.start2end[st1]
        st2 = self.starts[st_pos if st_pos < len(self.starts) else -1]
        en2 = self.start2end[st2]
        # print(self.starts, self.start2end, start, end)
        if self.no_conflict((start, end), (st2, en2)) and self.no_conflict((start, end), (st1, en1)):
            self.starts.insert(st_pos, start)
            self.start2end[start] = end
            return True
        else:
            return False

        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
