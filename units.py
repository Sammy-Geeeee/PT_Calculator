# This is to define a class containing all of the units

class Units():
    def __init__(self):
        self.mass = ['kg', 'mg', 'g', 'T', 'oz', 'lb', 'st']
        self.time = ['s', 'ms', 'min', 'hr']
        self.distance = ['m', 'mm', 'cm', 'km', 'in', 'ft', 'yd', 'mi']
        self.linear_speed = ['m/s', 'm/min', 'mm/s', 'mm/min', 'km/hr', 'ft/s', 'mi/hr']
        self.rotational_speed = ['rad/s', 'rad/min', 'deg/s', 'deg/min', 'rev/s', 'rev/min', 'rev/hr']
        self.linear_acceleration = ['m/s/s', 'm/s/min', 'km/hr/s', 'km/hr/min', 'km/hr/hr', 'ft/s/s', 'ft/s/min', 'mi/hr/s', 'mi/hr/min', 'mi/hr/hr']
        self.force = ['N', 'kN', 'kg.f', 'T.f', 'lb.f']
        self.torque = ['N.m', 'kN.m', 'kg.f.m', 'lb.f.ft']
        self.power = ['W', 'kW', 'hp']
