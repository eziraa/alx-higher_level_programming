#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This function defin  whether one class is the sub class of the other object.

    Args :
        obj(any): the object we want to check.
        a_class(type): the super class of the object we will check.
    Returns :
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
