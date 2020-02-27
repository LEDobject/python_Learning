# -*- coding: utf-8 -*-
import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrap(*arg,**kw):
        sta = time.time()
        x=fn(*arg,**kw)
        end=time.time()
        last=end-sta
        print('%s executed in %s ms' % (fn.__name__, last))
        return x
    return wrap

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')
