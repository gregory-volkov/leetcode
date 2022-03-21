# Upper bound
# Returns the id of required item or the place where it should be
def bsearch_upper(lst, item):
    i, j = 0, len(lst)
    while i < j:
        mid = (i + j) // 2
        if lst[mid] <= item:
            i = mid + 1
        else:
            j = mid
    return i - 1
