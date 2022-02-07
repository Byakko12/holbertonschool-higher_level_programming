#!/ur/bin/python3
"""class Base"""


class Base:
    """contructor of class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init atributte"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
