#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name', 
                    default='World', help="It's the name of the person you want to greet")
args = parser.parse_args()
print('Hello, ' + args.name + '!')