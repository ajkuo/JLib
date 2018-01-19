# coding: utf-8
from JLib import JTime
from JLib.JConfig import Rsp

ts = JTime.GetTimestamp()
res = Rsp.Loads(ts) 
print(ts)
if not res.error:
    print(res.message)
else:
    print("{} [DEBUG] {}".format(res.message, res.debug))