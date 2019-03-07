import random

numList = [2]
for count in range(6):
    numList.append(random.randint(1, 10))
    numList.sort()
sumNumList = sum(numList)
avgNumList = (sumNumList / 7)

print("List: ", numList, " - Sum: ", sumNumList, " - Median: ", numList[3], " - Avg: ", round(avgNumList, 3))