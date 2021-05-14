# author=shuyang

class A:
    """父类"""
    a1 = 1

    def __init__(self):
        self.b1 = 2

    def c1(self):
        return self.b1


class B(A):
    pass

b = B()
print(b)
print(b.a1)
print(b.b1)
print(b.c1())

# class B2(A):
#     def __init__(self):
#         super(B2, self).__init__()  # 显示引入父类初始化函数
#         self.b2 = 123
# b2 = B2()
# print(b2.b2)
# print('none')
# print(b2.b1)  # 覆盖了

class B3(A):
    a1 = 4

    def __init__(self):
        super(B3, self).__init__()  # 显示引入父类初始化函数
        self.b2 = 20

    def c1(self):
        print(self.a1)  # 调用子类的属性
        print(super(B3, self).a1)  # 调用父类的同名属性
        print(super(B3, self).c1())  # 调用父类同名方法

varb3 = B3()
print(varb3.b1)
print(B3.a1)
print(varb3.b2)
varb3.c1()

#multi extends
class A:
    def show(self):
        print('A的show')

class B(A):
    def show(self):
        print('B的show')

class C(A):
    def show(self):
        print('C的show')

class D(B, C):
    pass

d = D()
d.show()
print(D.__mro__)