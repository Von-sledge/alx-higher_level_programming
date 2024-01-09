#!/usr/bin/python3

"""Create a function that returns TRUE if the object is exactly an instance\n
of the specified class, otherwise FALSE."""


def is_same_class(obj, a_class):
    """Create a function that validates if an object is exactly\
       an instance of the specified class."""

       return (type(obj) == a_class)
    
