import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']

def build():
    os.system('python setup.py sdist')

def publish():
    os.system('python setup.py sdist upload')

if sys.argv[-1] == 'build':
    build()
    sys.exit()

if sys.argv[-1] == 'publish':
    publish()
    sys.exit()

setup(
    name='racks',
    version='0.0.1',
    description='racks on sacks for stacked graphs',
    url='http://www.github.com/benglass/racks',
    author='Ben Glassman',
    author_email='bglassman@gmail.com',
    install_requires=dependencies,
    packages=['racks'],
    entry_points={
        'console_scripts': [
            'racks=racks.main:main'
        ],
    },
    classifiers={
        'Development Status :: Uh...',
        'Programming Language :: Python'
    }
)
