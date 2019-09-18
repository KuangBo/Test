# coding=utf-8

num_a = 29222222.151215251215
num_b = 25.54
print("数字一：%f，数字二：%f" % (num_a, num_b))
print("数字一：%5.2f，数字二：%10.2f" % (num_a, num_b))
print("数字一：%5.2f，数字二：%010.2f" % (num_a, num_b))
name = "xiaoming"
age = 18
score = 100.8
print("姓名：%s，年龄：%d，成绩：%6.2f" % (name, age, score))
print("姓名：%(name)s，年龄：%(age)d，成绩：%(score)6.2f" % vars())
result1 = (1 + 2) * (5 / 2)
result2 = (1 + 2) * (5 // 2)
print(result1)
print(result2)
print(4/2)
result = 10 == 10
print("结果：%s" % result)
print("结果：%d" % result)
print("a：%d" % ord('a'))
print("A：%d" % ord('A'))
aa = -1 <= 1 <= 19
print(aa)
bb = 25
print(type(bin(bb)))
print(type(oct(bb)))
print(type(int(bb)))
print(type(hex(bb)))
print(bin(bb))
print(oct(bb))
print(int(bb))
print(hex(bb))
q = 10
p = 10
print(q == p)
print(id(q))
print(id(p))
print(id(10))
print(id(11))
num_int = 100
num_float = 100.0
print(id(num_int))
print(id(num_float))
print(num_int == num_float)
print(num_int is num_float)
