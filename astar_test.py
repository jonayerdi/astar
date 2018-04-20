#!/usr/bin/python

from astar import PositionNode, solve

def test():
    nodes = []
    for x in range(0, 4):
        nodes.append([])
        for y in range(0, 4):
            nodes[x].append(PositionNode(x, y))
    nodes[0][0].connections = [nodes[0][1], nodes[1][0]]
    nodes[0][1].connections = [nodes[0][0], nodes[0][2]]
    nodes[0][2].connections = [nodes[0][1], nodes[0][3]]
    nodes[0][3].connections = [nodes[0][2], nodes[1][3]]
    nodes[1][0].connections = [nodes[0][0]]
    nodes[1][1].connections = [nodes[1][2], nodes[2][1]]
    nodes[1][2].connections = [nodes[1][1], nodes[2][2]]
    nodes[1][3].connections = [nodes[0][3], nodes[2][3]]
    nodes[2][0].connections = [nodes[3][0], nodes[2][1]]
    nodes[2][1].connections = [nodes[2][0], nodes[1][1], nodes[3][1]]
    nodes[2][2].connections = [nodes[1][2], nodes[2][3]]
    nodes[2][3].connections = [nodes[2][2], nodes[1][3]]
    nodes[3][0].connections = [nodes[2][0]]
    nodes[3][1].connections = [nodes[2][1], nodes[3][2]]
    nodes[3][2].connections = [nodes[3][1], nodes[3][3]]
    nodes[3][3].connections = [nodes[3][2]]
    result = solve(nodes[3][3], nodes[1][0])
    for step in result:
        print(step)

if __name__ == "__main__":
    test()
