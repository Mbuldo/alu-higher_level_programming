#!/usr/bin/python3
"""
    def class 'MyList'
"""


class MyList(list):
    """
        sorted list
    """

    def print_sorted(self):
        """
            print sorted list
        """
        print(sorted(self))