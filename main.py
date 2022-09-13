#!/usr/bin/env python3
"""
Sky implementation for Python
"""
__author__ = "Blazed Labs LLC"
__version__ = "0.0.1"
__license__ = "MIT"

import contract



def main():
    """ Main entry point of the app """
    print("Sky for Python version: " + __version__)
    c = contract.Contract({
      'name': 'Blazed Cash',
      'symbol': 'BLZ'
    })
    c.mintBlock()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
