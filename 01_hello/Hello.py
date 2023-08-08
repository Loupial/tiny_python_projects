#!/usr/bin/env python
# Purpose: Say Hello

import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('name', help="It's the name of the person you want to greet")
args = parser.parse_args()
print('Hello, ' + args.name + ' !')