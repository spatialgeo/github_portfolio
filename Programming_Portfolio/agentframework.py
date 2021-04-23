import random

#agent framework
      
class Agent():
    def __init__ (self, environment, agents):
        self._x = random.randint (0,99)
        self._y = random.randint (0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def __str__(self):
        return "x=" + str(self._x) + ", y=" + str(self._y) + ", Store=" + str(self.store)
        
    #@property
    def move(self):
        
        '''
        This moves the x and y variables for the agent either by + 1 or -1, depending on if the random value is < 0.5 or not. 
        It then repeats for the second movement.

        Returns
        -------
        None.

        '''
        if random.random() < 0.5:
            self.y = (self._y + 1) % 100
        else:
            self.y = (self._y - 1) % 100

        if random.random() < 0.5:
            self.x = (self._x + 1) % 100
        else:
            self.x = (self._x - 1) % 100
        #x = property
        
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10.

            
