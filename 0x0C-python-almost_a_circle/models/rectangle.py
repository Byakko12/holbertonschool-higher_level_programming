#!/usr/bin/python3
"""Rectangle"""


from models.base import Base


class Rectangle (Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init atributte"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """widht setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area of rectangle"""
        return self.height * self.width

    def display(self):
        """display rectangle with height, width, x, y"""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """return data"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """update data"""
        data_args = ['id', 'width', 'height', 'x', 'y']

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for i in range(len(args)):
            if hasattr(self, data_args[i]):
                setattr(self, data_args[i], args[i])

    def to_dictionary(self):
        """to dictionary"""
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
