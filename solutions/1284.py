# 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/


from itertools import product 
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:

        def mat2num(mat):
            n, m = len(mat[0]), len(mat)
            mul = 1
            ans = 0
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 1:
                        ans |= 2**(i*n + j)
            return ans

        def is_cool(mat):
            return mat == 0
        
        n, m = len(mat[0]), len(mat)

        # Generate all possible flip masks
        # For applying them XOR is used
        masks = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mask = 0
                mask |= 2**(i*n + j)
                if j > 0:
                    mask |= 2**(i*n + j - 1)
                if j < n - 1:
                    mask |= 2**(i*n + j + 1)
                if i > 0:
                    mask |= 2**((i - 1)*n + j)
                if i < m - 1:
                    mask |= 2**((i + 1)*n + j)
                masks[i][j] = mask
        
        matrices = [mat2num(mat)]
        visited = set()
        new_visit = True
        steps = 0
        max_steps = 2**(m*n)
        while new_visit and not any(is_cool(mat) for mat in matrices):
            old_visit = len(visited)
            new_matrices = [mat^masks[i][j] for mat in matrices for i in range(m) for j in range(n) if mat not in visited]
            visited.update(matrices)
            new_visit = len(visited) != old_visit
            matrices = new_matrices
            steps += 1
        
        return steps if new_visit else -1
