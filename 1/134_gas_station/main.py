class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        start, end = n-1, 0

        tank = gas[start] - cost[start]

        # we start from the last position
        while start > end:
            # we go as far as we could, pushing end to the next, as long as the gas allows it
            if tank >= 0:
                tank += gas[end] - cost[end]
                end += 1
            # when not possible to move end further more, we know if we choose this start, it can't go a circle
            # so we try another start by moving start to the previous position
            # until start and end meets
            else:
                start -= 1
                tank += gas[start] - cost[start]

        return start if tank >= 0 else -1


if __name__ == '__main__':
    s = Solution()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert s.canCompleteCircuit(gas, cost) == 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert s.canCompleteCircuit(gas, cost) == -1
