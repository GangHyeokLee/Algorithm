import datetime as dt

m, d = map(int, input().split())

day = dt.datetime(2007, m, d)
print(day.strftime('%A').upper()[:3])