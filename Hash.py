# coding: utf-8
import hashlib
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
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[MD5] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Utils.GetApiJson(message, result=result, error=error, debug=errorMessage)

    return jsonResult
   

def SHA1(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.sha1()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[SHA1] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Utils.GetApiJson(message, result=result, error=error, debug=errorMessage)

    return jsonResult 


def SHA256(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.sha256()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[SHA256] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Utils.GetApiJson(message, result=result, error=error, debug=errorMessage)

    return jsonResult