import csv
import numpy
from matplotlib import pyplot

def stock_behavior():
 
  #The input file is 'table.csv'
  #Read the data into a list of dictionaries (stock_data)
  with open('table.csv','rb') as f:
    stock_data = [val for val in csv.DictReader(f,delimiter=',',quotechar="'")]

  #The dictionary entries in the table are:
  #Date,Open,High,Low,Close,Volume,Adj Close

  #For each date, find the day of the week
  for val in stock_data:
    val['Day'] = determine_day(val['Date'])

  #Compute the average volume traded by day of the week
  #traded_volume_dict
  traded_vol_dict = {}
  traded_vol_days = {}
  average_vol = []
  for val in stock_data:
    day = val['Day']
    traded_vol_dict[day] = traded_vol_dict.get(day,0) + float(val['Volume'])
    traded_vol_days[day] = traded_vol_days.get(day,0) + 1

  display_name = ['Monday','Tuesday','Wednesday','Thursday','Friday']
  average_vol = [traded_vol_dict[day]/float(traded_vol_days[day]) for day in display_name]
  print display_name
  
  

  #Plot the average volume by day in a bar chart
  fig = pyplot.figure()
  width = 0.35
  ind = numpy.arange(len(display_name))
  print ind
  pyplot.bar(ind,average_vol)
  pyplot.xticks(ind+width/2,display_name)
  pyplot.title('Average stock volume traded for Apple')
  fig.autofmt_xdate()
  fig.show()
  
  
    




def determine_day(date_string):
  #First take the date string and break it up by the dashes (year - month - date)
  date_pieces = date_string.split('-')

  #To do this, I need a reference.  I will choose Jan 1 1981
  year = int(date_pieces[0])
  month = int(date_pieces[1])
  date = int(date_pieces[2])

  #Add up the number of days since Jan 1 1981, due to the year difference
  #1980 was a leap year
  #Count the number of leap years
  num_leapyears = sum([isLeapYear(this_year) for this_year in range(1981,year)])
  num_years = year - 1981
  year_offset = num_years*365 + num_leapyears  #The 2nd term is the extra days from the leap year
 
  month_offset = 0
  #Number of days until the month is reached
  for mo in range(month-1):
    if (mo+1) == 1 or (mo+1) == 3 or (mo+1) == 5 or (mo+1)==7 or (mo+1)==8 or (mo+1) ==10 or (mo+1)==12:
      month_offset = month_offset + 31
    elif (mo+1) == 4 or (mo+1) == 6 or (mo+1) == 9 or (mo+1) == 11:
      month_offset = month_offset + 30
    elif (mo+1) == 2:
      #We need to figure out if it is a leap year to decide if we should add 28 or 29
      if isLeapYear(year):  #Leap year!
        month_offset = month_offset + 29
      else:
        month_offset = month_offset + 28
    else:
      print('There is a problem with the month')
      exit
  
  #The number of days in the current month is obtained directly from date (now an int)
  total_days = year_offset + month_offset + date
  #The offset of the reference date is "1" (no year/month offset, just date)
  if (total_days - 1)%7 == 0:
    day = "Thursday"
  elif (total_days - 1)%7 == 1:
    day = "Friday"
  elif (total_days - 1)%7 == 2:
    day = "Saturday"
  elif (total_days - 1)%7 == 3: 
    day = "Sunday"
  elif (total_days - 1)%7 == 4:
    day = "Monday"
  elif (total_days - 1)%7 == 5:
    day = "Tuesday"
  elif (total_days - 1)%7 == 6:
    day = "Wednesday"
  else: 
    print("There is a problem with the day")
  
  return day




#Return a logical: True if the tested year is a leap year; False if it is not.
def isLeapYear(year):
  #The year is a leap year if it can be divided by 4 but not 100.  The exception to this rule 
  #occurs when the number can be divided by 400.  
  if year%400 == 0:
    leapyear = True
  elif year%100 == 0:
    leapyear = False
  elif year%4 == 0:
    leapyear = True
  else:
    leapyear = False
  
  return leapyear
  

  
