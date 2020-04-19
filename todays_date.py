
from datetime import datetime

from num2words import num2words


def todays_date():
    date = datetime.today().strftime("%Y-%m-%d")
    day = datetime.today().strftime("%d")
    month = datetime.today().strftime("%m")
    year = datetime.today().strftime("%Y")
    
    months = {"01":"January", "02":"Febuary", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}
    
    day = num2words(day, to='ordinal')
    
    
    result = "Today is " + str(months[month]) + " "+ str(day) + ", " + str(year) + "."
    
    return result