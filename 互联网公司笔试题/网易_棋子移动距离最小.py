#coding=UTF-8
'''
小易将n个棋子摆放在一张无限大的棋盘上。第i个棋子放在第x[i]行y[i]列。同一个格子允许放置多个棋子。
每一次操作小易可以把一个棋子拿起并将其移动到原格子的上、下、左、右的任意一个格子中。
小易想知道要让棋盘上出现有一个格子中至少有i(1 ≤ i ≤ n)个棋子所需要的最少操作次数.

输入描述:
输入包括三行,第一行一个整数n(1 ≤ n ≤ 50),表示棋子的个数
第二行为n个棋子的横坐标x[i](1 ≤ x[i] ≤ 10^9)
第三行为n个棋子的纵坐标y[i](1 ≤ y[i] ≤ 10^9)


输出描述:
输出n个整数,第i个表示棋盘上有一个格子至少有i个棋子所需要的操作数,以空格分割。行末无空格

如样例所示:
对于1个棋子: 不需要操作
对于2个棋子: 将前两个棋子放在(1, 1)中
对于3个棋子: 将前三个棋子放在(2, 1)中
对于4个棋子: 将所有棋子都放在(3, 1)中

输入例子1:
4
1 2 4 9
1 1 1 1

输出例子1:
0 1 3 10

思路：最少操作的棋子最终所在位置一定是横坐标与纵坐标都在原始棋子位置上的，
对于每个横坐标取自x，每个纵坐标取自y的所有可能位置遍历，找到距离该位置最近的n个点
比如（1,1） 最近的n个点距离分别是0,1,3,8， 做cumsum得到0,1,4,12即该位置有1-n个旗子的最小距离
(2,1) 则是0,1,2,7 做cumsum得到0,1,3,10
(4,1) 则是0,2,3,5 做cumsum得到0,2,5,10
(9,1) 则是0,5,7,8 做cumsum得到0,5,12,20
从而得到一个二维矩阵
[[0,1,4,12], [0,1,3,10], [0,2,5,10], [0,5,12,20]
找到二维矩阵的每一列的最小值,即是最终的输出
'''
def printMinOperation(n, x, y):
    _x = list(set(x))
    _y = list(set(y))
    dist_list = []
    for i in _x:
        for j in _y:
            distances = [abs(i-x[k]) + abs(j-y[k]) for k in range(n)]
            distances.sort()
            sum_list = [sum(distances[:m]) for m in range(1, n+1)]
            dist_list.append(sum_list)

    for i in range(n):
        result = min(a[i] for a in dist_list)
        if i == n-1:
            print(result)
        else:
            print(result, end=" ")


if __name__ == "__main__":
    n = 4
    x = [1, 1, 4, 9]
    y = [1, 1, 3, 9]
    printMinOperation(n, x, y)

            