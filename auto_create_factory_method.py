import os


def codeCreate(hPath):
    data = open(hPath, "r", encoding="utf-8", errors="ignore")
    each = data.readline()
    print(data)

    while each:
        print(each)
        each = data.readline()





if __name__ == "__main__":
    codeCreate(r"/Users/wen/tips-ios2/Liaodao/Classes/Follow/IndicialEquation/Main/Model/LDLeagueStandingItem.h")