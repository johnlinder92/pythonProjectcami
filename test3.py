import sys
from itertools import product
from pip._vendor.msgpack.fallback import xrange


width, height = 10, 5
coordinates = list(product(xrange(width), xrange(height)))
coordinates[0] = "Godzilla"
print(coordinates)

#second
counter = 0
for line in sys.stdin:
    counter += 1
    ab = line.split()
    itemsCount = len(ab)
    finalExpression = []
    nextCounter = 0
    for index in range(len(ab)):
        if (index == nextCounter):

            item = ab[index]
            if item in ['+', '-', '*'] and index <= (itemsCount - 3):
                if ab[index + 1].isnumeric() and ab[index + 2].isnumeric() and int(ab[index + 1]) in range(-10,
                                                                                                           10) and int(
                        ab[index + 2]) in range(-10, 10):
                    result = 0
                    if (item == '+'):
                        result = int(ab[index + 1]) + int(ab[index + 2])
                    elif (item == '-'):
                        result = int(ab[index + 1]) - int(ab[index + 2])
                    else:
                        result = int(ab[index + 1]) * int(ab[index + 2])

                    finalExpression.append(result)
                    nextCounter += 3
                else:
                    finalExpression.append(item)
                    nextCounter += 1
            else:
                finalExpression.append(item)
                nextCounter += 1

    print("Case " + str(counter) + ": " + ' '.join(map(str, finalExpression)))