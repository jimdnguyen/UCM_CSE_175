#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# ignore the long float number, as long as it rounds to correct ans its okay, as TA said.
# Worked with Denylson Fuentes
#
# YOUR NAME - THE DATE
# Jim Nguyen - 10/06/2021


from route import Node
from route import Frontier


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    startLoc = Node(problem.start)

    if problem.is_goal(startLoc.loc):
        return startLoc
    
    visited_Nodes = Frontier(startLoc, sort_by='g')
    visitedSet = set()
    visitedSet.add(startLoc)
    
    while not visited_Nodes.is_empty():
        tmpNode = visited_Nodes.pop()
        if problem.is_goal(tmpNode.loc):
            return tmpNode
        tmpNodeList = tmpNode.expand(problem)
        for node in tmpNodeList:
            if repeat_check:
                if node in visitedSet:
                    if visited_Nodes.contains(node) and (visited_Nodes[node] > node.value(sort_by="g")):
                        visited_Nodes.__delitem__(node)
                        visited_Nodes.add(node)
                else:
                    visited_Nodes.add(node)
                    visitedSet.add(node)
            else:   
                visited_Nodes.add(node)
    return None
