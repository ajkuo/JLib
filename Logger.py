# coding: utf-8
from JLib import Utils
from JLib import Config as config

# TODO: 尚未完成
def Write(source=None, actionType=None, actionContent=None, target=None, noteText=None, noteNum1=None, noteNum2=None, createTime=None):
    """
    傳入指定參數以寫進 Log 文字檔案及資料表(需在config設定, 否則就只會顯示而已)，參數如下：
    source: 必填，執行動作的來源，可能是帳號、姓名、程式名稱等，自訂一個可識別的字串。
    actionType: 必填，動作類型，對執行的動作做一個分類，可自定義，例如「SQL」、「File」等等。
    actionContent: 必填，動作內容，描述做了什麼事。
    target: (選填) 此動作的對象是誰，例如：交易紀錄的交易對象、買賣雙方的某一方。
    noteText: (選填) 文字備註，可以用來註記，亦可用作自訂欄位，例如將其充當為「幣別」、「地址」等。
    noteNum1: (選填) 數字備註1，自訂用途，可以用來當作交易金額、手續費等。
    noteNum2: (選填) 數字備註2，同上。
    createTime: (選填) 動作發生時間，預設為當下(Now)，並以系統預設時區為準。
    """
    message = ""
    jsonResult = ""
    file_result = False
    db_result = False

    if source is None:
        message = "Log argument 'source' is required."  
    elif actionType is None or actionContent is None:
        message = "Log arguments 'actionType' and 'actionContent' are required."
    else:
        if createTime is None:
            createTime = Utils.GetNowDatetime()

        # 寫進文件檔
        if config.SYSTEM_LOG_TO_TEXT_FILE:
            try:

            # Open (path=config.SYSTEM_LOG_TEXT_FILE_PATH, name=以日期區分檔名)     
            # Write
            # Close

                message += "[FILE] Success "
                file_result = True          
            except Exception as ex:
                message += "[FILE] Failure "
                if config.DEBUG_MODE:
                    message += "[FILE_DEBUG] '{0}' ".format(str(ex))      
                    file_result = False          
        else:
            message += "[FILE] Pass "
            file_result = True     

        # 寫進資料庫
        if config.SYSTEM_LOG_TO_DATABASE:
            try:
                tableName = config.SYSTEM_LOG_TABLE_NAME
                SQL = "INSERT INTO {0}(Source, ActionType, ActionContent, Target, NoteText, NoteNum1, NoteNum2, CreateTime) VALUES('{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8});".format(tableName, source, actionType, actionContent, target, noteText, noteNum1, noteNum2, createTime) 
                # Connect to database.
                # Run SQL
                # Disconnect.
                # Done.
                
                message += "[DATABASE] Success "
                db_result = True
            except Exception as ex:
                message += "[DATABASE] Failure "
                if config.DEBUG_MODE:
                    message += "[DATABASE_DEBUG] '{0}' ".format(str(ex))
                    db_result = False          
        else:
            message += "[DATABASE] Pass "
            db_result = True
    
    if file_result and db_result:
        jsonResult = Utils.GetApiJson(message, result=True, time=createTime)
    else:
        jsonResult = Utils.GetApiJson(message, result=False, error=True)
        
    return jsonResult

