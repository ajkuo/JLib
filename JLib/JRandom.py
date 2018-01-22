# coding: utf-8
import random
from JLib.JConfig import Rsp 

def Randint(start=0, end):
    """
    隨機產生一個整數亂數
    """
    try:
        num = float(num)
        return Rsp.Dumps(math.floor(num), True)

    except Exception as ex:
        return Rsp.Dumps("[Floor] Failure", result=False, error=True, debug=str(ex))


def Rand():
    """
    隨機產生一個 0.0 - 1.0 之間的浮點數
    """
    try:
        rand = random.random()
        return Rsp.Dumps(str(rand), True)

    except Exception as ex:
        return Rsp.Dumps("[Rand] Failure", result=False, error=True, debug=str(ex))


def RandRange(start, end):
    """
    隨機產生一個 start - end 之間的浮點數
    """
    a = start
    b = end
    try:
        if start > end:
            a = end
            b = start
            
        rand = random.random()
        return Rsp.Dumps(str(rand), True)

    except Exception as ex:
        return Rsp.Dumps("[Rand] Failure", result=False, error=True, debug=str(ex))

