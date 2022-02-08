#!/usr/bin/python3
"""Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init atributtes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading square"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update data"""
        data_args = ['id', 'width', 'height', 'x', 'y']

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for i in range(len(args)):
            if hasattr(self, data_args[i]):
                setattr(self, data_args[i], args[i])
