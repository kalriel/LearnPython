import datetime

def FlexibleNumberArguments(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

dt = datetime.datetime.now()
nNum = dt.microsecond
FlexibleNumberArguments(nNum)