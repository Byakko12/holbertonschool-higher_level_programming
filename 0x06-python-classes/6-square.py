#!/usr/bin/python3
'''class square'''


class Square:
    '''define Square'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) or len(value) != 2 \
            or not isinstance(value[0], int) or not isinstance(value[1], int) \
                or isinstance(value[0]) < 0 or isinstance(value[1]) < 0:
            raise TypeError("sposition must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print('_' * self.position[0], end="")
                print('#' * self.size)
