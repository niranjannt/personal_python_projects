print("This prints seconds to days, hours, minutes")
seconds=input("Please type in the number of seconds")
if int(seconds)>= 86400:
    days_seconds= int(seconds)/86400
    print(str(days_seconds) +' ' +  "days")
elif int(seconds) >= 3600:
    hours_seconds= int(seconds)/3600
    print(str(hours_seconds) +' ' +  "hours")
elif int(seconds) >=60:
     minutes_seconds= int(seconds)/60
     print(str(minutes_seconds) +' ' +  "minutes")
elif int(seconds) < 60:
      print(str(seconds) + ' ' + "seconds")
     
