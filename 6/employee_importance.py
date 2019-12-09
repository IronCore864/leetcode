"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        sub = []
        for e in employees:
            if e.id == id:
                res = e.importance
                sub = e.subordinates
                break
        for s in sub:
            res += self.getImportance(employees, s)

        return res
