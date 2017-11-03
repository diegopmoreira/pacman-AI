# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    a = problem.getStartState()
    print a
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
"""
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH, 'West': Directions.WEST, 'East': Directions.EAST}
    startState = problem.getStartState()

    list = util.PriorityQueue()

    visited = set()
    list.push((startState, []),0)

    while not list.isEmpty():
        nextNode = list.pop()        
        actualState = nextNode[0]
        direct = nextNode[1]
        cost = 0

        if problem.isGoalState(actualState):
            cost = problem.getCostOfActions(direct)
            print "Total cost:" + str(cost)
            return direct
        if actualState not in visited:
            visited.add(actualState)
            for i in problem.getSuccessors(actualState):
                if i[0] not in visited:
                    list.push((i[0], direct + [directionTable[i[1]]]),0)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def hillClimbingSearch(problem): 
    from game import Directions
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH, 'West': Directions.WEST, 'East': Directions.EAST}
    startState = problem.getStartState()
    list = util.PriorityQueue()
    visited = set()
    list.push((startState, []),0)

    while not list.isEmpty():
        nextNode = list.pop()
        actualState = nextNode[0]
        direct = nextNode[1]
        cost = 0
        a = 0
        low_h = 0
        low_state = []
        

        if problem.isGoalState(actualState):
            cost = problem.getCostOfActions(direct)
            print "Total cost:" + str(cost)
            return direct
        if actualState not in visited:
            visited.add(actualState)
            for i in problem.getSuccessors(actualState):                
                a=nullHeuristic(i[0],problem)
                if a < low_h:
                    low_h = a
                    low_state = i[0]
            if i[0] not in visited:
                list.push((low_state, direct + [directionTable[i[1]]]),0)
    util.raiseNotDefined()
                





def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
