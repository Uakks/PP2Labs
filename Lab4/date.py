from datetime import datetime, date, time, timedelta
import datetime
# 1
date = date.today() - timedelta(days=5)
# print(date)

# 2
d2 = date.today()
d1 = date.today() - timedelta(days=1)
d3 = date.today() + timedelta(days=1)
# print(f"Yesterday - {d1}, today - {d2}, tomorrow - {d3}")

# 3
d4 = datetime.datetime.now()
# print(d4.strftime("%d/%m/%Y, %H:%M:%S"))

# 4
d5 = datetime.datetime(year=int(input("Enter year for first date: ")),
                       month=int(input("Enter month for first date: ")),
                       day=int(input("Enter day for first date: ")),
                       hour=int(input("Enter hours for first date: ")),
                       minute=int(input("Enter minutes for first date: ")),
                       second=int(input("Enter seconds for first date: "))
                       )
d6 = datetime.datetime(year=int(input("Enter year for second date: ")),
                       month=int(input("Enter month for second date: ")),
                       day=int(input("Enter day for second date: ")),
                       hour=int(input("Enter hours for second date: ")),
                       minute=int(input("Enter minutes for second date: ")),
                       second=int(input("Enter seconds for second date: "))
                       )
# print(f"Difference between two dates - {abs(timedelta.total_seconds(d5 - d6))} s")
