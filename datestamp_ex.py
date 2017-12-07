import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dateTime = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    re_tz = re.match(r'(UTC)([+-]\d+)([:]\d+)',tz_str)
    tz_utc_num = int(re_tz.group(2))
    new_tz_utc = timezone(timedelta(hours=tz_utc_num))
    new_dt = dateTime.replace(tzinfo=new_tz_utc)
    timestp = new_dt.timestamp()
    print(timestp)
    return timestp




# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')