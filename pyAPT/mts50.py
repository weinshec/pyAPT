"""
MTS50 - controller subclass for the Thorlabs MTS50/M-Z8 stage
"""

from .controller import Controller

class MTS50(Controller):
    """
    MTS50 - controller subclass for the Thorlabs MTS50/M-Z8 stage
    """

    def __init__(self,*args, **kwargs):
        """Constructor

        Passes *args, **kwargs to Controller.Constructor
        """

        super(MTS50, self).__init__(*args, **kwargs)
     
        self.max_velocity = 2.2
        self.max_acceleration = 4.0
     
     
        # From Thorlabs APT specification rev.14
        enccnt = 34304
        T = 2048/6e6
        self.position_scale = enccnt
        self.velocity_scale = enccnt * T * 65536
        self.acceleration_scale = enccnt * T * T * 65536
     
        self.linear_range = (0,50)

