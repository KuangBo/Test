# coding=utf-8

import tensorflow as tf

# TensorFlow运行模型--会话

sess = tf.Session()
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b
with sess.as_default():
    print(result.eval())
print(sess.run(result))
print(result.eval(session=sess))

# tf.InteractiveSession()函数会自动将生成的绘画注册为默认会话
sess = tf.InteractiveSession()
print(result.eval())
sess.close()

# ConfigProto配置会话
config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
sess1 = tf.InteractiveSession(config=config)
sess2 = tf.Session(config=config)
