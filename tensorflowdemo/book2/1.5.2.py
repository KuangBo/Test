# coding=utf-8

import tensorflow as tf
import numpy as np

sess = tf.Session()
identity_matrix = tf.diag([1.0, 1.0, 1.0])
var = tf.Variable(identity_matrix)
A = tf.truncated_normal([2, 3])
B = tf.fill([2, 3], 5.0)
C = tf.random_uniform([3, 2])
D = tf.convert_to_tensor(np.array([[1., 2., 3.], [-3., -7., -1.], [0., 5., -2.]]))
print(sess.run(identity_matrix))
print(sess.run(A))
print(sess.run(B))
print(sess.run(C))
print(sess.run(D))

# 矩阵的加减法
print(sess.run(A+B))
print(sess.run(B-B))
# 矩阵乘法 Multiplication
print(sess.run(tf.matmul(B, identity_matrix)))
# 矩阵转置
print(sess.run(tf.transpose(C)))
# 计算矩阵行列式
print(sess.run(tf.matrix_determinant(D)))
# 矩阵的逆矩阵
print(sess.run(tf.matrix_inverse(D)))
# 矩阵分解法
print(sess.run(tf.cholesky(identity_matrix)))
# 求解矩阵的特征值与特征向量
print(sess.run(tf.self_adjoint_eig(D)))
