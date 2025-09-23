import math

print(math.sqrt(30))
print(math.pi)


import random

print(random.randrange(1,200))
print(random.randint(1,200))

from datetime import datetime

print(datetime.now())


# Own module

import helpers

helpers.greetMe("tejas")


import math_utils

print(math_utils.subtract(2,4))