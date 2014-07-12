#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Racks.

Usage:
    racks rand [--count=<count>] [--min=<min>] [--max=<max>] [--delay=<ms>]
    racks <numbers>...

Examples:
    racks 1 25 221 57 32 68 8

Options:
    -h --help           Show this screen.
    -v --version        Show version.
    -c --count=<count>  Number of numbers to generate [default: 10]
    -n --min=<min>      Minimum number [default: 1]
    -x --max=<max>      Max number [default: 100]
    -d --delay=<ms>     Delay for animation in ms
"""
from docopt import docopt
from termcolor import colored, cprint
from random import randint
import time
import os

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

def randomize_numbers(count, min, max):
    numbers = [ randint(min, max) for x in range(count) ]
    return numbers

def animate_numbers(count, min, max, delay):
    numbers = randomize_numbers(count, min, max)
    normalize_numbers(numbers)
    time.sleep(delay / float(1000))
    os.system('clear')
    animate_numbers(count, min, max, delay)

def main():
    args = docopt(__doc__, version='1.0')
    numbers = args.get('<numbers>', None)
    rand = args.get('rand', False)
    if rand:
        ncount = int(args.get('--count'))
        nmin = int(args.get('--min'))
        nmax = int(args.get('--max'))
        delay = args.get('--delay')
        if not delay:
            numbers = randomize_numbers(ncount, nmin, nmax)
            normalize_numbers(numbers)
        else:
            animate_numbers(ncount, nmin, nmax, int(delay))
    elif numbers:
        try:
            numbers = map(int, numbers)
            normalize_numbers(numbers)
        except ValueError:
            cprint('Racks only accepts integers', 'red')
