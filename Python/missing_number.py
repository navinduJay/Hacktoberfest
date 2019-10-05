# FIND THE MISSING NUMBER

arr = [1, 2, 3, 5]


def findMissingNo(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2
    sumArr = sum(arr)
    return total - sumArr


result = int(findMissingNo(arr))
print(result)
