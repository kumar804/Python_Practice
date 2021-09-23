"""""
*author - Manish Singh
*date 19-09-2021
*time - 05:45 PM
*Title - Flip coin
"""""

import random
tailCount = 0
headCount = 0
coinResult = 0

count = int(input("enter number of time want to flip coin"))
class FlipCoin:
    for i in range(1,count):
        coinResult = random.uniform(0,1)
        print(coinResult)
        if coinResult < 0.5:
            tailCount += 1
        else:
            headCount += 1
            headPercentage = (headCount / count)*100
            print("Head Percentage is:",headPercentage)
            tailPercentage = (tailCount / count)*100
            print("Tail Percentage is:",tailPercentage)