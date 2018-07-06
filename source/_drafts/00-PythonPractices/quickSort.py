# -*- coding: utf-8 -*-

import numpy as np


#1）依次对比arr[0]和其他元素，比arr[0]小的话，就原地删除，然后插入到arr[0]前面，基准值后移。大于等于，则不处理。然后递归
#原地排序
def quick_sort1(arr, left, right):

    if left >= right:
        return
    flag = left
    for i in range(left + 1, right + 1):
        if arr[flag] > arr[i]:
            temp = arr[i]
            del arr[i]
            arr.insert(flag, temp)
            flag += 1
    quick_sort1(arr, left, flag - 1)
    quick_sort1(arr, flag + 1, right)


#2）基准值arr[0]，对比所有元素，比它小就追加到less后面，比它大就追加到great后面，相等就追加到pivot后面，然后递归
#返回排序后的列表
def quick_sort2(arr):
    less = []
    great = []
    pivot = []
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]
        for i in arr:
            if i < p:
                less.append(i)
            elif i > p:
                great.append(i)
            else:
                pivot.append(i)
        less = quick_sort2(less)
        great = quick_sort2(great)
        return less + pivot + great


#2-2）基本思想同上，代码更简化
def quick_sort22(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort22([i for i in arr[1:]
                             if i < arr[0]]) + [arr[0]] + quick_sort22(
                                 [i for i in arr[1:] if i >= arr[0]])


#2-3）思路同上，更简化的版本
quick_sort23=lambda xs:((len(xs)<=1 and [xs]) or [quick_sort23([x for x in xs[1:] if x<xs[0]])+[xs[0]]+quick_sort23([x for x in xs[1:] if x>=xs[0]])])[0]
quick_sort24=lambda arr:arr if len(arr)<=1 else quick_sort24([x for x in arr[1:] if x<arr[0]])+[arr[0]]+quick_sort24([x for x in arr[1:] if x>=arr[0]])

#lambda 参数：取值1，如果满足条件1，否则，取值2


#3）定义两个函数：分区和排序。分区是要把列表元素移动位置，直到基准值arr[0]移到中间（左边都比它小，右边都比它大）。排序则调用分区并递归
#原地排序
def partition(arr, i, j):
    p = arr[i]
    while i != j:
        while i < j and p <= arr[j]:  #此处添加=，解决了之前遇到的序列中有重复值时死循环的问题
            j -= 1
        arr[i] = arr[j]
        while i < j and p > arr[i]:
            i += 1
        arr[j] = arr[i]
    arr[i] = p
    return i


def quick_sort3(arr, i, j):
    if i < j:
        mid = partition(arr, i, j)
        quick_sort3(arr, i, mid - 1)
        quick_sort3(arr, mid + 1, j)


#3-2)上述思路的变体，分区函数变动，每次都比右边是否比基准值大，大的话，j前移，否则，把arr[j]给到arr[i]，然后i后移，arr[i]再给到arr[j]，继续上述循环
def partition2(arr, i, j):
    p = arr[i]
    while i != j:
        while i < j and p <= arr[j]:
            j -= 1

        while i < j and p > arr[j]:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = p
    return i


def quick_sort32(arr, i, j):
    if i < j:
        mid = partition2(arr, i, j)
        quick_sort32(arr, i, mid - 1)
        quick_sort32(arr, mid + 1, j)


#3-3)分区函数变动，基准值为最后一个值，依次比较，如果比基准值小，就换到前面去，最后再把基准值换到中间。
def partition3(arr, i, j):
    p = arr[j]
    x = i - 1
    for y in range(i, j):
        if arr[y] <= p:
            x += 1
            arr[x], arr[y] = arr[y], arr[x]
    arr[x + 1], arr[j] = arr[j], arr[x + 1]
    return x + 1


def quick_sort33(arr, i, j):
    if i < j:
        mid = partition3(arr, i, j)
        quick_sort33(arr, i, mid - 1)
        quick_sort33(arr, mid + 1, j)


#4）非递归方式，使用栈,思路类似previous，只是把切分边界保存在栈（用list实现）里，\
#当只剩一个元素时，跳出本次循环，进入下次循环，看下一个区间里元素值是否多于1个，直到栈空
def quick_sort4(arr, i, j):
    if j <= i:
        return
    stack = []
    stack.extend([i, j])
    while stack:
        left = stack.pop(0)
        right = stack.pop(0)
        if right <= left:
            continue
        x = left - 1
        p = arr[right]
        for y in range(left, right):  #此处循环不包括最后一个元素，循环结束后，最后一个元素换到中间
            if arr[y] <= p:
                x += 1
                arr[x], arr[y] = arr[y], arr[x]
        arr[x + 1], arr[right] = arr[right], arr[x + 1]
        stack.extend([left, x, x + 2, right])


if __name__ == "__main__":
    s = np.random.randint(1, 30, 20).tolist()
    print(s)
    #print(quick_sort24(s))
    quick_sort4(s, 0, len(s) - 1)
    print(s)