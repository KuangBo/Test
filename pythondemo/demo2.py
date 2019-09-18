# coding=utf-8

age = 12
assert 11 <= age <= 25, "age变量处理结果错误！"
print("年龄：%d" % age)

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
else:
    print("结束了")
print(sum)

num_a = 0
num_b = 1
while num_b < 1000:
    print(num_b, end="、")
    num_a, num_b = num_b, num_a + num_b
print()
q, p = 10, 19
print(q, p)

for x in range(50, 100, 3):
    print(x, end="、")

msg = "HelloWorld!"
for i in msg:
    print(i, end="|")
print()
for i in msg:
    if 97 <= ord(i) <= 122:
        uppper = ord(i) - 32
        print(chr(uppper), end="、")
    else:
        print(i, end="、")
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i, end="、")
print()
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end="\t")
    print()
line = 5
for i in range(line):
    print(" " * (line - i), end=" ")
    print("*" * (i + 1))
