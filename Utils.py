# coding: utf-8
import json
from datetime import datetime
from JLib import Config as config
from JLib import Time
    

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
        if econfig.DEBUG_MODE:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time, "debug": debug})
        else:
            strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time})   
        
    return strJson

