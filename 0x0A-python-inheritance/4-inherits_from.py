#!/usr/bin/python3
"""Defining sub class chacking """


def inherits_from(obj, a_class):
    """This function defin  whether one class is the sub class of the other object.
    Args : obj(any) the object we want to check.
        a_class(type) the super class of the object we will check.
    Returns :
        True if  the class is the super class of the object class.
        else return false
    """
    if issubclass(obj, a_class):
        return True
    return False
