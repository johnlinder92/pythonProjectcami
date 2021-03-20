import sys

x = 0
n = 0
while n != -1:

    for line in sys.stdin:
        if ' ' in line:
            x += 1
            ab = line.split()

            if x == 1:
                a = int(ab[0])
                a2 = int(ab[1])
                break
            if x == 2:
                b = int(ab[0])
                b2 = int(ab[1])
                break
            if x == 3:
                c = int(ab[0])
                c2 = int(ab[1])
                break
            if x == 4:
                d = int(ab[0])
                d2 = int(ab[1])
                break
            if x == 5:
                e = int(ab[0])
                e2 = int(ab[1])
                break
            if x == 6:
                f = int(ab[0])
                f2 = int(ab[1])
                break
            if x == 7:
                g = int(ab[0])
                g2 = int(ab[1])
                break
            if x == 8:
                h = int(ab[0])
                h2 = int(ab[1])
                break
            if x == 9:
                i = int(ab[0])
                i2 = int(ab[1])
                break
            if x == 10:
                j = int(ab[0])
                j2 = int(ab[1])
                break
        else:

            if n == 1:
                distance = (a2 * a)
                print(str(distance) + " miles")
            if n == 2:
                distance = (a2 * a) + ((b2 - a2) * b)
                print(str(distance) + " miles")
            if n == 3:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c)
                print(str(distance) + " miles")
            if n == 4:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d)
                print(str(distance) + " miles")
            if n == 5:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e)
                print(str(distance) + " miles")
            if n == 6:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e) + (
                            (f2 - e2) * f)
                print(str(distance) + " miles")
            if n == 7:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e) + (
                            (f2 - e2) * f) + (
                                   (g2 - f2) * g)
                print(str(distance) + " miles")
            if n == 8:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e) + (
                            (f2 - e2) * f) + (
                                   (g2 - f2) * g) + ((h2 - g2) * h)
                print(str(distance) + " miles")
            if n == 9:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e) + (
                            (f2 - e2) * f) + (
                                   (g2 - f2) * g) + ((h2 - g2) * h) + ((i2 - h2) * i)
                print(str(distance) + " miles")
            if n == 10:
                distance = (a2 * a) + ((b2 - a2) * b) + ((c2 - b2) * c) + ((d2 - c2) * d) + ((e2 - d2) * e) + (
                            (f2 - e2) * f) + (
                                   (g2 - f2) * g) + ((h2 - g2) * h) + ((i2 - h2) * i) + ((j2 - i2) * j)
                print(str(distance) + " miles")
            x = 0
            n = int(line)
            break
