# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/6/26
# coding=utf-8
"""测试except的执行顺序

从前往后检查，一旦匹配就不再往下查找，即使下面的异常类型同样也匹配，而是执行finally, 再向调用栈的上层抛出。
"""


def func_raise():
    raise StopIteration


try:
    func_raise()
except BaseException as e:
    print("Base Exception happens.")
except BaseException as e:
    print("Base Exception happens.")
except StopIteration as e:
    print("StopIteration happens.")
except Exception as e:
    print("Exception happens!")
    print(str(e))
    print(e.__doc__)
    print(e.__repr__())
