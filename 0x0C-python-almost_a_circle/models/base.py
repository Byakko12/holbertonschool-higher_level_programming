#!/ur/bin/python3
"""class Base"""


class Base:
    __nb_objects = 0
    """contructor of class"""

    def __init__(self, id=None):
        """init atributte"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
