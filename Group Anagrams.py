def groupAnagrams(strs):
    letters = dict()
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in letters.keys():
            letters[sorted_s] = [s]
        else:
            letters[sorted_s].append(s)

    ans = []
    for key in letters.keys():
        ans.append(letters[key])
    return ans


d = dict()
print(d.keys())
print(groupAnagrams(["a"]))