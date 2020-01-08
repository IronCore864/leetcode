class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != color:
                return

            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]

        if color != newColor:
            traverse(sr, sc)
        return image


s = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(s.floodFill(image, 1, 1, 2))
