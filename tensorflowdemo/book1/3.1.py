# coding=utf-8

import tensorflow as tf

# 计算图的使用
# TensorFlow中的每一个计算都是计算图上的一个节点
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b
# 通过a.graph可以查看张量所属的计算图，因为没有特意指定，所以这个计算图应该等于当前默认的计算图。所以下面这个操作的输出值为True
print(a.graph is tf.get_default_graph())
print(a.graph)
print(tf.get_default_graph())

# 除了使用默认的计算图，TensorFlow支持通过tf.Graph函数来生成新的计算图。不同计算图上的张量和运算都不会共享。
g1 = tf.Graph()
with g1.as_default():
    # 在计算图g1中定义变量"V"，并设置初始值为0
    v = tf.get_variable("v", initializer=tf.zeros_initializer()(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量"V"，并设置初始值为1
    v = tf.get_variable("v", initializer=tf.ones_initializer()(shape=[1]))

# 在计算图g1中读取变量"v"的取值。
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g1中，变量"V"的取值应该为0，所以下面这行会输出[0.]
        print(sess.run(tf.get_variable("v")))

# 在计算图g2中读取变量"v"的取值。
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # 在计算图g2中，变量"v"的取值应该为1，所以下面这行会输出[1.]
        print(sess.run(tf.get_variable("v")))

g = tf.Graph()
# 指定计算运行的设备
with g.device('/gpu:0'):
    result = a + b
