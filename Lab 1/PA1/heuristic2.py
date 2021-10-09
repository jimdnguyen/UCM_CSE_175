#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# purpose to estimate future cost
# doesnt overestimate actual cost
# in time units
# can calc eudication distance
# convert distance to speed
# unique speed between speed
#
# YOUR NAME - THE DATE
# Jim Nguyen - 10/06/2021



import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        #find speed here
        #have whole problem
        #speed = d/t
        #d = euc dis
        # euc dis needs 2 loc, your location and end location
        #t = action cost
        #action cost -> current node and children node
        # PLACE ANY INITIALIZATION CODE HERE
        self.speed = 0.0
        self.distance = 0.0
        self.locSpeed = {}
        self.locDistance = {}

        roadCost = 0.0
        for loc in problem.map.loc_dict:
            print(loc)
            for connection in problem.map.connection_dict:
                tmpRoadCost = problem.map.get(loc,connection)
                if tmpRoadCost is not None:
                    roadCost = tmpRoadCost
                #print(self.roadCost)
                self.distance = problem.map.euclidean_distance(loc,connection)
                self.locDistance[loc] = self.distance
                #print(distance)
                if roadCost != 0.0:
                    self.speed = self.distance/roadCost
                self.locSpeed[loc] = self.speed
                #print(self.speed)
        
        print(self.locSpeed.keys())
      

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            tmpSpeed = self.locSpeed[loc]
            tmpDistance = self.locDistance[loc]

            print(tmpSpeed)
            print(tmpDistance)
           
            value = 10000
            
            return value