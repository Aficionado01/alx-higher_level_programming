#!/usr/bin/python3
"""This module has a function that checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Function returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise False
    Args:
        obj: the object to check
        a_class: the class or subclass to check against
    """

    return True if isinstance(obj, a_class) else False
