#!/usr/bin/python3
"""4-square module

This module defines a square based on 3-square.py by:
- Private instance attribute: size where:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
      - size must be an integer, otherwise raise a TypeError exception message:
         'size must be an integer'
      - if size less than 0, raise a ValueError exception with the message:
         'size must be >= 0'

- Instantiation with optional size: def __init__(self, size=0):

- Public instance method: def area(self): that returns the current square area

- without importing any module

"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size
        """__init__ method

        This method initializes the size argument and checks if:
        - size is < 0
        - size is not an integer

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """area method

        This method returns the current square area

        """
        area = self.__size
        return area*area

    @property
    def size(self):
        """size method

        This is used to retrieve the property of size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size.setter method

        This method is used to set the size value of the square object

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
