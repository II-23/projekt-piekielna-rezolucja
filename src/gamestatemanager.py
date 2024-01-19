import pygame
from Scenes import BaseScene

class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
        self.new_state = None
        self.args = None
        self.states = {}
        
    def get_state(self):
        return self.currentState
    
    def transition_to_new_state(self):
        '''if last scene finished its on_exit method it switches to a new scene'''
        if not self.states[self.get_state()].pause and self.new_state: 
            self.currentState=self.new_state
            self.states[self.get_state()].on_entry(self.args)
            self.new_state = None
            self.args = None
            
    def set_state(self, state, args):
        '''If you want to pass arguments to the on_entry() put them in a dict'''
        self.states[self.get_state()].on_exit() # calls on_exit method and waits untill it finishes (pause == False)
        self.new_state = state
        self.args = args
