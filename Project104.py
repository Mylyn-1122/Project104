import csv
from collections import Counter
with open('./heightweight.csv') as f:
#with open('/Users/zhengmylyn/OneDrive/Documents/Games-coding/coding/Python/Projects/Project104/heightweight.csv') as f: 
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
        nNum = fileData[i][1]
        newData.append(float(nNum))

def mean():
    

    n = len(newData)
    total = 0

    for x in newData:
        total += x

    mean = total/n
    print("the mean is " + str (mean))
    return mean


def mode():
    
    
    data = Counter(newData)
    modeRange = {
        "50-60":0,
        "60-70":0,
        "70-80":0,
    }

    for height, occurance in data.items():
        if 50<float(height)<60:
            modeRange["50-60"]+=occurance
        elif 60<float(height)<70:
            modeRange["60-70"]+=occurance
        elif 70<float(height)<80:
            modeRange["70-80"]+=occurance

    mode_range, mode_occurance = 0,0

    for range, occurance in modeRange.items():
        if occurance > mode_occurance:
            mode_range, mode_occurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance

    mode = float((mode_range[0]+mode_range[1])/2)
    print("mode is " + str(mode))


def median():
    

    n=len(newData)
    newData.sort()
    if n%2 == 0 :
        m1 = float(newData[n//2])
        m2 = float(newData[n//2-1])
        median = (m1+m2)/2
    else:
        median = newData[n//2]

    print("the median is "+str(median))
    return median



mean()
median()
mode()