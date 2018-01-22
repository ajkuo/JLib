# coding: utf-8
import random
from JLib.JConfig import Rsp 

def IsNumerical(num):
    """
    傳入一個變數，檢查是否為數值
    """
    try:
        x = float(num)
        return Rsp.Dumps("[IsNumerical] Success", True)
    except ValueError:
        return Rsp.Dumps("[IsNumerical] Success", False)
    except Exception as ex:
        return Rsp.Dumps("[IsNumerical] Failure", result=False, error=True, debug=str(ex))


def IsEmptyOrNull(value, ignore_whitespace=False):
    """
    傳入一個任何型態的變數，檢查是否為空值或 Null (即 None )，若為空則回傳 True
    預設不會忽略空白，如果要忽略空白請將 ignore_whitespace 設為 True
    """
    try:
        # 先檢查是否為 None，以免發生錯誤
        if value is None:
            return Rsp.Dumps("[IsEmptyOrNull] Success", True)

        # 檢查是否為數值型態，若是則不能進下一個判斷，因數值型態不能用 len() 判斷長度
        elif Rsp.Loads(IsNumerical(value)).result:
            return Rsp.Dumps("[IsEmptyOrNull] Success", False)

        # 再來要檢查是否為 List, Tuple, Dict 等型態，以免發生錯誤。
        elif isinstance(value, (list, tuple, dict)):
            if len(value) == 0:
                return Rsp.Dumps("[IsEmptyOrNull] Success", True)
            else:
                return Rsp.Dumps("[IsEmptyOrNull] Success", False)

        # 最後將變數轉為字串，並依照是否忽略空白來判斷字串長度。
        else:
            value = str(value)
            if ignore_whitespace:
                if len(value.strip()) == 0:
                    return Rsp.Dumps("[IsEmptyOrNull] Success", True)
                else:
                    return Rsp.Dumps("[IsEmptyOrNull] Success", False)
            else:
                if len(value) == 0:
                    return Rsp.Dumps("[IsEmptyOrNull] Success", True)
                else:
                    return Rsp.Dumps("[IsEmptyOrNull] Success", False)
    except Exception as ex:
        return Rsp.Dumps("[IsEmptyOrNull] Failure", result=False, error=True, debug=str(ex))



