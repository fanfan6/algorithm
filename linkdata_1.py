#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 约瑟夫环问题

def linkData(n, m):
    # 自动生成列表，由1到n
    list = range(1, n+1)
    # 删除的为下标，真实数值 -1
    m -= 1
    # 第一次删除的下标
    k = m%n
    # 取到剩余的最后一人
    while(len(list) > 1):
        # 删除列表中下标为K的元素。python中del元素下标自动补齐
        del list[k]
        # 获取每次需要删除的元素下标进行删除
        k = (k+m) % len(list)
    # 输出最后的结果
    # 一般用return返回结果
    print list[0]


if __name__ == '__main__':
    n = int(raw_input('Enter monky number:'))
    m = int(raw_input('Enter number:'))
    linkData(n, m)
