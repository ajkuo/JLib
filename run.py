# coding: utf-8
from JLib import JTime, JCheck, JModels
from JLib.JConfig import Rsp
import decimal
from datetime import datetime

str_list = [decimal.Decimal("1"),
            "", " ", datetime.now(),
             "123", 324, 0, -1.23, ["1", "easd"],
              [], ("1", "2"), (), {"k": "12"}, {},
               "3rfsdggjkld ", " r", None, "-12", True, "False", JModels.RspJson("123", True, True, "321", datetime.now())
            ]

for item in str_list:
    ts = JCheck.IsEmptyOrNull(item, True)
    res = Rsp.Loads(ts) 

    # print(ts)

    if not res.error:
        print(str(item).rjust(30, ".") + " >> RESULT: " + str(res.result).rjust(5, " ") + " (Error: " + str(res.error) + ")")

    else:
        print("{} [DEBUG] {}".format(res.message, res.debug))

print(decimal.Decimal("1"))
print(decimal.Decimal("1.2"))
print(decimal.Decimal("0.2"))
print(decimal.Decimal("21"))
print(str(decimal.Decimal(0.2)))