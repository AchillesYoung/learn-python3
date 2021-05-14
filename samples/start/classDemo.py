# author=shuyang

class Bsum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self,c):
        return self.a+self.b+c


a = Bsum(1,2).sum(3)

print(a)

# 类的结构
class Human:
    """类的结构"""
    def __init__(self, name, eyes):
        """构造方法"""
        self.name = name
        self.eyes = eyes

    def look(self, what):
        x = '{}用{}只眼睛看{}'.format(self.name, self.eyes, what)
        return x

# # 将类实例化为对象
# xiaoming = Human('小明', 2)
# print(xiaoming.name)  # 调用对象属性
# print(xiaoming.look('世界'))  # 调用对象方法
#
# # 实例化其他对象
# erlang = Human('二郎', 3)
# print(erlang.look('猴儿！'))
#
# one_eyes = Human('独眼巨人', 1)
# print(one_eyes.look('俄底修斯'))


# 类属性和实例属性
class A:
    """类属性和对象属性"""

    # 类属性
    a1 = 0

    # 实例属性
    def __init__(self):
        self.a2 = 1

    def aaa(self):
        pass

A.a1  # 类属性可以不实例化直接调用
# A.a2  # 出错，实例属性不能直接调用

class1 = A()  # 类实例化为对象class1
class1.a1, class1.a2  # 输出实例属性，(0, 1)

class2 = A()  # 类实例化为对象class2
class2.a1, class2.a2  # 输出实例属性，(0, 1)

# 修改类属性和实例属性
A.a1 = 2
A.a2 = 3  # 并非修改实例属性，实际上是创建了一个新的类属性，因为原实例属性类无法直接访问
A.a1, A.a2  # (2, 3)

# 改后类属性跟着改变，实例属性未变，类和实例隔离
class1.a1, class1.a2  # (2, 1)
class2.a1, class2.a2  # (2, 1)

# 修改实例1属性
class1.a1 = 4  # 这里是创建了一个新实例属性a1,并非修改类属性a1
class1.a2 = 5
class1.a1, class1.a2  # (4, 5)

A.a1, A.a2  # 修改实例1属性后，类属性未变(2, 3)

class2.a1, class2.a2  # 修改实例1属性后，实例2属性未变，(2, 1)

# 主要属性和方法
print(A.__dict__)
print(class1.__dict__)
print(class2.__dict__)
#
# # 全部属性和方法
print(dir(A))
print(dir(class1))
print(dir(class2))

class A:
    """类方法、实例方法、静态方法"""

    # 类属性
    a1 = 0

    # 实例属性
    def __init__(self):
        self.a2 = 1

    # 静态方法
    @staticmethod
    def d():
        return '不能调用类和实例属性'

    # 类方法
    @classmethod
    def b(cls):
        """类方法，加装饰器，cls代表类本身"""
        return cls.a1

    # 实例方法
    def c(self):
        """self代表实例本身"""
        return self.a1, self.a2


# 公开和私有

class Abc:

    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def aa(self):
        print(self.__b)
        return '公开方法'


    def __bb(self):
        return '私有方法'

x = Abc('公开属性', '私有属性')
print(x.a)
#print(x.__b)
print(x.aa())
print(x._Abc__b)
print(x.aa())
#print(x.__bb())
print(x._Abc__bb())

print(dir(x))