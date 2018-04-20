#!/usr/bin/python

from heapq import heappush, heappop

class Node:
    def __init__(self):
        self.connections = []
        self.previous = None
        self.cost = None
        self.heuristic = None
        self.priority = None
    def move(self, previous=None, goal=None):
        self.previous = previous
        if previous is None:
            self.cost = 0
            self.heuristic = None   # First node, heuristic and
            self.priority = None    # priority are not relevant
        else:
            self.cost = previous.cost + self.cost_function(previous)
            self.heuristic = self.heuristic_function(goal)
            self.priority = self.cost + self.heuristic
    def cost_function(self, previous):
        raise NotImplementedError("No cost function implemented")
    def heuristic_function(self, goal):
        raise NotImplementedError("No heuristic function implemented")
    def __gt__(self, other):
        return self.priority > other.priority
    def __lt__(self, other):
        return self.priority < other.priority

class PositionNode(Node):
    def __init__(self, x, y):
        Node.__init__(self)
        self.x = x
        self.y = y
    def euclidean_distance(self, other):
        return ((((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** (.5))
    def cost_function(self, previous):
        return self.euclidean_distance(previous)
    def heuristic_function(self, goal):
        return self.euclidean_distance(goal)
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

def solve(start, goal):
    found = False
    new = []
    visited = []

    start.move()
    new.append(start)

    while new:
        current = heappop(new)
        visited.append(current)
        if current == goal:
            found = True
            break
        for node in current.connections:
            if node not in visited:
                node.move(current, goal)
                heappush(new, node)

    if found:
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = current.previous
        path.append(current)
        return path[::-1]
    else:
        return None
