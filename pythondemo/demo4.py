# coding=utf-8

infos = []
print("初始化列表长度：%d，地址：%d" % (len(infos), id(infos)))
infos.append("Hello")
infos.insert(0, "1111")
print("追加后的长度为：%d，地址：%d，列表内容：%s" % (len(infos), id(infos), infos))
list_a = ["World", "I'm coming!"]
infos.extend(list_a)
print("追加后的长度为：%d，地址：%d，列表内容：%s" % (len(infos), id(infos), infos))
msgs = infos.copy()
print("列表长度：%d，地址：%d，列表内容：%s" % (len(msgs), id(msgs), msgs))
if "World" in msgs:
    print("执行数据删除remove函数：%s" % msgs.remove("World"))
print("删除后的列表内容：%s" % msgs)
del msgs[1]
print("删除后的列表内容：%s" % msgs)
print("执行数据删除pop()函数：%s" % msgs.pop(0))
print("删除后的列表内容：%s" % msgs)
msgs.extend(infos)
print("删除后的列表内容：%s" % msgs)
print("执行数据删除pop()函数：%s" % msgs.pop(0))
print("删除后的列表内容：%s" % msgs)
print("执行数据删除pop()函数：%s" % msgs.pop(0))
print("删除后的列表内容：%s" % msgs)
msg = []
for item in range(10):
    msg.append("Hello--%d" % item)
print("列表初始化内容：%s" % msg)
for item in range(len(msg)):
    print(msg)
    print(item)
    print("列表数据弹出：%s" % msg.pop(0))
