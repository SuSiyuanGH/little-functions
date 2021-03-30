# -*- coding : utf-8 -*-
# @author : Papaya
# @first date : 2021-03-29
# @sn : 1-1
# @desc : 获取指定目录下的所有后裔目录和所有后裔文件的绝对路径
# @version : 2
# @新功能：异常处理

import os


def f1(dir: str):
    all = [dir]
    idx = 0
    while(True):
        if(os.path.isdir(all[idx])):
            while(True):
                # 异常处理
                try:
                    clist = os.listdir(all[idx])
                    for i in clist:
                        all.append(all[idx]+'/'+i)
                    break
                except Exception as exp:
                    break
        if(idx == len(all)-1):
            break
        idx += 1
    return all
