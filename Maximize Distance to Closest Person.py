def check(seats):

        currMax, curr = 0, 0

        for n in seats:
            if n:
                if not currMax and seats[0] == 0:
                    currMax = max(currMax, curr)
                else:
                    currMax = max(currMax, (curr + 1) // 2)
                curr = 0
            else:
                curr += 1

        return max(currMax, curr)
print(check([1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]))



