"""judge0api - A Python API for interacting with the Judge0"""


from . import language, submission
from .client import Client
from .status import Judge0Status

__version__ = '0.1.17'
__author__ = 'Aaron Walker <aaw13@aber.ac.uk>'
__all__ = ['client', 'submission', 'language', 'Judge0Status']

if __name__ == '__main__':
    pass
