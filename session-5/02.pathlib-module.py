# Import EVERYTHING from math
import math

# ---------------------

# Import only factorial() from math
from math import factorial

# ---------------------

# Import only different functions WITH ALIAS from math
from math import factorial as fact, cos as cosinous, sin as sinous
print(sinous(fact(100)))

# ---------------------
# ---------------------
# ---------------------

print(dir(math))


# file is a magic variable
print(__file__)


# show all magic variables:
print(dir())


# __ is called "daander (dunder)"
print('dunder name:', __name__)


from pathlib import Path
address = Path(__file__)
address = address.parent.parent.joinPath('folder').joinPath('file.txt')