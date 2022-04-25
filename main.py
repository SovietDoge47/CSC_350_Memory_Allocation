import random

# Initializing physical memory list as global variable
memoryListSize = 64
memoryList = [memoryListSize]
for x in range(1, memoryListSize):
    memoryList.append(0)
# Initializing other global variables
bestFitSimulation = True
notFull = True
averageTotalUtilization = 0
searchTime = 0
count = 0


def main():
    global memoryList
    global averageTotalUtilization

    if bestFitSimulation:
        for i in range(0, 50):
            while notFull:
                size = random.randint(1, 8)
                memoryList = Best_Fit(memoryList, size)
            currentUtilization = Memory_Utilization(memoryList)
            print(currentUtilization)
            memoryList = Release(memoryList)
            averageUtilization = currentUtilization / 50
            averageTotalUtilization = averageTotalUtilization + averageUtilization
            print(memoryList)
            print("")
        print("Average memory utilization: " + str(round(averageTotalUtilization, 4)))
        print("Average search time: " + str(round((searchTime / count), 4)))

    else:
        for i in range(0, 50):
            while notFull:
                size = random.randint(1, 8)
                memoryList = Worst_Fit(memoryList, size)
            currentUtilization = Memory_Utilization(memoryList)
            print(currentUtilization)
            memoryList = Release(memoryList)
            averageUtilization = currentUtilization / 50
            averageTotalUtilization = averageTotalUtilization + averageUtilization
            print(memoryList)
            print("")
        print("Average memory utilization: " + str(round(averageTotalUtilization, 4)))
        print("Average search time: " + str(round((searchTime / count), 4)))


def Best_Fit(mem, size):
    global notFull
    global searchTime
    global count
    viableHole = []

    for i in range(0, len(mem)):
        if mem[i] < 0 and -size >= mem[i]:
            viableHole.append([mem[i], i])
    if len(viableHole) == 0:
        notFull = False
        return mem
    else:
        searchTime = searchTime + len(viableHole)
        count = count + 1
        smallestHoleSize = -len(mem)
        smallestHoleIndex = 0
        for i in range(0, len(viableHole)):
            if viableHole[i][0] > smallestHoleSize:
                smallestHoleSize = viableHole[i][0]
                smallestHoleIndex = viableHole[i][1]
        oldHoleSize = smallestHoleSize
        mem[smallestHoleIndex] = size
        if smallestHoleIndex + size < len(mem):
            if mem[smallestHoleIndex + size] == 0:
                mem[smallestHoleIndex + size] = oldHoleSize + size
        return mem


def Worst_Fit(mem, size):
    global notFull
    global searchTime
    global count
    viableHole = []

    for i in range(0, len(mem)):
        if mem[i] < 0 and -size >= mem[i]:
            viableHole.append([mem[i], i])
    if len(viableHole) == 0:
        notFull = False
        return mem
    else:
        searchTime = searchTime + len(viableHole)
        count = count + 1
        largestHoleSize = 0
        largestHoleIndex = 0
        for i in range(0, len(viableHole)):
            if viableHole[i][0] < largestHoleSize:
                largestHoleSize = viableHole[i][0]
                largestHoleIndex = viableHole[i][1]
        oldHoleSize = largestHoleSize
        mem[largestHoleIndex] = size
        if largestHoleIndex + size < len(mem):
            if mem[largestHoleIndex + size] == 0:
                mem[largestHoleIndex + size] = oldHoleSize + size
        return mem


def Release(mem):
    global notFull
    notFull = True
    allocated = []

    for i in range(0, len(mem)):
        if mem[i] > 0:
            allocated.append([mem[i], i])
    randomIndex = random.randint(0, len(allocated)-1)
    releaseSize = allocated[randomIndex][0]
    releaseIndex = allocated[randomIndex][1]

    mem[releaseIndex] = -releaseSize
    combinedMem = Combine_Mem(mem)
    return combinedMem


def Memory_Utilization(mem):
    global memoryListSize
    runningTotal = 0
    for i in range(0, len(mem)):
        if mem[i] > 0:
            runningTotal = runningTotal + mem[i]
    memUtilization = runningTotal / memoryListSize
    return memUtilization


def Combine_Mem(mem):
    allocatedOrFree = []
    for i in range(0, len(mem)):
        if mem[i] != 0:
            allocatedOrFree.append([mem[i], i])
    for i in range(len(allocatedOrFree)-2, -1, -1):
        if allocatedOrFree[i+1][0] < 0 and allocatedOrFree[i][0] < 0:
            mem[allocatedOrFree[i][1]] = allocatedOrFree[i][0] + allocatedOrFree[i+1][0]
            allocatedOrFree[i][0] = allocatedOrFree[i][0] + allocatedOrFree[i + 1][0]
            mem[allocatedOrFree[i+1][1]] = 0
    return mem


if __name__ == '__main__':
    main()
