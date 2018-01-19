# coding: utf-8
import math
from JLib import Config as config, Utils

def Floor(num):
    """無條件捨去"""
    try:
        num = float(num)
        return Utils.GetApiJson(math.floor(num), True)

    except Exception as ex:
        return Utils.GetApiJson("[Floor] Failure", result=False, error=True, debug=str(ex))


def Ceil(num):
    """無條件進位"""
    try:
        num = float(num)
        return Utils.GetApiJson(math.ceil(num), True)

    except Exception as ex:
        return Utils.GetApiJson("[Ceil] Failure", result=False, error=True, debug=str(ex))


def Round(num):
    """四捨五入"""
    try:
        num = float(num)
        return Utils.GetApiJson(round(num), True)

    except Exception as ex:
        return Utils.GetApiJson("[Round] Failure", result=False, error=True, debug=str(ex))

