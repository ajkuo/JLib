# coding: utf-8
import sys, os
from JLib import Config as config, Utils


# 回傳目前工作目錄
def CurrentPath():
    try:
        path = os.getcwd()
        return Utils.GetApiJson(path, True)

    except Exception as ex:
        return Utils.GetApiJson("[CurrentPath] Failure", result=False, error=True, debug=str(ex))


# 回傳執行的腳本所在目錄
def CurrentScriptPath():
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        return Utils.GetApiJson(path, True)

    except Exception as ex:
        return Utils.GetApiJson("[CurrentScriptPath] Failure", result=False, error=True, debug=str(ex))


# 檢查指定路徑 or 檔案是否存在
def Exists(path):
    result = False
    try:
        if os.path.exists(path):
            result = True

        return Utils.GetApiJson("[Exists] Success", result)

    except Exception as ex:
        return Utils.GetApiJson("[Exists] Failure", result=False, error=True, debug=str(ex))


# 檢查指定目錄下是否有指定檔案
def FileExist(path, fileName):
    message = ""
    result = False
    try:
        if os.path.exists(path):
            if path[-1] != "/":
                path += "/"
            result = os.path.isfile(path + fileName) #如果不存在就返回False
            message = "[FileExist] Success"
        else:
            message = "Path not exist."

        return Utils.GetApiJson(message, result)

    except Exception as ex:
        return Utils.GetApiJson("[FileExist] Failure", result=False, error=True, debug=str(ex))
