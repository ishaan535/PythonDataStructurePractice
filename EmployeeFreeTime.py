def EmployeeFreeTime(schedule):
    intervals = [interval for employee in schedule for interval in employee]
    intervals.sort(key = lambda x: x[0])
    resulting_list = []
    for interval in intervals:
        if not resulting_list or resulting_list[-1][1]<interval[0]:
            resulting_list.append(interval)
        else:
            resulting_list[-1][1] = max(resulting_list[-1][1], interval[1])

    free_time = []

    for i in range(1, len(resulting_list)):
        free_time.append([resulting_list[i-1][1], resulting_list[i][0]])

    return free_time


if __name__ == "__main__":
    test_cases = [
        [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]],
        [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
    ]

    for i, schedule in enumerate(test_cases, 1):
        print(f"Test Case {i}: {EmployeeFreeTime(schedule)}")