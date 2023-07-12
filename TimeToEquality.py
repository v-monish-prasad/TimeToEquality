def timeToEquality(array):
    if not array:
        return "Empty Array."

    maximum = array[0]
    changes = 0
    totalTime = 0

    for i in range(1, len(array)):
        if array[i] >= maximum:
            maximum = array[i]

    for i in range(len(array)):
        if array[i] < maximum:
            totalTime += maximum - array[i]

    return totalTime


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(timeToEquality(array))
