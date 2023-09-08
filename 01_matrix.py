from collections import deque
from typing import List


class MatrixUpdater:
    def __init__(self, mat: List[List[int]]):
        """
        Initialize MatrixUpdater with input matrix, directions, and an output matrix.
        """
        self.mat = mat
        self.m, self.n = len(mat), len(mat[0])
        self.output = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        self.queue = deque()
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def initialize_output_and_queue(self):
        """
        Initialize the output matrix and the queue.
        Add all cells with 0s from the input matrix to the queue and mark them as 0 in the output matrix.
        """
        for i in range(self.m):
            for j in range(self.n):
                if self.mat[i][j] == 0:
                    self.queue.append((i, j))
                    self.output[i][j] = 0

    def valid_neighbour(self, x: int, y: int) -> bool:
        """
        Check if (x, y) is a valid unvisited neighbour in the matrix.
        """
        return 0 <= x < self.m and 0 <= y < self.n and self.output[x][y] == -1

    def explore_neighbours(self):
        """
        Use BFS to explore and update the distances in the output matrix.
        """
        while self.queue:
            x, y = self.queue.popleft()
            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if self.valid_neighbour(new_x, new_y):
                    self.output[new_x][new_y] = self.output[x][y] + 1
                    self.queue.append((new_x, new_y))

    def updateMatrix(self) -> List[List[int]]:
        """
        Main function to update the matrix based on BFS.
        """
        if not self.mat:
            return []

        self.initialize_output_and_queue()
        self.explore_neighbours()

        return self.output


class MatrixProblem:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        updater = MatrixUpdater(mat)
        return updater.updateMatrix()


# Test Cases
if __name__ == "__main__":
    solution = MatrixProblem()

    mat1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert solution.updateMatrix(mat1) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    mat2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert solution.updateMatrix(mat2) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    print("All tests passed!")
