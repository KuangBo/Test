# coding=utf-8

import tensorflow as tf

sess = tf.Session()
weights = tf.Variable(tf.random_normal([2, 3], stddev=2))
biases = tf.Variable(tf.zeros([3]))
ww2 = tf.Variable(weights.initialized_value())
ww3 = tf.Variable(weights.initialized_value() * 2.0)

print(sess.run(weights.initializer))

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1), name="w1")
w2 = tf.Variable(tf.random_normal([2, 3], dtype=tf.float64, stddev=1), name="w2")
# w1.assign(w2)
q1 = tf.Variable(tf.random_normal([2, 3], stddev=1), name="q1")
q2 = tf.Variable(tf.random_normal([2, 2], stddev=1), name="q2")
# tf.assign(q1, q2)
tf.assign(q1, q2, validate_shape=False)
