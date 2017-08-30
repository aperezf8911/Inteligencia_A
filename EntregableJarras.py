# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 04:14:23 2017

@author: Alex
"""
import sys
sys.path
sys.path.append("C:/Users/Alex/Desktop/IA/")

# Support libraries from EDx CS188
import util
import search

# Libraries and code for graph and tree visualization
from graphviz import Graph, Digraph
from IPython.display import display


class jars_problem(search.SearchProblem):
    def __init__(self, cap_1, cap_2, goal):
        '''
        cap_1: jar 1 capacity
        cap_2: jar 2 capacity
        goal:  goal state
        '''
        cap_1=5
        cap_2=4
        self.cap_1 = cap_1
        self.cap_2 = cap_2
        self.start = (0, 0)
        self.goal = goal
        
    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return self.goal == state
    
    def actions(self, state):
        actions = ['llenarJ1', 'llenarJ2', 'verterJ1enJ2', 'verterJ2enJ1', 'vaciarJ1', 'vaciarJ2']
        return actions

    def getSuccessors(self, state):
        
        if action is 'llenarJ1':
            j1 = self.capacidadJ1
            state = ('J1', j1, 'J2', state[4])
            return state

        elif action is 'llenarJ2':
            j2 = self.capacidadJ2
            state = ('J1', state[1], 'J2', j2)
            return state
        
        elif action is 'verterJ1enJ2':
            cantidadJ1 = state[1]
            cantidadJ2 = state[4]
            j1 = 0
            j2 = 0
            deltaJ2 = self.capacidadJ2 - cantidadJ2

            if deltaJ2 > 0:

                if cantidadJ1 >= deltaJ2:
                    quedaEnJ1 = cantidadJ1 - deltaJ2
                    cantidadADepositar = cantidadJ1 - quedaEnJ1
                    j2 = cantidadJ2 + cantidadADepositar
                    j1 = quedaEnJ1
                else:
                    j2 = cantidadJ1 + cantidadJ2
                    j1 = 0

                state = ('J1', j1, 'J2', j2)
                return state
            return state

        elif action is 'verterJ2enJ1':
            cantidadJ1 = state[1]
            cantidadJ2 = state[4]
            j1 = 0
            j2 = 0

            deltaJ1 = self.capacidadJ1 - cantidadJ1

            if deltaJ1 > 0:

                if cantidadJ2 > deltaJ1:
                    quedaEnJ2 = cantidadJ2 - deltaJ1
                    cantidadADepositar = cantidadJ2 - quedaEnJ2
                    j1 = cantidadJ1 + cantidadADepositar
                    j2 = quedaEnJ2
                else:
                    j1 = cantidadJ2 + cantidadJ1
                    j2 = 0

                state = ('J1', j1, 'J2', j2)
                return state

            return state

        elif action is 'vaciarJ1':
            j1 = 0
            state = ('J1', j1, 'J2', state[3])
            return state

        elif action is 'vaciarJ2':
            j2 = 0
            state = ('J1', state[1], 'J2', j2)
            return state

        
        '''
        Receives a state and calculates the list of successors. Each successor 
        correspond a triple of the form (state, action, cost). 
        For instance for state = (0, 0) the list of successors could be:
        [((5, 0), "Fill 1", 5), ((0, 4), "Fill 2", 4)]
        '''
        # Your code here
        return successors
    
    
    problem = jars_problem(5, 4, (0,2))
    actions = dfs(problem)
    print actions