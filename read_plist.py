# -*- coding:utf-8 -*-
#!/usr/bin/python3
# 测试读取plist文件数据,修改后重新写入

from biplist import *
import time
import os


try:
    # 当前目录
    cur_dir = os.getcwd()

    # 文件路径
    app_info_path = '/Users/wen/Desktop/Info.plist'
    setting_path = '/Users/wen/Desktop/Info.plist'

    # 读取Info.plist文件和ProjectSettings.plist
    app_info = readPlist(app_info_path)
    settings = readPlist(setting_path)

    # 读取版本号
    app_version = app_info['appInsideVersion'].split('.')
    auto_verson = settings['MyBuildVersion']

    # 拆出前三出来比较
    app_version = ''.join(app_version)
    auto_verson_pre3 = auto_verson[0:3]
    auto_verson_sub3_int = int(auto_verson[-3:])

    target_autoVersion = ''
    if app_version != auto_verson_pre3:
        target_autoVersion = app_version + '000'
    else:
        auto_verson_sub3_int += 1
        target_autoVersion = auto_verson_pre3 + '%03d' % (auto_verson_sub3_int)

    # 更新数据
    settings['MyBuildVersion'] = target_autoVersion

    settings['UpdateDate'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(settings)

    # 写入
    res = writePlist(settings, setting_path, 'utf-8')
    print(res)


except BaseException as e:
    print(str(e))