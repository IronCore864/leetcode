## 3. Longest Substring without Repeating Characters

### Algorithm

Keep a dict, where the key is a character in the input string, and the value is the index of the character in the string.

Start from index zero and use a sliding window to iterate through the input string. If the next char isn't used yet, calculate max length of the substr; if it's used, find the previous occurrence of it, and move the start of the sliding window after that char.

### Example

Input: "abcdbef"

Begin: start = 0 (char 'a').

Go to next char index 1, char 'b', not used, max substr length = 2

Go to next char index 2, char 'c', not used, max substr length = 3

Go to next char index 3, char 'd', not used, max substr length = 4

Go to next char index 4, char 'b', used, move start to 5 and start from there. No need to try start with values less than 5 because the max sub str length is less.
