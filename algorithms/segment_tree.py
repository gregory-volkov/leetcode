# Segment tree implementation for the SUM function
# The code below provides the following functions:
# build_tree: builds the segment tree from a list
# update: update a value by index and rebuilds tree (actually, a relevant path in the tree)
# sumRange: returns sum of a given range [l, r)

def build_tree(a):
    n = len(a)
    # The number of nodes is 2*n-1. For the convenience nodes numbering starts with 1
    tree = [0 for _ in range(2 * n)]

    # Filling n..2n-1 nodes
    for i in range(n):
        tree[n + i] = a[i]

    # Creating parent node by adding left and right child
    # From n-1 downto 1
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]
    return tree


def update(tree, n, index, val):
    # Set value at position index
    tree[index + n] = val
    index += n

    # After updating the child node,update parents
    i = index

    while i > 1:
        # Update parent by adding new left and right child
        if i % 2:
            tree[i // 2] = tree[i] + tree[i-1]
        else:
            tree[i // 2] = tree[i] + tree[i + 1]
        i = i // 2

    return tree


def sumRange(tree, n, left, right):
    sum = 0
    l = left + n
    r = right + n

    while l < r:
        if l % 2 == 1:
            sum += tree[l]
            l += 1
        if r % 2 == 1:
            r -= 1
            sum += tree[r]
        l //= 2
        r //= 2
    return sum


a = [1, 2, 3, 4, 5, 6]
n = 6
tree = build_tree(a)
print(tree)
tree = update(tree, n, 1, 4)
print(tree)
print(sumRange(tree, n, 1, 3))
