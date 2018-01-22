from JLib import JTime
from datetime import datetime


dt = datetime(1970, 1, 1, 17, 2, 43, 123)

print(datetime.strftime(dt, "%Y-%m-%d %H:%M:%S.%f"))

#print(JTime.TimestampToDatetime(1516406644.478761))