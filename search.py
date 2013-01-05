# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
import searchAgents
findGoal = False
visited = []


class Node:
	# This class is designe for getting the previous node of the current node.
	def __init__(self, state):
		"""
			state: the state of the current node
		"""
		self.state = state
		self.prevNode = None

	def setParent(self, node):
		self.prevNode = node

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
	 """
	 Returns the start state for the search problem 
	 """
	 util.raiseNotDefined()
  
  def isGoalState(self, state):
	 """
	   state: Search state
	
	 Returns True if and only if the state is a valid goal state
	 """
	 util.raiseNotDefined()

  def getSuccessors(self, state):
	 """
	   state: Search state
	 
	 For a given state, this should return a list of triples, 
	 (successor, action, stepCost), where 'successor' is a 
	 successor to the current state, 'action' is the action
	 required to get there, and 'stepCost' is the incremental 
	 cost of expanding to that successor
	 """
	 util.raiseNotDefined()

  def getCostOfActions(self, actions):
	 """
	  actions: A list of actions to take
 
	 This method returns the total cost of a particular sequence of actions.  The sequence must
	 be composed of legal moves
	 """
	 util.raiseNotDefined()
		   

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", pro
  blem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  visited = []
  stack = util.Stack()
  listOfActions = []
  state = problem.getStartState()
  node = Node(state)
  stack.push(node)
  while True:
  	if stack.isEmpty():
  		return None
  	node = stack.pop()
  	state = node.state
  	if state == problem.getStartState():
  		coordinate = state
  	else:
  		coordinate = state[0]
  	if problem.isGoalState(coordinate):

  		# Generate path here
  		path = BFS_generatePath(node, problem)
  		print path
  		return path
  	if not coordinate in visited:
  		visited.append(coordinate)
  		for successor in problem.getSuccessors(coordinate):
  			# print successor
  			successorNode = Node(successor)
  			stack.push(successorNode)
  			successorNode.setParent(node)



 

# Convert list of states into list of directions

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  initState = problem.getStartState()
  visited = []
  queue = util.Queue()
  finalNode = BFS(problem, initState, queue)
  # print "getResult"
  print "breadthFirstSearch is calledcl"
  result = BFS_generatePath(finalNode, problem)
  print result
  return result


def BFS(problem, state, queue):
	startNode = Node(state)
	queue.push(startNode)
	while not queue.isEmpty():
		currentNode = queue.pop()
		visited.append(currentNode.state[0])
		value = currentNode.state
		if value == problem.getStartState():
			v = value
		else:
			v = value[0]
		if problem.isGoalState(v):
			return currentNode
		for node in problem.getSuccessors(v):
			successorNode = Node(node)
			successorNode.setParent(currentNode)
			if not node[0] in visited:
				visited.append(node[0])
				if problem.isGoalState(node[0]):
					return successorNode
				else:
					queue.push(successorNode)

# Generate path.
def BFS_generatePath(node, problem):
	path = util.Stack()
	# print "Generate path here"
	# print "The node state is", node.state
	while not node == None:
		state = node.state
		# print "The node state is ", node.state
		# print state
		action = state[1]
		path.push(state)
		node = node.prevNode
	# Reverse the order
	result = util.Queue()
	for i in path.list:
		result.push(i[1])
	# print "result is", result.list
	if not len(result.list) == 0:
		result.list.remove(result.list[0])
	# print result.list
	return result.list

def printQueue(queue):
	result = []
	for i in queue.list:
		result.append(i.state[0])
	print result

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"

  # Initialization
  initState = problem.getStartState()
  startNode = Node(initState)
  frontier = util.PriorityQueue()
  frontier.push(startNode, 0)
  visited = []


  while not frontier.isEmpty():
	currentNode = frontier.pop()
	state = currentNode.state
	if state == problem.getStartState():
		value = state
	else:
		value = state[0]

	if problem.isGoalState(value):
		return BFS_generatePath(currentNode, problem)

	for node in problem.getSuccessors(value):
		if not node[0] in visited:
			visited.append(node[0])
			successorNode = Node(node)
			successorNode.setParent(currentNode)
			(exsiting, index) = checkIfStateExisting(frontier, node)
			if not exsiting:
				# Return if goal
				if problem.isGoalState(node[0]):
					return BFS_generatePath(successorNode, problem)
				# Push the successor node into priority queue
				cost = successorNode.state[2]
				frontier.push(successorNode, accumulativeCost(successorNode, problem)) 
			else:
				(priority, item) = frontier.heap[index]
				if priority > node[2]:
					#Replace the existing node with current node
					frontier.heap[index] = (node[2], successorNode)
					successorNode.setParent(item.prevNode)


# If true, return True and the index
def checkIfStateExisting(frontier, state):
	for n in range(len(frontier.heap)):
		(priority, item) = frontier.heap[n]
		if item.state[0] == state[0]:
			return (True, n)
	return (False, 0)


# Get the accumulative cost from the starting node to the current node
def accumulativeCost(node, problem):
	totalCost = 0
	while not node is None:
		if node.state == problem.getStartState():
			cost = 1
		else:
			cost = node.state[2]
		totalCost = totalCost + cost
		node = node.prevNode
	return totalCost

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0


def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  # Initialization
  initState = problem.getStartState()
  startNode = Node(initState)
  frontier = util.PriorityQueue()
  frontier.push(startNode, 0)
  visited = []


  while not frontier.isEmpty():
	currentNode = frontier.pop()
	# if currentNode.state == problem.getStartState():
	#     v = currentNode.state
	# else:
	#     v = currentNode.state[0]
	state = currentNode.state
	# To get the correct coordinate
	if state == problem.getStartState():
		value = state
	else:
		value = state[0]

	# Return if goalState
	if problem.isGoalState(value):
		return BFS_generatePath(currentNode, problem)

	for node in problem.getSuccessors(value):
		if not node[0] in visited:
			visited.append(node[0])
			successorNode = Node(node)
			successorNode.setParent(currentNode)
			(exsiting, index) = checkIfStateExisting(frontier, node)
			if not exsiting:
				# Return if goal
				if problem.isGoalState(node[0]):
					return BFS_generatePath(successorNode, problem)
				# Push the successor node into priority queue
				cost = successorNode.state[2]
				frontier.push(successorNode, accumulativeCost(successorNode, problem) + heuristic(successorNode.state[0], problem)) 
			else:
				(priority, item) = frontier.heap[index]
				if priority > node[2]:
					#Replace the existing node with current node
					frontier.heap[index] = (node[2], successorNode)
					successorNode.setParent(item.prevNode)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
