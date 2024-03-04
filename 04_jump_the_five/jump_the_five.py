#!/usr/bin/env python3
"""
Author : jim <jim@localhost>
Date   : 2024-03-04
Purpose: Jump the five - Encode numbers base on the wire code
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode numbers from a text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='A sentence, if it contains number will come out encoded')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text

    #let's define a dictionnary containing the code :
    dict = {'1':"9",'2':"8",'3':"7",'4':"6",'5':"0",'6':"4",'7':"3",'8':"2",'9':"1",'0':"5"}
#    sentence = ''
#    for char in str_arg:
#        if char in dict:
#            sentence = sentence + dict[char]
#        else:
#            sentence = sentence + char
    for char in args.text:
        print(dict.get(char, char), end='')
    print()

#    print(f'{sentence}')




# --------------------------------------------------
if __name__ == '__main__':
    main()
