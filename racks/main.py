#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Racks.

Usage:
    racks <numbers>...

Examples:
    racks 1 25 221 57 32 68 8

Options:
    -h --help     Show this screen.
    -v --version  Show version.
"""
from docopt import docopt
from termcolor import colored, cprint

steps = u'▁▂▃▄▅▆▇'

def normalize_numbers(numbers):
    """
    Given a list of numbers, normalize the given numbers to 0-6 to allow each number to account for the number of different unicode
    blocks we have to represent them.
    """
    step_range = max(numbers) - min(numbers)
    step = ((step_range) / float(6)) or 1
    rack = u''.join(steps[int(round((n - min(numbers)) / step))] for n in numbers)
    cprint(rack, 'green')

def main():
    args = docopt(__doc__, version='1.0')
    numbers = args.get('<numbers>', None)
    if numbers:
        try:
            numbers = map(int, numbers)
            normalize_numbers(numbers)
        except ValueError:
            cprint('Racks only accepts integers', 'red')
    # print(args)
    # print('▁ ▂ ▃ ▅ ▆ ▇')
