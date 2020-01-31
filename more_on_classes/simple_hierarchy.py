#! /usr/bin/env python3.7

class MyClass():
    '''Parent is object.'''
    pass

class MyChildClass(MyClass):
    '''Parent is MyClass.'''
    pass

my_child_instance = MyChildClass()
my_class_instance = MyClass()

print(MyChildClass.__bases__)
print(MyClass.__bases__)
print(object.__bases__)

print(my_child_instance.__class__)

print(type(my_child_instance))
print(isinstance(my_child_instance, MyChildClass))
print(isinstance(my_child_instance, MyClass))
print(isinstance(my_child_instance, object))
