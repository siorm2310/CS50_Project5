import math
import numpy as np


class VectorProperty():
    def __init__(self,first_property,second_property,is_polar=False):
        if not is_polar:
            self.x = first_property
            self.y = second_property
            self.magnitude = math.sqrt((self.x)**2 + (self.y)**2)

            if abs(self.x) < 1e-5:
                self.arg = math.pi / 2
            else:
                self.arg = math.tan(self.y/self.x)
        else:
            self.magnitude = first_property
            self.arg = second_property
            self.x = self.magnitude * math.cos(self.arg)
            self.y = self.magnitude * math.sin(self.arg)

    def validate_location(self):
        if self.y >= 0 and self.magnitude > 1e-5:
            return True
        return False

class BallisticThrow():

    g = 9.81

    def __init__(self,x_position,y_position,velocity,angle):
        self.location = VectorProperty(x_position,y_position)
        self.velocity = VectorProperty(velocity,angle,is_polar=True)

    def calc_landing(self):
        v = self.velocity.magnitude
        theta = self.velocity.arg
        h = self.location.x
        t_tof = (1/self.g) * (v * math.sin(theta) + math.sqrt(v * (math.sin(theta))**2) + 2 * self.g * h) # Time of flight
        range_flight = self.location.x + self.velocity.x * t_tof
        h_max = h + v**2 * (math.sin(theta))**2 / (2 * self.g)
        return {
            "Time" : t_tof,
            "MaxRange" : range_flight,
            "MaxHeight" : h_max
        }

    def create_datapoints(self):
        pass

