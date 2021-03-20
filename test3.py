import sys
from itertools import product
from pip._vendor.msgpack.fallback import xrange


width, height = 10, 5
coordinates = list(product(xrange(width), xrange(height)))
coordinates[0] = "Godzilla"
print(coordinates)
