def merge_intervals(intervals):
    # Step 1: Sort the intervals based on the starting point.
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize a result list with the first interval.
    result = [intervals[0]]

    # Step 3: Traverse the sorted intervals from the second interval onward.
    for i in range(1, len(intervals)):
        # Current interval
        curr_start, curr_end = intervals[i]
        # Last interval in the result list
        last_start, last_end = result[-1]

        # Step 4: Compare current interval with the last interval in the result list.
        # Step 5: If they overlap, merge them; if not, simply append to the result list.
        if curr_start <= last_end:
            result[-1] = [last_start, max(last_end, curr_end)]
        else:
            result.append(intervals[i])

    return result


# Test Case 1
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Expected: [[1,6], [8,10], [15,18]]

# Test Case 2
print(merge_intervals([[1, 4], [4, 5]]))  # Expected: [[1,5]]
