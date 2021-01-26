def dayOfProgrammer(year):
  if(year%400==0):
    feb=29
  elif(year%100==0):
    feb=28
  elif(year%4==0):
    feb=29
  else:
    feb=28
  n=215+feb
  pd=256-n
  print(f"{pd}.09.{year}")

n=int(input())
dayOfProgrammer(n)