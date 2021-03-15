## 79. Word Search

### 1 Corner Cases

If the word is longer than the number of board cells, it's not possible to form the word. For example:

```python
# board has totally 9 cells but the word has 10 characters.
board = [
    ['A', 'B', 'C'],
    ['S', 'F', 'C'],
    ['A', 'D', 'E']
]
word = 'ABCDEFGHIJ'
```

If the word has the same char 3 times but there are only 2 times of the char appearing on the board, it's not possible to construct the word. Example:

```python
# board has only 2 'A' but the word requires 3
board = [
    ['A', 'B', 'C'],
    ['S', 'F', 'C'],
    ['A', 'D', 'E']
]
word = 'AAA'
```

These two corner cases could rule out quite a few test cases and speed it up significantly.

## 2 The Recursive Algorithm

Iterate over all cells (i, j) of the board, try to match the first char of the word.

When a cell is matched, mark it (i, j) temporarily as used.

Then recursively search the remaining part of the word, trying to match the next char in the upper, lower, left, and right cells.

Until all chars in the word are matched, when nothing is left, return True; otherwise, if the next char can't be found, return False.
