import os
import re
import argparse

strong_type = ['copy', 'strong', 'retain']

def codeCreate(hPath):
    data = open(hPath, "r", encoding="utf-8", errors="ignore")
    each = data.readline()

    my_property = list()
    whole_string = ''
    while each:
        whole_string += each

        if each.find("@property") != -1:
            clean_each = each.strip("\n")
            my_property.append(each)

        each = data.readline()


    factory_string = "+ (instancetype)itemWith"

    for index in range(len(my_property)):
        each = my_property[index]
        match = re.findall(r"\b[a-zA-Z_0-9]+\b", each)
        name = match[-1]
        type = match[-2]
        retain_type = match[-3]

        if index == 0:
            if retain_type in strong_type:
                factory_string += '%s:(%s *)%s' % (name.capitalize(), type, name)
            else:
                factory_string += '%s:(%s)%s' % (name.capitalize(), type, name)

        else:
            if retain_type in strong_type:
                factory_string += '\n%s:(%s *)%s' % (name, type, name)
            else:
                factory_string += '\n%s:(%s)%s' % (name, type, name)

    factory_string += ';'
    whole_string = whole_string.replace("@end", factory_string)
    whole_string += "\n@end"

    with open(hPath, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(whole_string)

    class_name = ""
    match = re.findall(r"\b[a-zA-Z_0-9]+\b", hPath)
    class_name = match[-2]


    ## .m 方法
    mPath = hPath[0:-1]
    mPath += "m"


    data = open(mPath, "r", encoding="utf-8", errors="ignore")
    each = data.readline()

    whole_string = ''
    while each:
        whole_string += each
        each = data.readline()

    whole_string = whole_string.replace("@end", factory_string)
    whole_string = whole_string.rstrip()
    whole_string = whole_string[0:-1]
    whole_string += '\n{\n'
    whole_string += "\t%s* item = [self new];\n" % (class_name)

    for index in range(len(my_property)):
        each = my_property[index]
        match = re.findall(r"\b[a-zA-Z_0-9]+\b", each)
        name = match[-1]
        type = match[-2]
        whole_string += "\titem.%s = %s;\n" % (name, name)

    whole_string += "\treturn item;\n}"
    whole_string += "\n\n@end"

    with open(mPath, 'w', encoding='utf-8', errors='ignore') as f:
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
