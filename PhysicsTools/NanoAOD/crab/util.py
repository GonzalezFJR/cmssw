import datetime
def GetMonthName(n):
  if   n == 1 : return 'Jan'
  elif n == 2 : return 'Feb'
  elif n == 3 : return 'Mar'
  elif n == 4 : return 'Apr'
  elif n == 5 : return 'May'
  elif n == 6 : return 'Jun'
  elif n == 7 : return 'Jul'
  elif n == 8 : return 'Ago'
  elif n == 9 : return 'Sep'
  elif n == 10: return 'Oct'
  elif n == 11: return 'Nov'
  elif n == 12: return 'Dec'

def GetToday():
  now = datetime.datetime.now()
  today = str(now.day) + GetMonthName(now.month) + str(now.year)[2:]
  return today

def GetTimeNow():
  now = datetime.datetime.now()
  time = str(now.hour) + 'h' + str(now.minute) + 'm' + str(now.second) + 's'
  return time

