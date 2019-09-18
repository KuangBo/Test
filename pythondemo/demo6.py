# coding=utf-8

msgs = "www.baidu.com"
print("字符串的长度：%d" % len(msgs))
print("最大字符：%s" % max(msgs))
print("最小字符：%s" % min(msgs))
if "www" in msgs:
    print("www存在于msgs中！")
name = "www"
age = 18
info = ["kk", 18.525252, "China"]
infos = "姓名：{list_param[0]}，年龄：{list_param[1]}，住址：{list_param[2]}"
print(infos.format(list_param=info))
num = 10
num_a = 2522525
num_b = 8545466
strs = "www.baidu.com百度"
print("UNICODE编码：{info!a}".format(info=strs))
print("成绩：{info:6.2f}".format(info=98.2555252))
print("收入：{numA:G}，收入：{numB:E}".format(numA=num_a, numB=num_b))
print("二进制数据：{num:#b}".format(num=num))
print("八进制数据：{num:#o}".format(num=num))
print("十六进制数据：{num:#X}".format(num=num))
