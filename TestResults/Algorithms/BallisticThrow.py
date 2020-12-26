import math
import numpy as np

g = 9.81

class VectorProperty():
    def __init__(self,x_property,y_property):
        self.x = x_property
        self.y = y_property
        self.length = math.sqrt((self.x)**2 + (self.y)**2)
        self.arg = math.tan(self.y/self.x)

    def validate_location(self):
        if self.y >= 0 and self.length > 1e-5:
            return True
        return False

class InitialConditions():
    def __init__(self,x_position,y_position,x_velocity,y_velocity):
        self.location = VectorProperty(x_position,y_position)
        self.velocity = VectorProperty(x_velocity,y_velocity)

    def calc_landing(self):
        v = self.velocity.length
        theta = self.velocity.arg
        h = self.location.x
        t_tof = (1/g) * (v * math.sin(theta) + math.sqrt(v * (math.sin(theta))**2) + 2 * g * h) # Time of flight
        range_flight = self.location.x + self.velocity.x * t_tof
        h_max = h + v**2 * (math.sin(theta))**2 / (2 * g)
        return {
            "Time of Flight [s]" : t_tof,
            "Range of Flight [m]" : range_flight,
            "Maximum Height [m]" : h_max
        }

    def create_datapoints(self):
        pass

