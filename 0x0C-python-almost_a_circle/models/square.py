#!/usr/bin/python3
"""Square"""


from tarfile import RECORDSIZE
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init atributtes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading square"""
        return ("[Square] {:d} {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))
    