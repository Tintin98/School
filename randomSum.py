import random

numList = [2]
for count in range(6):
    numList.append(random.randint(1, 10))
    numList.sort()
sumNumList = sum(numList)
avgNumList = (sumNumList / 7)

print(numList, "\nFrom this list, the sum is", sumNumList, ", the median is", numList[3],
    "\nand the average is", round(avgNumList, 2))
