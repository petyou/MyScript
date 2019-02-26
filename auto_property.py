import os
import re
import argparse



def codeCreate(hPath):
    data = open(hPath, "r", encoding="utf-8", errors="ignore")
    each = data.readline()

    my_property_list = list()
    whole_string = ''
    while each:
        whole_string += each

        if each.find("import") != -1:
            each = data.readline()
            continue

        if each.find("=") != -1:
            name = each.split("=")[0]
            name = name.strip()
            my_property_list.append(name)
            each = data.readline()
            continue

        match = re.search('"(.*?)"', each)
        if match != None :
            name = match.group(1)
            my_property_list.append(name)

        each = data.readline()
        continue

    property_string = ''

    for i in range(len(my_property_list)):
        each_property = my_property_list[i]
        auto_property = "@property (nonatomic, copy) NSString *%s;\n" % (each_property)
        property_string += auto_property

    whole_string = whole_string.replace("@end", property_string)
    whole_string += "\n@end"

    with open(hPath, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(whole_string)

    print("Done!!")



if __name__ == "__main__":

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--path", help=".h的全路径", metavar="path")
    options = parser.parse_args()
    hPath = ""
    hPath = options.path

    if hPath:
        codeCreate(hPath)
        print("Done")
    else:
        print(".h路径为空 使用 -path带上路径")
    '''
    path = r"/Users/wen/tips-ios2/Liaodao/Classes/TeamData/TeamDetail/Overview/Model/LDTeamHonorCellItem.h"
    codeCreate(path)
