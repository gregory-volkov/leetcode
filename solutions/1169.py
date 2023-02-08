# 1169. Invalid Transactions
# https://leetcode.com/problems/invalid-transactions/description/

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def add_ans(ans, tr_name, info):
            ans.append(f"{tr_name},{info[0]},{info[1]},{info[2]}")
        
        # Process transactions list, so we will have a map TransactionName -> (other info)
        ans = []
        name2info = {}
        usd_tres = 1000
        t_tres = 60
        for transaction in transactions:
            name, t, amt, place = transaction.split(',')
            if name not in name2info:
                name2info[name] = []
            name2info[name].append((int(t), int(amt), place))
        
        for name, info in name2info.items():
            name2info[name] = sorted(name2info[name])
            
        for name, info in name2info.items():
            i = 0
            loc2trans = {}
            print(info)
            while i < len(info):
                cur = info[i]
                is_susp = False
                # 1000 usd check
                if cur[1] > usd_tres:
                    is_susp = True

                j = i - 1
                while not is_susp and j >= 0 and cur[0] - info[j][0] <= 60:
                    print(cur[0], info[j][0])
                    if cur[2] != info[j][2]:
                        is_susp = True
                    j-= 1
                j = i + 1
                while not is_susp and j < len(info) and info[j][0] - cur[0] <= 60:
                    print(cur[0], info[j][0])
                    if cur[2] != info[j][2]:
                        is_susp = True
                    j+= 1

                if is_susp:
                    add_ans(ans, name, cur)

                i+= 1

        return ans
