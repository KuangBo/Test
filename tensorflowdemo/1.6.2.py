# coding=utf-8

import tensorflow as tf

sess = tf.Session()
print(sess.run(tf.div(3, 4)))
print(sess.run(tf.truediv(3, 4)))
print(sess.run(tf.floordiv(3.0, 4.0)))
print(sess.run(tf.mod(22.0, 5.0)))
# 计算两个张量间的点积，点积函数只为三位向量定义，cross()函数以两个三位张量作为输入
print(sess.run(tf.cross([1., 0., 0.], [0., 1., 0.])))
# Tangent function (tan(pi/4) = 1)
print(sess.run(tf.div(tf.sin(3.1416/4.), tf.cos(3.1416/4.))))


# 自定义二次多项式函数
def custom_ploynomial(value):
    return tf.subtract(3 * tf.square(value), value) + 10


print(sess.run(custom_ploynomial(11)))
