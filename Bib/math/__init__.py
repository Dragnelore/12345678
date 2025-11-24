from .kids.add import add
from .kids.fact import factorial
from .kids.mean import mean

OPERATIONS = {
    "fa": factorial,
    "avg": mean,
    "add": add
}



__version__ = "1.0.0"
__author__ = "ARS"
__license__ = "MIT"