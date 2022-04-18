def busyStudent(startTime, endTime, queryTime) -> int:
    events = []
    for i in range(len(startTime)):
        events.append((startTime[i], -1))
        events.append((endTime[i], 1))

    events.append((queryTime, 0))
    events.sort()

    currStuds = 0
    for event in events:
        if event[1] == -1:
            currStuds += 1
        elif event[1] == 1:
            currStuds -= 1
        else:
            return currStuds


print(busyStudent([4], [4], 4))