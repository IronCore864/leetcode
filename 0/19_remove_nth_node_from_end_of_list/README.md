## One-Pass Solution

Keeping a fixed distance of n between pointers "current" and "tail".

Move the two pointers together one step at a time, like a sliding fixed length window.

When the "tail" pointer is None, the "current" pointer will points at the element which needs to be removed.

Illustration:

```bash
head: 1 -> 2 -> 3 -> 4 -> 5
n: 2
```

```bash
1       -> 2 -> 3 -> 4 -> 5
^
previous
current
tail
```

```bash
for i in range(n):
    tail = tail.next
```

```bash
# i=0:
1       -> 2 -> 3 -> 4 -> 5
^
current   ^
          tail

# i=1:
1       -> 2 -> 3 -> 4 -> 5
^
current         ^
                tail
```

Now the distance between tail and current are 2 (the value of n.)

```bash
while tail != None:
    previous = current
    current = current.next
    tail = tail.next
```

```bash
# beginning state
1       -> 2 -> 3 -> 4 -> 5
^
previous
current         ^
                tail

# 1st iteration
1 -> 2 ->     3 -> 4 -> 5
     ^        ^
     previous current   ^
                        tail

# 2nd iteration
1 -> 2 -> 3 ->     4 -> 5
          ^        ^
          previous current   ^
                             tail(None)
```

When tail is None, current points to the nth element from the tail of the list.

Removal:

```bash
# remove "current" node
previous.next = current.next

# cornor case: if previous == current, it means removing the first element of the list
head = previous.next
return head
```
