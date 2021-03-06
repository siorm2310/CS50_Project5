import math
import numpy as np


class VectorProperty():
    def __init__(self, first_property, second_property, is_polar=False):
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

    def __init__(self, x_position, y_position, velocity, angle):
        self.location = VectorProperty(x_position, y_position)
        self.velocity = VectorProperty(velocity, angle, is_polar=True)

    def calc_landing(self):
        v = self.velocity.magnitude
        theta = self.velocity.arg
        h = self.location.y
        t_tof = (1/self.g) * (v * math.sin(theta) + math.sqrt((v *
                                                               math.sin(theta))**2 + 2 * self.g * h))  # Time of flight
        range_flight = self.location.x + self.velocity.x * t_tof
        h_max = h + v**2 * (math.sin(theta))**2 / (2 * self.g)
        return {
            "Time": round(t_tof,ndigits=2),
            "MaxRange": round(range_flight,ndigits=2),
            "MaxHeight":round(h_max,ndigits=2) 
        }

    def create_datapoints(self, tof_dict):
        t = np.linspace(0, tof_dict["Time"], num=20)
        x = []
        y = []

        for timestep in t:
            xstep = self.location.x + self.velocity.x * timestep
            ystep = self.location.y + self.velocity.y * timestep - 0.5 * self.g * timestep ** 2

            x.append(round(xstep,ndigits=3))
            y.append(round(ystep,ndigits=3))

        return {
            "t": t.tolist(),
            "x": x,
            "y": y,
        }

    def get_data(self):

        solution = self.calc_landing()
        datapoints = self.create_datapoints(solution)
        solution.update(datapoints)
        return solution
