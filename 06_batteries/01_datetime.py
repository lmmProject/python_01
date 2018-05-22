from datetime import datetime
now = datetime.now()
# 2018-05-10 19:22:20.436335
print(now)


# 获取指定日期和时间
# 2015-04-19 12:20:00
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 当前时间就是相对于epoch time的秒数，称为timestam
t = dt.timestamp()
print(t)

print(datetime.fromtimestamp(t))


# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

print(cday)

print(datetime.now().strftime('%a, %b %d %H:%M'))

# datetime加减
from datetime import timedelta
dt = datetime(2015, 4, 19, 12, 20)
print(dt + timedelta(days=1))


# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。