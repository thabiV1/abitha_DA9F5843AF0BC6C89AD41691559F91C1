year = int(input('Enter any year:'))
if year % 400 == 0 and year%100==0:
  print('It is leap year')
elif year%4==0 and year%100!=0:
  print('It is year')
else:
  print('It is not a leap year')
