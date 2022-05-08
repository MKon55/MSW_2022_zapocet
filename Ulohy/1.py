import datetime
import numpy as np


def dotProduct(a, b):
    return sum(x*y for x, y in zip(a, b))


def timeAFunction(func, a, b):
    startTime = datetime.datetime.utcnow()
    result = func(a, b)
    endTime = datetime.datetime.utcnow()
    return result, (endTime - startTime)


def printResult(title, result):
    print(title + ":")
    print("Result:", result[0])
    print("Time taken: ", result[1])


if(__name__ == "__main__"):
    # Dot product
    a = np.random.randint(-1000, 1000, size=2000000)
    b = np.random.randint(-1000, 1000, size=2000000)

    npResult = timeAFunction(np.dot, a, b)
    pureResult = timeAFunction(dotProduct, a, b)

    printResult("numpy", npResult)
    printResult("pure", pureResult)
