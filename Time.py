# coding: utf-8
from datetime import datetime, timedelta, timezone
from JLib import Config as config, Utils

def GetNowDatetime(offset=config.SYSTEM_DEFAULT_TIMEZONE):
    """預設時區為 UTC+8 ，可由 offset 參數做時區調整。"""
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