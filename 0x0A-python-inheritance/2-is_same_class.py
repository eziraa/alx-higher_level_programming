#!/usr/bin/python3
"""Defing a function thst check weather or object is instance of the the given class"""


def is_same_class(obj, a_class):
    """Chceck is the object is the instance of the given class
    Args : 
        obj (any) which is an object that can be tested
        a_class(type) is the given class indication
    Returns:
        Ture if the object is instance of the  given class  or false if not.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
