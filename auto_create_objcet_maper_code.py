import os
import re
import argparse

strong_type = ['copy', 'strong', 'retain']

def codeCreate(hPath):
    data = open(hPath, "r", encoding="utf-8", errors="ignore")
    each = data.readline()

    my_property = list()
    whole_string_list = []
    insertIndex = 0

    count = 0
    while each:
        whole_string_list.append(each)


        if each.find("var") != -1:
            clean_each = each.strip("\n")
            start = clean_each.index("var")
            end = clean_each.index(":")
            clean_each = clean_each[start+3:end]
            clean_each = clean_each.strip()
            my_property.append(clean_each)
            insertIndex = count + 1

        each = data.readline()
        count += 1

    factory_string = "\n"
    factory_string += "\trequired init?(map: Map) {\n\n\t}\n\n"

    factory_string += "\tfunc mapping(map: Map) {\n"

    for index in range(len(my_property)):
        each = my_property[index]
        pre = "\t\t" + each

        if len(pre) < 14:
            for index in range(14 - len(pre)):
                pre += " "

        factory_string += pre
        factory_string += '<- map["%s"]\n' %(each)

    factory_string += "\t}\n"

    whole_string_list.insert(insertIndex, factory_string)

    whole_string = "".join(whole_string_list)



    with open(hPath, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(whole_string)


if __name__ == "__main__":
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

