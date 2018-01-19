# coding: utf-8
import time
from datetime import datetime, timedelta, timezone
from JLib import Config as config, Utils
from JLib import Math

def GetNowDatetime(offset=config.SYSTEM_DEFAULT_TIMEZONE):
    """
    預設時區為 UTC+8 ，可由 offset 參數做時區調整。
    傳入的 offset 乃基於 UTC 時間偏移，非基於預設時區偏移。
    """
    message = ""
    errorMessage = ""
    error = False
    result = False
    now = datetime.utcnow()
    now = now.replace(tzinfo=timezone.utc)
    try:
        now = now.astimezone(timezone(timedelta(hours=offset)))
        result = True
        message = str(now)
    except Exception as ex:
        message = "[GetNowDatetime] Failure"
        error = True
        result = False
        errorMessage = str(ex)

    jsonResult = Utils.GetApiJson(message, result=result, error=error, debug=errorMessage)
    return jsonResult

def GetTimestamp(offset=(config.SYSTEM_DEFAULT_TIMEZONE * 3600), floor=False):
    """
    回傳 Unix Timestamp
    預設時區依照 Config 設定，可傳入 offset 參數調整。
    offset: 偏移時間 (秒) -> 基於 UTC 時間偏移，非基於預設時區偏移。
    floor: 是否要移除小數點 (預設為 False)
    """
    try:
        ts = time.time() + offset
        if not floor:
            return Utils.GetApiJson(str(ts), True)
        else:
            res = Utils.RspLoad(Math.Floor(float(ts)))
            if not res.error:
                return Utils.GetApiJson(str(res.message), True)
            else:
                return Utils.GetApiJson("[GetTimestamp] Failure", False, error=True, debug=res.debug)


    except Exception as ex:
        return Utils.GetApiJson("[GetTimestamp] Failure", False, error=True, debug=str(ex))
     
def TimestampToDatetime(timestamp):
    """
    將 Unix Timestamp 轉換為 Datetime 形式呈現。
    """
    try:
        res = Utils.RspLoad(Math.Floor(float(timestamp)))
        if not res.error:
            timestamp = int(res.message)
            dt = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            return Utils.GetApiJson(str(dt), True)
        else:
            return Utils.GetApiJson("[TimestampToDatetime] Failure", False, error=True, debug=res.debug)

    except Exception as ex:
        return Utils.GetApiJson("[TimestampToDatetime] Failure", False, error=True, debug=str(ex))

