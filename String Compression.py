def compress(chars):
    counter = 0
    curr = chars[-1]
    chars.insert(0, 'qq')
    for i in range(len(chars) - 1, -1, -1):
        if chars[i] == curr:
            counter += 1
        else:
            del chars[i+1:i+1+counter]
            if counter > 1:
                [chars.append(char) for char in reversed(str(counter))]

            chars.append(curr)
            curr = chars[i]
            counter = 1

    chars.remove('qq')
    chars.reverse()
    print(chars)
    return len(chars)


print(compress(["a","a","b","b","c","c","c"]))

