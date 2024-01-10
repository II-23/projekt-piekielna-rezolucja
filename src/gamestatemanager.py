import pygame

class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState=state
