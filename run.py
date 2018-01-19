# coding: utf-8
from JLib import JTime
from JLib.JConfig import Rsp

res = Rsp.Loads(JTime.GetTimestamp()) 

if not res.error:
    print(res.message)
    
else:
    print("{} [DEBUG] {}".format(res.message, res.debug))