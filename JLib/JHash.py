# coding: utf-8
import hashlib
from JLib import JConfig as config
from JLib.JConfig import Rsp

    
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
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

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
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

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
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

    return jsonResult


def SHA512(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.sha512()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[SHA512] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

    return jsonResult


def SHA3_256(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.sha3_256()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[SHA3_256] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

    return jsonResult


def SHA3_51(text):
    message = ""
    errorMessage = ""
    result = False
    error = False
    m = hashlib.sha3_512()
    try:
        text = bytes(text, encoding="utf8")
        m.update(text)
        message = str(m.hexdigest())
        result = True
    except Exception as ex:
        message = "[SHA3_512] Failure"
        errorMessage = str(ex)    
        result = False
        error = True
    
    jsonResult = Rsp.Dumps(message, result=result, error=error, debug=errorMessage)

    return jsonResult

