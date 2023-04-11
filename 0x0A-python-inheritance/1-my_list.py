#!/usr/bin/pyhton
"""Define  a class with its funciton which sort a lis in asecnding order."""


class MayList(list):
    pass

    """a subclass of list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    # defining a function which sort a list

    def print_sorted(self):
        print(self.sort)
