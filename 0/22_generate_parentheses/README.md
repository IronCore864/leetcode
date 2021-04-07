## 22. Generate Parentheses

### 1 Brute Force Using Backtracking

Keep a track of current path, starting from empty string ''

Add a left parenthesis, recursion the remaining part

After the recursion, pop the left parenthesis, add a right parenthesis, recursion the remaining part

In this way, we iterated over all possible situations.

Code:

```python
def dfs_backtracking(path=''):
    if len(path) == 2*n:
        if self.is_valid(path):
            result.append(path)
        return

    path += '('
    dfs_backtracking(path)
    path = path[0:len(path)-1]

    path += ')'
    dfs_backtracking(path)
```

### 2 Improvement Over the Brute Force

For example, when n == 2:

It doesn't make sense to add more than n left parentheses, for example, `((((` will be invalid for sure.

It also doesn't make sense to add more right than left, for example, `()))`.

So before the recursion we can add conditions to check these, so that we only iterate over valid results.

Code:

```python
def dfs_backtracking_optimized(path='', left=0, right=0):
    # skip invalid results
    if len(path) == 2*n:
        result.append(path)
        return

    # only add left parenthesis when left < n
    # for example, if n == 2, ((() will apparently be not valid
    if left < n:
        path += '('
        dfs_backtracking_optimized(path, left+1, right)
        path = path[0:len(path)-1]

    # only add right parenthesis when left >right
    # for example, if n == 2, ())) will apparently be not valid
    if left > right:
        path += ')'
        dfs_backtracking_optimized(path, left, right+1)
```

We add two more parameters to keep count of the left and right parentheses, and skip invalid situations to speed things up.
