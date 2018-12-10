# 我媳妇给我的测试题.

class ContinuousNum:
    def __init__(self, start,end):
        self.start = start
        self.end = end

    # 判断传进来的item是否是连号
    def is_previous_item(self,item):
        if int(item.start) == int(self.end) or int(item.start) == int(self.end) + 1:
            return True
        elif int(item.end) > int(self.end):
            return True
        else:
            return False


    # 判断传进来的item是否被自己包含
    def is_part_item(self, item):
        if int(self.start) <= int(self.start) and int(self.end) >= int(item.end):
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

    # 升序
    start_end_nums = sorted(start_end_nums, key=lambda each_num: int(each_num.start))
    for each in start_end_nums:
        print(each)
    print("======= sort end ============")


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
            # 若当前这个被上个包含了,则忽略它
            if last_num.is_part_item(num):
                #print("被包含了")
                continue

            # 若当前这个是上个的续号则添加进入
            if last_num.is_previous_item(num):
                last_nums.append(num)
                last_num = num
                print("连续")
            else:
                #print("下一组")
                last_nums = list()
                whole_list.append(last_nums)
                last_nums.append(num)
                last_num = num


    for each in whole_list:
        combine_num = combine_nums_to_one(each)
        print(combine_num)



if __name__ == '__main__':
    command_main('(1,6)|(2,4)|(3,5)|(2,8)|(7,11)|(6,6),(3,3)|(3,4)')