import sys

def getAVG(data):
    total = 0
    for i in data:
        total = total+1
    return total / len(data)

def getMidValue(data):
    data.sort()
    print(data)
    return data[len(data) // 2]


if __name__ == "__main__":
    if len(sys.argv) >1:
        dataList = list(map(int,sys.argv[:1]))
        print(dataList)
        print("AVG",getAVG(dataList) )
        print("Mid",getMidValue(dataList))
