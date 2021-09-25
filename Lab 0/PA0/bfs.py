#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
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


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    
    startLoc = Node(problem.start)

    if problem.is_goal(startLoc.loc): 
        return startLoc
    visited_Nodes = Frontier(startLoc)
    visitedSet = set () 
    visitedSet.add(startLoc) # I added in the start node b/c old pseudocode did not have it
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

# FIFO first in first out
# |1|2|3|4|5|
#use queue

#searching for goal node
#in slides checks current node is goal node
#in txtbook, it delays it
# use sets to track what nodes i've visited, no order
# store any type of data together
# 

# https://docs.python.org/3/tutorial/classes.html initialized class
# https://www.w3schools.com/python/python_sets.asp understaing sets
# https://appdividend.com/2021/06/21/python-set-contains/ finds contents in set

#The TA helped me out a lot for this bfs code
# She told me that the Frontier.pop() command gives you the node its popping so I didn't have that before and I had to set it to a variable
# Also she told me that the Node.expand() command returns a list of node children so I had to set a variable to it for the for loop in the next line.
# She also recommended me to move the second if problem.is_goal(node.loc) inside the for loop since she has experienced it has worked better inside
# From there we worked together to get the work to a good place before running it and making any more adjustments. 