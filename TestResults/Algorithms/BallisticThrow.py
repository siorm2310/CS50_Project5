import math
import numpy as np
class VectorProperty():
    """
    docstring
    """
    def __init__(self,x_property,y_property):
        self.x = x_property
        self.y = y_property
        self.length = math.sqrt((self.x)**2 + (self.y)**2)
        self.arg = math.tan(self.y/self.x)


class InitialConditions(VectorProperty):
    pass



def calc_landing_properies(initial_conditions):
    """
    docstring
    """
    t_landing = 0