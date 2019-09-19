# coding=utf-8

import tensorflow as tf

# TensorFlow数据模型--张量
# 一个张量主要保存了三个属性：名字(name)，维度(shape)和类型(type)
sess = tf.Session()
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b
print(result)
print(sess.run(result))
