# coding=utf-8

import tensorflow as tf

'''
    激励函数是使用所有神经网路算法的必备“神器”。激励函数的目的是为了调节权重和误差。
    在Tensorflow中，激励函数是作用在张量上的非线性操作。
    激励函数的使用方法和前面的数学操作相似。
    激励函数的功能有很多，但其主要是为计算图归一化返回结果而引进的非线性部分。
'''
sess = tf.Session()
# 整流线性单元ReLU，max(0, x)，每个数与0比较取最大
print(sess.run(tf.nn.relu([-3., 3., 10.])))
# ReLU6，min(max(0, x), 6)
print(sess.run(tf.nn.relu6([-3., 3., 10.])))
# sigmoid函数，表示为1/(1+exp(-x))，取值范围-1~1在机器学习训练过程中反向传播项趋近于0，不怎么使用
print(sess.run(tf.nn.sigmoid([-1., 0., 1.])))
# 双曲正切函数，取值范围0~1，(exp(x)-exp(-x))/(exp(x)+exp(-x))
print(sess.run(tf.nn.tanh([-1., 0., 1.])))
# softsign函数，表达式为x/(abs(x)+1)，是符号函数的连续估计
print(sess.run(tf.nn.softsign([-1., 0., 1.])))
# softplus函数是ReLU的平滑版，表达式为log(exp(x)+1)
print(sess.run(tf.nn.softplus([-1., 0., 1.])))
'''
    当输入增加时，softplus激励函数趋近于无限大，softsign函数趋近于1
    当输入减小时，softplus激励函数趋近于0，softsign函数趋近于-,ELU激励函数趋近于-1
'''
# ELU激励函数，表达式(exp(x)+1)if x<0 else x
print(sess.run(tf.nn.elu([-1., 0., 1.])))
print("我是好孩子")
