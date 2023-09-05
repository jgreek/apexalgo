from typing import List

class ImageFloodFill:
    """
    The Flood Fill algorithm is similar to the bucket tool in MS Paint.
    Given a 2D matrix (image) where each integer represents a color, a start pixel, and a new color,
    it modifies the color of the starting pixel, then its neighboring pixels,
    and so on, until there are no more adjacent pixels of the same color to the starting pixel.

    This class provides a solution to the flood fill problem.

    For example, given:
    Image: [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc (starting pixel): 1, 1
    NewColor: 2
    Result would be: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    """

    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """Performs flood fill on an image starting at position (sr, sc) with the specified color."""
        if image[sr][sc] == color:
            return image

        orig_color = image[sr][sc]

        def dfs(r: int, c: int):
            """Depth-first search helper function to perform flood fill."""
            # If out of bounds or not the original color, return
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != orig_color:
                return

            # Change the color of the current pixel
            image[r][c] = color

            # Continue DFS for neighboring pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


# Test Cases
def test_flood_fill():
    img_fill = ImageFloodFill()

    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result1 = img_fill.flood_fill(image1, 1, 1, 2)
    expected1 = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert result1 == expected1

    image2 = [[0, 0, 0], [0, 1, 1]]
    result2 = img_fill.flood_fill(image2, 1, 1, 1)
    expected2 = [[0, 0, 0], [0, 1, 1]]
    assert result2 == expected2

    print("All test cases passed!")


if __name__ == "__main__":
    test_flood_fill()
