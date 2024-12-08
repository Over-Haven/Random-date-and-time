import random

import time

def getRandomDate(StarDate , endDate):
    print("Printing random date between", StarDate , "and" , endDate)
    randomGenerator = random.random()
    dateForamat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(StarDate,dateForamat))
    endtime = time.mktime(time.strptime(endDate,dateForamat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateForamat, time.localtime(randomTime))
    return randomdate

print("random date =", getRandomDate("1/1/2020" , "12/12/2024"))