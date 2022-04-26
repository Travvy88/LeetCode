class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for interval in intervals:
            events.append((interval[0], -1))
            events.append((interval[1], 1))

        events.sort()
        merged = []
        count = 0
        for event in events:
            if event[1] == -1:
                if count < 1:
                    merged.append([event[0]])
                count += 1

            if event[1] == 1:
                if count <= 1:
                    merged[-1].append(event[0])
                count -= 1

        return merged

print(Solution.merge(0, [[1, 2],[1,1]]))






