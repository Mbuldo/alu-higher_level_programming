#!/usr/bin/python3
"""
    class lockedclass with no class or object instance that prevents,
    the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
"""


class LockedClass:
    """
        empty class
    """
    __slots__ = ["first_name"]
