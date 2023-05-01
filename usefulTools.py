import random

feetInMile = 5280
metersInKilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harisson", "Ringo Star"]


def fileGetExt(filename):
    return filename[filename.index(".") + 1]


def rollDice(num):
    return random.randint(1, num)
