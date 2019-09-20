# coding=utf-8

import tensorflow as tf

'''
    batch的概念，反向传播算法相当于实现了一个迭代的过程
    每次迭代的开始，需要选取一小部分训练数据，这一小部分的数据就是batch
'''
'''
    因为每生成一个常量，Tensorflow就会在计算图中增加一个节点，将会使得计算图非常大，而且效率低
    placeholder相当于定义了一个位置，这个位置中的数据在程序运行的时候再进行指定
    placeholder的类型是不可以改变的
    feed_dict={x: [[0.7, 0.9]]}
'''
# seed?
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义palceholder作为存放输入数据的地方。这里维度也不一定要定义。
# 但如果维度是确定的，那么给出维度可以降低出错的概率
# x = tf.placeholder(tf.float32, shape=(1, 2), name="input")
x = tf.placeholder(tf.float32, shape=(3, 2), name="input")
# 暂时将输入的特征向量定义为一个常量。注意这里x是一个1*2的矩阵。
# x = tf.constant([[0.7, 0.9]])
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

'''
    cross_entropy定义了真实值与预测值之间的交叉熵，这是分类问题常用的损失函数。
    train_step定义了反向传播的优化方法。
    比较常用的优化方法有三种：tf.train.GradientDescentOptimizer、tf.train.AdamOptimizer、tf.train.MomentumOptimizer
'''
# 使用sigmoid函数将y转换为0~1之间的数值。转换后y代表预测是正样本的概率，1-y代表预测是负样本的概率
y = tf.sigmoid(y)
# 定义损失函数来刻画预测值与真实值之间的差距
cross_entropy = -tf.reduce_mean(
    y * tf.log(tf.clip_by_value(y, 1e-10, 1.0)) + (1 - y) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))
# 定义学习率
learning_rate = 0.001
# 定义反向传播算法来优化神经网络中的参数
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# 下面一行将会得到和3.4.3小节中一样的输出结果[[3.95757794]]
# print(sess.run(y, feed_dict={x: [[0.7, 0.9]]}))
# 因为x在定义的时候指定了n=3，所以在运行前向传播过程的时候是需要提供3个样例数据
print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
