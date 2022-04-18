def check(array):
    maxans = -1
    sum1, sum2 = 0, 0
    for el in array:
        sum2 += el
        if el == 0:
            maxans = max(maxans, sum1 + sum2)
            sum1 = sum2
            sum2 = 0

    maxans = max(maxans, sum1 + sum2)
    if maxans == len(array):
        return maxans - 1
    else:
        return maxans



print(check([1, 1, 0, 0, 1, 1, 1, 1, 1]))