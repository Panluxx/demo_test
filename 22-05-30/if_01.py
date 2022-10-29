# -*- coding: utf-8 -*-
# @Time     : 2021/1/21 22:12
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : if_01.py
# Software  : PyCharm


n = 0
for i in range(1, 101):
    n += i
print(n)

a = [5, 6, 7, 9, 10, 23, 45]
a.reverse()
print(a)
print(a[::-1])

# price = input('客户购买的价格为：')
# if not  price.isdigit():
#     print('输入值不合法！！！')
# else:
#     if 50 <= float(price) <= 100:
#         print('在这个范围内可优惠{:.0%}，最终的需要支付的金额为{:.2f}'.format((1 - 0.9), (0.9 * float(price))))
#     elif float(price) > 100:
#         print('在这个范围内可优惠{:.0%}，最终的需要支付的金额为{:.2f}'.format((1 - 0.8), (0.8 * float(price))))
#     else:
#         print('在这个范围内没有优惠，最终的需要支付的金额为{}'.format(float(price)))


n = 0
while n < 2:
    user = input('请输入你的性别1：男，2：女：')
    if user in '1,2':
        if user == '2':
            user_age = input('请输入你的年龄：')
            if user_age.isdigit():
                user_age = int(user_age)
                if 10 <= user_age <= 12:
                    print('你可以加入')
                else:
                    print('你不可以加入')
            else:
                print('输入的值非法')
        else:
            print('你是男生，不可以加入')
    else:
        print('请输入1，2选项')
    n += 1

# age = input("请输入你的年龄：")
# if age.isdigit():
#     age = int(age)
#     if 1 <= age <= 7:
#         print('儿童')
#     elif 8 <= age <= 17:
#         print('少年')
#     elif 18 <= age <= 30:
#         print('青年')
#     elif 31 <= age <= 59:
#         print('中年')
#     elif 60 <= age <= 100:
#         print('老年')
#     elif 100 < age <= 150:
#         print('寿星')
#     else:
#         print('年龄异常')
#
# else:
#     print('输入值非法')

# n = 0
# while True:
#     a = input('请输入数字')
#     if n == 1:
#         break
#     else:
#         n +=1
#         print(n)

# n = 0
# while n <= 1:
#     a = input('请输入数字')
#     n += 1
#     print(a)
