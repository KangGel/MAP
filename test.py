def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        def getGhostStates():
          return currentGameState.getGhostStates()
        def getScaretime():
          ret = []
          for item in currentGhostStates:
            ret.append(item.scaredTimer)
          return ret
        def getGhostPositions():
          return successorGameState.getGhostPositions()
        def getGhostPositions():
          return currentGameState.getGhostPositions()

        def helper(sumGhostDistances,foodList,foodDistance,ghostAround,scoreDifference,additionalFactor):

            for i in range(0, len(newGhostPositions)):
                ghostDistance = util.manhattanDistance(newGhostPositions[i], newPos)
                sumGhostDistances += [ghostDistance]
                if newScaredTimes[i] == 0 and ghostDistance < 4:
                    ghostAround = True

            if action == Directions.STOP:
                additionalFactor -= 5
        
            if currentScaredTimes.count(0) < newScaredTimes.count(0):
                additionalFactor += 5
        
            if ghostAround:
                return additionalFactor + min(sumGhostDistances) + scoreDifference
        
            if len(foodList) > 0:
                distance, closestFood = min([(util.manhattanDistance(newPos, food), food) for food in foodList])
                if distance == 0:
                    foodDistance = 10 
                else:
                    foodDistance = - distance
        
            if currentGameState.getNumFood() > successorGameState.getNumFood():
                additionalFactor += 100
        
            return foodDistance + scoreDifference + additionalFactor

        currentGhostStates = getGhostStates()
        currentScaredTimes = getScaretime()
        newGhostPositions = getGhostPositions()
        currentGhostPositions = getGhostPositions()
        Difference = successorGameState.getScore() - currentGameState.getScore()
        return helper([],newFood.asList(),0,False,Difference,0)