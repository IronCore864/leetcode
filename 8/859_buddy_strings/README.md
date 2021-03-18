## 859. Buddy Strings

### 1 Corner Cases

If word A has only 1 character, it's not possible to swap two characters.

If word A and word B differ in length, it's not possible either.

### 2 Main Logic

#### 2.1 if A == B

If word A and B are exactly the same, it is still possible to swap two letters from A, if there are two identical letters in A.

Turning the list of letters of A into a set will remove the duplicates. If the length of the set is less than the length of A itself, it means there are duplicated letters, so it's possible to swap that two identical letters.

Therea are multiple ways to detect if there are duplicated letters. One way is to use Counter from collections.

Given the size of A is under 20,000 characters, the method for duplication detection doesn't matter that much.

#### 2.2 if A != B

Iterate over A and B, find out the positions where the letters are different. If there are more than two positions that are different, it's not possible to swap.

If there are only one position that is different, it's not possible either.

When there are exactly two positions that are different, let's say position `x` and `y`, and only when:

```python
A[x] == B[y] and A[y] == B[x]
```

it's possible to swap these two.

#### 3 Golang Implementation

Same logic as the python version except using a different way of detecting duplicated characters.
