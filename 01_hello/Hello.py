#!/usr/bin/env python3
"""
Author: It's a me, MARIOOOOOOOOOOOO
Purpose: Say hello
"""

import argparse

"-----------------------------------------------------------------------------------------"
def get_args():
    """
    Get the command-line arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World',
                        help="It's the name of the person you want to greet")
    return parser.parse_args()


"-----------------------------------------------------------------------------------------"
def main():
    """
    Main program
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


"-----------------------------------------------------------------------------------------"
if __name__ == '__main__':
    main()
