try:
    from setuptools import setup
except:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']

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
            'racks=racks.main:start'
        ],
    },
    classifiers={
        'Development Status :: Uh...',
        'Programming Language :: Python'
    }
)
