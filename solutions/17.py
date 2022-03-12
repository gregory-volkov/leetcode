# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    num2letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    return list(map(lambda x: ''.join(x),
    product(*(num2letters[ch] for ch in digits))))
