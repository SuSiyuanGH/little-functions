# -*- coding : utf-8 -*-
# @author : Papaya
# @first date : 2021-03-29
# @sn : 1-2
# @desc : 获取指定目录下的所有后裔目录和所有后裔文件的绝对路径
# @version : 1

import os


def f1(dir:str):
    all = [dir]
    all_f = []
    idx = 0
    while(True):
        if(os.path.isdir(all[idx])):
            for i in os.listdir(all[idx]):
                path = all[idx]+'/'+i
                all.append(path)
                if(os.path.isfile(path)):
                    all_f.append(path)
        if(idx == len(all)-1):
            break
        idx += 1
    return all_f

for i in f1('H:/Mine'):
    print(i)
