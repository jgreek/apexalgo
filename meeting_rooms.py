from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Iterate over the intervals
    for i in range(len(intervals) - 1):  # Stop at the penultimate interval
        cur = intervals[i]
        next_interval = intervals[i + 1]

        # Check if the current interval's end time is after the next interval's start time
        if cur[1] > next_interval[0]:
            return False

    return True


# Test cases
test_cases = [
    ([[0, 30], [5, 10], [15, 20]], False),  # Overlapping meetings
    ([[7, 10], [2, 4]], True),  # No overlapping meetings
    ([[1, 5], [2, 6], [3, 7]], False),  # Multiple overlaps
    ([[1, 5], [5, 6], [6, 7]], True),  # Meetings end and start at the same time
    ([[1, 5], [5, 10], [10, 15]], True)  # Multiple meetings end and start at the same time
]

# Running the test cases
for intervals, expected in test_cases:
    result = canAttendMeetings(intervals)
    print(
        f"canAttendMeetings({intervals}) = {result}; Expected = {expected}; {'PASS' if result == expected else 'FAIL'}")
