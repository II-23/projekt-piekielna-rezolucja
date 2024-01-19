import pygame
from Scenes import BaseScene

class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
        self.states = {}
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state, args):
        '''If you want to pass arguments to the on_entry() put them in a dict'''
        self.states[self.get_state()].on_exit()
        self.currentState=state
        self.states[self.get_state()].on_entry(args)
