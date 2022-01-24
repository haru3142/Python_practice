import datetime

today = datetime.datetime.now()
n = int(input("何日後を表示しますか"))
answer = today + datetime.timedelta(days = n)
print(answer)