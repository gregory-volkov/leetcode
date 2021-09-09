    def romanToInt(self, s: str) -> int:
        rom2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        
        for i in range(len(s)):
            if i == len(s) - 1:
                num += rom2int[s[i]]
            else:
                if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    num -= 1
                    continue
                if s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    num -= 10
                    continue
                if s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    num -= 100
                    continue
                num += rom2int[s[i]]
        return num
