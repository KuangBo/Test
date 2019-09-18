# coding=utf-8

infos = ("Hello", "World")*2 + ("I'm", "coming")
for item in infos:
    print(item, end="、")
print(type(infos))

list_a = ["Hello", "World", "I'm coming"]
msgs = tuple(list_a)
print("list_a的变量类型：%s，内容为：%s" % (type(list_a), list_a))
print("msgs的变量类型：%s，内容为：%s" % (type(msgs), msgs))
list_b = list(msgs)
print("list_b的变量类型：%s，内容为：%s" % (type(list_b), list_b))
list_c = [True, 1, None]
print(any(list_c))
print(all(list_c))
