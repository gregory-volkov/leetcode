# 2115. Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        n = len(recipes)
        smth_new = True
        ans = set()
        while smth_new:
            smth_new = False
            for i in range(n):
                rec_ingr = ingredients[i]
                rec_name = recipes[i]
                if (rec_name not in ans) and all(ingr in supplies for ingr in rec_ingr):
                    supplies.add(rec_name)
                    ans.add(rec_name)
                    smth_new = True
        return list(ans)
