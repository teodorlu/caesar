#! /usr/bin/env python3

import fileinput

def addcounter(charusage, letter):
    if letter in charusage:
        charusage[letter] = charusage[letter] + 1
    else:
        charusage[letter] = 1

def printusage(usagetups, fractions):
    usagetups.sort(key=lambda tup: tup[1], reverse=True)
    for k, v in usagetups:
        print("{0:5d} ({1:.2f} %): {2}".format(v, fractions[k], k))

def mkpercents(charusage):
    total = sum(charusage.values())
    percents = {}
    for letter, count in charusage.items():
        fraction = count / total * 100.0
        percents[letter] = fraction
    return percents

def main():
    charusage = {}
    for line in fileinput.input():
        for letter in line:
            if letter is not "\n":
                addcounter(charusage, letter)

    fractions = mkpercents(charusage)
    printusage(list(charusage.items()), fractions)

if __name__ == '__main__':
    main()
