

class ContinuousNum:
    def __init__(self, start,end):
        self.start = start
        self.end = end

    # 判断传进来的item是否是连号
    def is_previous_item(self,item):
        if (int(item.start) - 1 ) == int(self.end):
            return True
        else:
            return False

    def __str__(self):
        return "(%s,%s)" % (self.start,self.end)


# 将(x,y)构建成对象
def init_continuous_num(a_string):
    a_string =  a_string.strip("(")
    a_string = a_string.strip(")")

    start_end = a_string. split(",")
    if len(start_end) != 2:
        return None
    else:
        num = ContinuousNum(start_end[0], start_end[1])
        return num


# 将多个连续组合成一个
def combine_nums_to_one(a_list):
    first_num = a_list[0]
    last_num = a_list[-1]
    combine_num = ContinuousNum(first_num.start,last_num.end)
    return combine_num


def command_main(long_time):
    if isinstance(long_time, str) is False:
        return

    times = long_time.split("|")
    if len(times) == 0:
        return

    start_end_nums = list()
    for each_time in times:
        num = init_continuous_num(each_time)
        if num != None:
            start_end_nums.append(num)

    # 需要start_end_nums 排序
    # ...

    last_num = None
    whole_list = list()
    last_nums = list()
    whole_list.append(last_nums)

    for index in range(len(start_end_nums)):
        num = start_end_nums[index]

        if last_num is None:
            last_nums.append(num)
            last_num = num
        else:
            if last_num.is_previous_item(num):
                last_nums.append(num)
                last_num = num
            else:
                last_nums = list()
                whole_list.append(last_nums)
                last_nums.append(num)
                last_num = num


    for each in whole_list:
        combine_num = combine_nums_to_one(each)
        print(combine_num)



if __name__ == '__main__':
    command_main('(1,3)|(4,4)|(5,8)|(9,10)|(12,15)|(16,17)|(19,20)|(27,29)')