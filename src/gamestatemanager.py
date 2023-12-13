class BaseScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def process_input(self, events, pressed_keys):
        pass
    def update(self):
        pass
    def render(self):
        self.display.fill('blue')

class Start(BaseScene):
    def __init__(self, display, gameStateManager):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager)
    def render(self):
        self.display.fill('red')
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState=state
