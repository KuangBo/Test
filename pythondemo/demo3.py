# coding=utf-8

list_c = ["I'm coming", "What"]
list_a = ["hello", "world", "beautiful"] + list_c
list_b = None
print("第一个列表的地址%d，对应的数据类型%s" % (id(list_a), type(list_a)))
print("第二个列表的地址%d，对应的数据类型%s" % (id(list_b), type(list_b)))
print(list_a[-1] == list_a[2])
print(type(list_a[-1]))
print(type(list_a[1]))
print(type(list_a[0]))
list_a[0] = "hello"
for item in list_a:
    print(item, end="、")
print(len(list_a))
list_a_1 = list_a[3:10]
list_a_2 = list_a[:2]
list_a_3 = list_a[1:]
list_a_4 = list_a[:-1]
list_a_5 = list_a[-2:]
print(list_a_1)
print(len(list_a_1))
print(list_a_2)
print(list_a_3)
print(list_a_4)
print(list_a_5)
list_a[1:5:2] = ["111", "222"]
print(list_a)
if "111" in list_a:
    print("111在list_a中")
