__author__ = 'zhengyangqiao'

import random

def coinToss(number):
    recordList, heads, tails = [], 0, 0
    for i in range(number):
        flip = random.randint(0,1)
        if (flip == 0):
            print("Heads")
            recordList.append("Heads")
        else:
            print("Tails")
            recordList.append("Tails")

    print(str(recordList))
    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))

coinToss(2)