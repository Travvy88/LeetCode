def checkInclusion_TimeLimit(self, s1: str, s2: str) -> bool:
    sorted_s1 = sorted(s1)
    n = len(s1)
    for i in range(len(s2) - n + 1):
        to_check = sorted([s2[j] for j in range(i, i + n)])
        if to_check == sorted_s1:
            return True

    return False


def checkInclusion(self, s1: str, s2: str) -> bool:
    n = len(s1)

    def to_dict(s):
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

    s1_dict = to_dict(s1)

    window = list(s2[:n])
    start = 0
    to_check = to_dict(window)
    for i in range(n, len(s2)):
        if to_check == s1_dict:
            return True

        to_check[s2[start]] -= 1
        if to_check[s2[start]] == 0:
            del to_check[s2[start]]
        if i not in to_check:
            to_check[s2[i]] = 1
        else:
            to_check[s2[i]] += 1
        start += 1


    if to_check == s1_dict:
        return True

    return False


print(checkInclusion(0, "abc", "ccccbbbbaaaa"))