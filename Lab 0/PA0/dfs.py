#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    startLoc = Node(problem.start)

    if problem.is_goal(startLoc.loc): 
        return startLoc
    visited_Nodes = Frontier(startLoc, stack=True)
    visitedSet = set () 
    visitedSet.add(startLoc)  # I added in the start node b/c old pseudocode did not have it
    while not visited_Nodes.is_empty():
        tmpNode = visited_Nodes.pop()#this returns node
        if problem.is_goal(startLoc.loc): # node is the whole object/class, node.loc is only getting location attribute
                return startLoc
        tmpNodeList = tmpNode.expand(problem)#this returns list of children nodes
        for node in tmpNodeList:
            if problem.is_goal(node.loc): # node is the whole object/class, node.loc is only getting location attribute
                return node
            if repeat_check == True: #checking if true, and find node in list, should not add it to frontier
                if node not in visitedSet:
                    visitedSet.add(node)
                    visited_Nodes.add(node)
            else:
                visited_Nodes.add(node)
    return None

    #LIFO Last in First out
    #|3|
    #|5|
    #|1|
    #|2|
    #|3|
    #use stack

# for this code, I copied over the code I had in bfs and changed from stack to True in Frontier(startLoc, stack = True), line 31