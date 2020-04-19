from datetime import datetime


def current_time():
    
  now = datetime.now()
  current_time = now. strftime("%H:%M:%S")
    
  current_time = current_time[-4::-1]
  current_time = current_time[::-1]
    
  nums=["zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", 
        "fourteen", "fifteen", "sixteen",  "seventeen", 
        "eighteen", "nineteen",  "twenty", "twenty one", 
        "twenty two",  "twenty three", "twenty four",  
        "twenty five",  "twenty six", "twenty seven", 
        "twenty eight", "twenty nine", "thirty",
        "thirty one","thirty two","thirty three",
        "thirty four","thirty five","thirty six",
        "thirty seven","thirty eight","thirty nine",
        "forty","forty one","forty two","forty three",
        "forty four","forty five","forty six",
        "forty seven","forty eight","forty nine",
        "fifty"
        ]
    
  if (int(current_time[0:2]) > 12):
    pm = True
  else:
    pm = False
    
    
  if pm:
    hour = int(current_time[0:2])
    minute = int(current_time[3:5])

    hour -= 12
        
    current_time = str(hour) + ":" + str(minute) + " p.m."
        
    return current_time
    
  else:
    current_time += " a.m."
    return current_time
    