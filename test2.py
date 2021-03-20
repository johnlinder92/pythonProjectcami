import sys

counter = 0
while counter != 5:

    try:

        for line in sys.stdin:
            counter += 1
            ab = line.split()
            i = len(ab)

            values = {}
            for X in range(0, i):
                values['val{0}'.format(X)] = ab[X]

            for X in range(1, i):

                try:
                    newvalue = 0
                    operatorinput = str(values.get('val{0}'.format(X - 1)))
                    firstvalue = int(values.get('val{0}'.format(X)))
                    lastvalue = int(values.get('val{0}'.format(X + 1)))
                    if firstvalue == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or -1 or -2 or -3 or -4 or -5 or -6 or -7 or -8 or -9 or -10 and lastvalue == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or -1 or -2 or -3 or -4 or -5 or -6 or -7 or -8 or -9 or -10 and operatorinput == '-' or '+' or '*':

                        if operatorinput == '+':
                            newvalue = int(firstvalue) + int(lastvalue)
                            values.update({('val{0}'.format(X + 1)): newvalue})
                            values.pop('val{0}'.format(X - 1))
                            values.pop('val{0}'.format(X))
                        elif operatorinput == "-":
                            newvalue = int(firstvalue) - int(lastvalue)
                            values.update({('val{0}'.format(X + 1)): newvalue})
                            values.pop('val{0}'.format(X - 1))
                            values.pop('val{0}'.format(X))
                        elif operatorinput == "*":
                            newvalue = int(firstvalue) * int(lastvalue)
                            values.update({('val{0}'.format(X + 1)): newvalue})
                            values.pop('val{0}'.format(X - 1))
                            values.pop('val{0}'.format(X))


                    def stringify(A):
                        return (A)


                    result = map(stringify, (values.values()))
                    listresult = list(result)
                    realresult = ' '.join(map(str, listresult))


                except:

                    def stringify(A):
                        return (A)


                    result = map(stringify, (values.values()))
                    listresult = list(result)
                    realresult = ' '.join(map(str, listresult))

            print("Case " + str(counter) + ": " + realresult)
            if counter == 5:
                exit()
            values.clear()
            del listresult
            realresult = ''
    except:
        realresult = ''
        if counter == 1:
            print("Case " + str(counter) + ": " + realresult)
