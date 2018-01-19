#!/user/bin/env python
# -*- coding:utf-8 -*-

str_temp = 'test'
def foo():
    str_temp = 'test_foo'
    print 'locals',locals()

print 'globals',globals()

foo()
