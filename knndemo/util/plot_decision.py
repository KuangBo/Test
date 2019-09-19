# coding=utf-8

from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

'''
    实现结果可视化Util
'''


def plot_decision_regions(x, y, test, classifier, resolution=0.02):
    # 设置标记点和颜色
    markers = ('^', 'o', 'v', 'x', 's')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 绘制决策面
    x1_min, x1_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    x2_min, x2_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # 绘制所有样本
    for idx, cl in enumerate(np.unique(y)):
        c_label = ('setosa' if cl == 0 else 'versicolor')
        plt.scatter(x=x[y == cl, 0], y=x[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx],
                    label=(c_label if cl == 1 else 'virginica'))
    # 高亮预测样本
    if test:
        x_test = test[0]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='black', alpha=1.0, linewidths=0.5, marker='x', s=55, label='Test_set')
