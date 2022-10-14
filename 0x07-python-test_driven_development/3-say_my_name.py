#!/usr/bin/python3
"""
This module has one function that print first name and last name
"""


def say_my_name(first_name, last_name=""):
    """Return the first name and last name
    Args:
        first_name: first argument
        last_name: second argument
    Returns:
        Print arguments
    Raises:
        TypeError: If either of the arguments is not a string
    """
    if ((not isinstance(first_name, str))):
        raise TypeError("first name must be a string")
    if ((not isinstance(last_name, str) )):
        raise TypeError("last name must be a string")
    return "My name is {} {}".format(first_name, last_name)
