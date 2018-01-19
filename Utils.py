# coding: utf-8
import json
from datetime import datetime
from JLib import Config as config
from JLib import Time
from JLib.Models import RspJson
    

def GetApiJson(message, result=True, error=False, debug=None):
    """
    將內容轉換為統一的 JSON 格式，說明如下：
    message：回傳之內容，若是失敗，必為一段文字。
    result：(Optional) 此結果為成功或失敗，預設為 True。
    error：(Optional) 是否發生錯誤，若為 True 表示發生錯誤。
    debug: (Optional) 傳入錯誤原因(Exception)，只在 Debug mode 下回傳。
    """
    strJson = ""
    time = "{} (UTC)".format(str(datetime.utcnow()))
    
    try:
        if error and config.DEBUG_MODE:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time, "debug": debug})
        else:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time})       
    except:
        message = "Convert to JSON failed."
        result = False
        error = True  
        if config.DEBUG_MODE:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time, "debug": debug})
        else:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time})   
        
    return strJson

def RspLoad(message):
    """
    將統一 JSON 格式轉為物件回傳，方便調用。
    回傳物件包含四項屬性：
    message、result、error 及 debug
    其中，若 error = False 或 Config 內 DEBUG_MODE = False，
    則 debug 必為 None
    """
    try:
        res = json.loads(message)
        message = res["message"]
        result = res["result"]
        error = res["error"]
        createTime = res["createTime"]
        if "debug" not in res:
            return RspJson(message, result, error, None, createTime)
        else:
            return RspJson(message, result, error, res["debug"], createTime)

    except Exception as ex:
        return GetApiJson("[RspLoad] Failure", False, error=True, debug=str(ex))