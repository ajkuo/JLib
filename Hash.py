# coding: utf-8
import hashlib
from datetime import datetime, timedelta, timezone
from JLib import Config, Utils

    
def MD5(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.md5()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.digest(), encoding="utf-8")
        result = True
    except Exception as ex:
        message = "[MD5] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Utils.GetApiJson(message, result=result, error=error, debug=errorMessage)

    return jsonResult