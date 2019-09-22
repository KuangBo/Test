# coding=utf-8


from sklearn.datasets import load_iris
from sklearn.externals._arff import xrange
from sklearn.model_selection import train_test_split  # 交叉验证
from sklearn.preprocessing import StandardScaler  # 标准化
from sklearn.neighbors import KNeighborsClassifier  # KNN
from irisdemo.util.plot_decision import plot_decision_regions
from sklearn.metrics import classification_report  # 判断准确率
import matplotlib.pyplot as plt
import numpy as np

'''
    利用KNN实现iris数据集的分类
    并通过matplotlib包实现结果可视化
'''

# 导入数据集
iris = load_iris()
# 将整个数据划分为训练集和测试集两个部分，其中训练集0.75，测试集0.25
X_train, X_test, Y_train, Y_test = train_test_split(iris.data[:, [2, 3]], iris.target, test_size=0.4, random_state=50)

# 将数据进行标准化处理，然后导入KNN模型进行训练
ss = StandardScaler()
ss.fit(X_train)  # 计算样本的均值和标准差
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

k_range = list(xrange(1, 21, 2))
test_accuracy = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, Y_train)
    y_predict = knn.predict(X_test)
    test_accuracy.append(knn.score(X_test, Y_test))
    # 检验模型的好坏
    print("The accuracy of K-Nearest Neighbor Classifier is", knn.score(X_test, Y_test))
    # print(classification_report(Y_test, y_predict, target_names=iris.target_names))
    # for i in range(len(y_predict)):
    #     print("第{}次，预测值：{}\t真实值：{}".format(i+1, y_predict[i], Y_test[i]))
    # 绘制决策边界
    x_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((Y_train, Y_test))
    plot_decision_regions(x=x_combined, y=y_combined, test=[X_test, Y_test], classifier=knn)
    plt.xlabel('petal length--std')
    plt.ylabel('petal width--std')
    plt.legend(loc='upper left')
    plt.savefig("./result/knn/Result of k={}".format(k))
    plt.show()

plt.plot(k_range, test_accuracy)
plt.xlabel("Value of K")
plt.ylabel("Testing Accuracy")
plt.savefig("./result/knn/Change of K and Acc")
plt.show()
'''
# 检验模型的好坏
print("The accuracy of K-Nearest Neighbor Classifier is", knc.score(X_test, Y_test))
print(classification_report(Y_test, y_predict, target_names=iris.target_names))
'''
