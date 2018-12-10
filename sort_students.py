# 排序学习

class Student:
    def __init__(self, name, score):
        self.__name__ = name
        self.__score__ = score

    def get_score(self):
        return self.__score__

    def get_name(self):
        return self.__name__

    def __str__(self):
        return str("name:{} score:{}".format(self.__name__, self.__score__))


if __name__ == "__main__":
    examine_scores = {"google": 98,
                      "facebook": 99,
                      "baidu": 52,
                      "alibaba": 80,
                      "yahoo": 49,
                      "IBM": 70,
                      "android": 76,
                      "apple": 99}

    students = [Student(x, y) for x, y in examine_scores.items()]
    for student in students:
        print(student)
    print("===" * 5)

    # 注意sorted 会生成行序列 不会改变原来的值。
    students = sorted(students, key=lambda student: student.get_score())
    # 或者这样 但是不建议 破坏了封装
    #students = sorted(students, key=lambda student: student.__score__)
    for student in students:
        print(student)

