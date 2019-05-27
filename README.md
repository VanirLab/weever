# weever
An Experimental Framework for Data Hiding 

weever is an experimental toolkit for filesystem based data hiding techniques, implemented in Python. It collects various common exploitation methods, that make use of existing datastructures on the filesystem layer, for hiding data from conventional file access methods. This toolkit is intended to introduce people to the concept of established anti-forensic methods associated with data hiding.


## Requirements
Build:
Python version 3.5 or higher
argparse - command line argument parsing
construct - parsing FAT filesystems
pytsk3 - parsing NTFS filesystems
simple-crypt - encryption of metadata using AES-CTR
Testing
pytest - unit test framework
mount and dd - unix tools. needed for test image generation
Documentation
sphinx - generates the documentation
sphinx-argparse - cli parameter documentation
graphviz - unix tool. generates graphs, used in the documentation

## Installation

# To run unit tests before installing
$ sudo python setup.py test

# Install the program
$ sudo python setup.py install

# Create documentation
$ pip install sphinx sphinx-argparse
$ python setup.py doc
To generate the documentation as pdf:

$ cd doc
$ make latexpdf
You may have to install some extra latex dependencies:

$ sudo apt-get install latexmk
$ sudo apt-get install texlive-formats-extra
