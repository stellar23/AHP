# -*- codeing = utf-8 -*-
# @Time : 02/10/2022
# @Author : rain
# @Email : stellar052323@163.com
# @File : AHP.py
# @Software : PyCharm


import numpy as np


# 层次分析法
class AHP:
    def __init__(self, C, P1, P2, P3, P4):
        self.C = C
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        pass

        #  计算矩阵维度
        self.C_x, self.C_y = self.C.shape
        self.P1_x, self.P1_y = self.P1.shape
        self.P2_x, self.P2_y = self.P2.shape
        self.P3_x, self.P3_y = self.P3.shape
        self.P4_x, self.P4_y = self.P4.shape

        #  判断矩阵一致性检验
        Checking(self.C)
        Checking(P1)
        Checking(P2)
        Checking(P3)
        Checking(P4)

        # 计算A-C权重向量
        self.w_c = Weightlist(C)
        # 计算C-P权重向量
        self.w_P1 = Weightlist(P1)
        self.w_P2 = Weightlist(P2)
        self.w_P3 = Weightlist(P3)
        self.w_P4 = Weightlist(P4)

        # 层次总排序
        self.listwp = []
        self.listwp.append(self.w_P1)
        self.listwp.append(self.w_P2)
        self.listwp.append(self.w_P3)
        self.listwp.append(self.w_P4)
        self.listwpwp = np.array(self.listwp)
        self.listwpwp.reshape(self.P1_x,4)
        self.sortw = np.dot(self.w_c,self.listwpwp)
        print("\n""权重总排序：",self.sortw)
        mm = max(self.sortw)
        for m in range(len(self.sortw)):
            if self.sortw[m] == mm:
                print("最优方案为方案{}".format(m+1))
                pass
            pass

    pass


def Weight(P_data, i):
    """
    计算归一化权重
    :param P_data: 矩阵形式
    :param i:矩阵的第i列
    :return: 权重w
    """
    x, e1 = P_data.shape
    sum0 = 1
    j = 0
    while j <= x - 1:
        sum0 = sum0 * P_data[i, j]
        j = j + 1
        pass
    w = sum0 ** (1 / x)
    return '%.3f' % w
    pass


def Weightlist(Matrix):
    """
    计算权重向量
    :param Matrix: 判断矩阵
    :return: 权重向量
    """
    xx, yy = Matrix.shape
    listw = []
    for n in range(xx):  # 格式输出判断矩阵A-C的w
        weight1 = Weight(Matrix, n)
        listw.append(weight1)
        pass
    listw_new = []
    for nnn in listw:  # 转换列表中元素类型
        listw_new.append(float(nnn))
        listw = listw_new
        pass
    listww = []
    for nn in range(xx):  # 归一化
        weight2 = listw[nn] / sum(listw)
        weight3 = round(weight2, 3)  # 保留三位小数
        listww.append(weight3)
        pass
    print("权重向量矩阵w：= {}".format(listww))
    return listww
    pass


def Checking(matrix):
    """
    一致性检验
    :param matrix:
    :return: CI,RI
    """
    n, e2 = matrix.shape
    [lamda, e3] = np.linalg.eig(matrix)
    max_lamda = max(lamda)
    CI = abs(max_lamda - n) / (n - 1)
    if n == 3:
        RI = 0.58
        pass
    elif n == 4:
        RI = 0.90
        pass
    elif n == 5:
        RI = 1.12
        pass
    elif n == 6:
        RI = 1.24
        pass
    elif n == 7:
        RI = 1.32
        pass
    elif n == 8:
        RI = 1.41
        pass
    elif n == 9:
        RI = 1.45
        pass
    elif n == 10:
        RI = 1.49
        pass
    else:
        print("False,矩阵阶数必须大于2 小于10")
        pass
    CR = CI / RI
    print("判断矩阵检验：")
    print("一致性检验指标：CI = "'%.6f' % CI)
    print("随机一致性指标：CR = "'%.6f' % CR, "\n")
    if CR > 0.1:
        print("False,RI值大于0.1，判断矩阵构造不合理")
        pass
    pass


if __name__ == "__main__":
    # 输入判断矩阵
    C = np.array([[1, 1 / 4, 2, 1 / 3], [4, 1, 8, 2], [1 / 2, 1 / 8, 1, 1 / 5], [3, 1 / 2, 5, 1]])
    P1 = np.array([[1, 1 / 4, 2], [4, 1, 8], [1 / 2, 1 / 8, 1]])
    P2 = np.array([[1, 5, 2], [1 / 5, 1, 1 / 2], [1 / 2, 2, 1]])
    P3 = np.array([[1, 1 / 3, 2], [3, 1, 5], [1 / 2, 1 / 5, 1]])
    P4 = np.array([[1, 5, 7], [1 / 5, 1, 2], [1 / 7, 1 / 2, 1]])
    # 运行模型
    AHP(C, P1, P2, P3, P4)
