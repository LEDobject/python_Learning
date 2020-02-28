# -*- coding: utf-8 -*-
import functools,time
'''
def log(fn=None):
    @functools.wraps(fn)
    def sta(fn):
        try:
            print("%s begin call at %s" % (fn,time.time()))
            x=fn()
            print('%s end call at %s' % (fn,time.time()))
            return x
        except:
            print("begin call at %s" % (time.time()))
            x = fn()
            print('end call at %s' % (time.time()))
            return x

    return sta
'''
def log(fn1):
    if isinstance(fn1,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args,**kw):
                print('%s %s():' % (fn1, fn.__name__))
                print('begin call %s' % fn.__name__)
                fn(*args,**kw)
                print('end call %s' % fn.__name__)
                return fn
            return wrapper
        return decorator
    else:
        @functools.wraps(fn1)
        def wrapper(*args,**kw):
            print('begin call %s' % fn1.__name__)
            fn1(*args,**kw)
            print('end call %s' % fn1.__name__)
            return fn1
        return wrapper
#Test
@log
def f():
    print('I\'m Blank')
    return
f()
@log('execute')
def f():
    print('I\'m With Variaty')
    return
f()