from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)

        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')

        return route[::-1]
