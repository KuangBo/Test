# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals._arff import xrange
from sklearn import tree

from irisdemo.util.plot_decision import plot_decision_regions


# 可视化iris数据集，寻找高相关性的属性
def visualize_data(x, y, feature_names):
    f = [y == 0, y == 1, y == 2]
    # 设置三类的索引
    color = ['red', 'blue', 'green']
    # 绘制四个属性两两之间的散点图
    fig = plt.figure(1)
    # fig, axes = plt.subplots(3, 4, sharex=True, sharey=True)
    foot = 0
    for i in range(16):
        row = i // 4
        col = i % 4
        foot += 1
        if row == col:
            foot -= 1
            continue
        ax = plt.subplot(3, 4, foot)
        for k in range(3):
            ax.scatter(x[f[k], row], x[f[k], col], c=color[k], s=3)
            # print(x[f[k], row])
            # print(f[k])
            # print(len(x[f[k], row]))
            # print('***'*60)
            # print(x[f[k], col])
            ax.set_xlabel(feature_names[row])
            ax.set_ylabel(feature_names[col])
    # 设置间距
    fig.subplots_adjust(hspace=0.5, wspace=1)
    plt.savefig("./result/Comparison of Attribution")
    plt.show()


if __name__ == '__main__':
    print("--------------------" * 5)
    # 导入iris数据集
    iris = load_iris()
    x = iris.data
    y = iris.target
    visualize_data(x, y, iris.feature_names)
    # 将整个数据集划分为两个部分，其中训练集占0.75，测试集占0.25，加入random_state，保证每次划分是一样的
    x_train, x_test, y_train, y_test = train_test_split(iris.data[:, [2, 3]], iris.target, test_size=0.25,
                                                        random_state=50)

    # 进行标准化处理
    ss = StandardScaler()
    x_train_std = ss.fit_transform(x_train)
    x_test_std = ss.fit_transform(x_test)

    max_d_set = list(xrange(1, 21, 1))
    test_accuracy = []
    for max_d in max_d_set:
        # 构建决策树
        clf = tree.DecisionTreeClassifier(max_depth=max_d)
        clf.fit(x_train, y_train)  # 进行决策树拟合

        # 预测
        y_test_pre = clf.predict(x_test)
        # print("The value of predict:", y_test_pre)
        # for i in range(len(y_test)):
        #     print("真实值：{}\t预测值：{}".format(y_test[i], y_test_pre[i]))

        # 计算准确率accuracy
        print("The accuracy:", clf.score(x_test, y_test))
        test_accuracy.append(clf.score(x_test, y_test))

        # 实现结果可视化
        x_combined = np.vstack((x_train, x_test))   # 按垂直方向（行顺序）堆叠数组构成一个新的数组
        y_combined = np.hstack((y_train, y_test))   # 按水平方向（列顺序）堆叠数组构成一个新的数组
        plot_decision_regions(x=x_combined, y=y_combined, test=[x_test, y_test], classifier=clf)
        # 只传出train的数据
        # plot_decision_regions(x=x_train, y=y_train, test=[x_test, y_test], classifier=clf)
        plt.xlabel('petal length--std')
        plt.ylabel('petal width--std')
        plt.legend(loc='upper left')
        plt.savefig("./result/decisionTree/Result of max_d={}".format(max_d))
        plt.show()
    plt.plot(max_d_set, test_accuracy)
    plt.xlabel("Value of max_depth")
    plt.ylabel("Testing Accuracy")
    plt.savefig("./result/decisionTree/Change of max_depth and Acc")
    plt.show()
