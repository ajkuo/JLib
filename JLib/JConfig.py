# coding: utf-8
import json
from datetime import datetime
from JLib import JModels

# Debug mode 設為 True 時，發生 Exception 時會顯示錯誤訊息。
DEBUG_MODE = True

# 是否開啟 Log 功能，可選擇存於 .txt 或資料庫(可同時開啟) 
SYSTEM_LOG_TO_TEXT_FILE = False
SYSTEM_LOG_TEXT_FILE_PATH = "/Log/"
SYSTEM_LOG_TO_DATABASE = False
SYSTEM_LOG_TABLE_NAME = "Log_System"
SYSTEM_DEFAULT_TIMEZONE = 8



# 用來統一載入/讀取回傳格式
class Rsp():
    def Dump(message, result=True, error=False, debug=None):
        return Rsp.Dumps(message, result, error, debug)


    def Dumps(message, result=True, error=False, debug=None):
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
            if error and Config.DEBUG_MODE:
                strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time, "debug": debug})
            else:
                strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time})       
        except:
            message = "Convert to JSON failed."
            result = False
            error = True  
            if DEBUG_MODE:
                strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time, "debug": debug})
            else:
                strJson = json.dumps({"message": message, "result": result, "error": error, "createTime": time})   
            
        return strJson

    def Load(message):
        return Rsp.Loads(message)

    def Loads(message):
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
                return JModels.RspJson(message, result, error, None, createTime)
            else:
                return JModels.RspJson(message, result, error, res["debug"], createTime)

        except Exception as ex:
            return Rsp.Dumps("[RspLoad] Failure", False, error=True, debug=str(ex))