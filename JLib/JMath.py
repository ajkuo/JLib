# coding: utf-8
import math
from JLib.JConfig import Rsp 

def Floor(num):
    """無條件捨去"""
    try:
        num = float(num)
        return Rsp.Dumps(math.floor(num), True)

    except Exception as ex:
        return Rsp.Dumps("[Floor] Failure", result=False, error=True, debug=str(ex))


def Ceil(num):
    """無條件進位"""
    try:
        num = float(num)
        return Rsp.Dumps(math.ceil(num), True)

    except Exception as ex:
        return Rsp.Dumps("[Ceil] Failure", result=False, error=True, debug=str(ex))


def Round(num):
    """四捨五入"""
    try:
        num = float(num)
        return Rsp.Dumps(round(num), True)

    except Exception as ex:
        return Rsp.Dumps("[Round] Failure", result=False, error=True, debug=str(ex))


