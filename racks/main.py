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

def start():
    args = docopt(__doc__, version='1.0')
    print('▁ ▂ ▃ ▅ ▆ ▇')
