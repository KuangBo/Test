# coding=utf-8

import tensorflow as tf
import numpy as np

my_var = tf.Variable(tf.zeros([2, 3]))
sess = tf.Session()
initialize_op = tf.global_variables_initializer()
print(sess.run(initialize_op))

sess = tf.Session()
x = tf.placeholder(tf.float32, shape=[2, 2])
y = tf.identity(x)
x_vals = np.random.rand(2, 2)
print(sess.run(y, feed_dict={x: x_vals}))
