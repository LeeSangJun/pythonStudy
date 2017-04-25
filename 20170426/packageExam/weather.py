from sources import daily, weekly
from sources.daily import forecast as df
#이건 에러
#from sources import daily.forecast as ddff, weekly
print("Dayly forcaset", daily.forecast())
print("Dayly forcaset__", df())
print("Dayly forcaset__", ddff())
print("Weekly forecast")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

'''
form 패키지명  import 듈명
'''