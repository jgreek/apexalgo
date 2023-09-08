from collections import deque


class MRUQueue:
    """
    A Most Recently Used (MRU) Queue.

    When an item is fetched, it's moved to the end of the queue,
    making it the most recently used item.
    """

    def __init__(self, n: int):
        """
        Initialize the MRU queue with integers from 1 to n.
        """
        self.queue = deque(range(1, n + 1))

    def fetch(self, k: int) -> int:
        """
        Fetch the k-th item (1-based index) from the queue and move it to the end.
        """
        # Handle edge case where k is the last item
        if k == len(self.queue):
            return self.queue[-1]

        # Retrieve item, move it to the end, then return
        item = self.queue[k - 1]
        self.queue.remove(item)
        self.queue.append(item)
        return item


def main():
    # Test cases
    mru = MRUQueue(5)

    # Assert initial state
    assert list(mru.queue) == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], but got {list(mru.queue)}"

    # Assert fetch behavior
    assert mru.fetch(3) == 3, "Expected 3"
    assert list(mru.queue) == [1, 2, 4, 5, 3], f"Expected [1,2,4,5,3], but got {list(mru.queue)}"

    # Assert another fetch behavior
    assert mru.fetch(1) == 1, "Expected 1"
    assert list(mru.queue) == [2, 4, 5, 3, 1], f"Expected [2,4,5,3,1], but got {list(mru.queue)}"

    print("All assertions passed!")


if __name__ == "__main__":
    main()
