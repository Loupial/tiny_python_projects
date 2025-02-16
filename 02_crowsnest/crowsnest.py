#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2023-10-24
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.word
    article = 'an' if pos_arg[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {pos_arg} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
