#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# ignore the long float number, as long as it rounds to correct ans its okay, as TA said.
#
# YOUR NAME - THE DATE
# Jim Nguyen - 10/06/2021


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startLoc = Node(problem.start, h_eval = h.h_cost(problem.start))

    if problem.is_goal(startLoc.loc):
        return startLoc
    
    visited_Nodes = Frontier(startLoc, sort_by = 'h')
    visitedSet = set()
    visitedSet.add(startLoc)

    while not visited_Nodes.is_empty():
        tmpNode = visited_Nodes.pop()
        if problem.is_goal(tmpNode.loc):
            return tmpNode
        tmpNodeList = tmpNode.expand(problem)
        for node in tmpNodeList:
            if repeat_check == True:
                if node not in visitedSet:
                    visitedSet.add(node)
                    visited_Nodes.add(node)
            else:   
                visited_Nodes.add(node)

    return None
