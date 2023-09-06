from typing import List


class IntervalInsertion:
    """
    Here I provide a solution to insert a new interval into a list of existing intervals.
    Overlapping intervals are merged.
    """

    def insert_interval(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into the list of intervals.
        :param intervals: A list of intervals where each interval is represented by a list of two integers.
        :param new_interval: The interval to be inserted.
        :return: A list of intervals with the new interval inserted (and overlapping intervals merged).
        """

        # Categorize existing intervals based on their relation to the new interval.
        before = [i for i in intervals if i[1] < new_interval[0]]
        overlapping = [i for i in intervals if i[1] >= new_interval[0] and i[0] <= new_interval[1]]
        after = [i for i in intervals if i[0] > new_interval[1]]

        # If there are overlapping intervals, merge them with the new interval.
        if overlapping:
            merged_start = min(overlapping[0][0], new_interval[0])
            merged_end = max(overlapping[-1][1], new_interval[1])
            return before + [[merged_start, merged_end]] + after

        # If no overlapping intervals, simply insert the new interval at the appropriate position.
        return before + [new_interval] + after


# Test Cases
def test_interval_insertion():
    ii = IntervalInsertion()

    intervals1 = [[1, 3], [6, 9]]
    new_interval1 = [2, 5]
    assert ii.insert_interval(intervals1, new_interval1) == [[1, 5], [6, 9]]

    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval2 = [4, 8]
    assert ii.insert_interval(intervals2, new_interval2) == [[1, 2], [3, 10], [12, 16]]

    intervals3 = []
    new_interval3 = [5, 7]
    assert ii.insert_interval(intervals3, new_interval3) == [[5, 7]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_interval_insertion()
