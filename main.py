
#imports
from wikir import *                  #1)  Wikipedia
from translator import *             #2)  Translator
from current_time import *           #3)  Current Time
from ip_address import *             #4)  IP Address
from math_solver import *            #5)  Math
from birthday_finder import *        #6)  Birthday Finder
from deathday_finder import *        #7)  Deathday Finder
from tongue_twisters import *        #8)  Tongue Twisters
from todays_date import *            #9)  Today's Date
from capitals import *               #10) Capitals
from definitions import *            #11) Definitions
                                     #12) Synonyms
                                     #13) Antonyms
                                     #14) Urban Dictionary Definition
                                     #14) Country Currencies
                                     #15) Country Time Zones
                                     #16) Country Languages
                                     #17) Country Boarders



#Greeting
print("Hello.")

#Run
repeat = True
while repeat:
  #Get query
  query = input("Type: ")
  unformatted_query = query
  #Format query from a string to a lowercase list of words
  query = query.lower()
  #Remove punctuation
  punct = ["?","."]
  if (query[-1] in punct):
      query = query[0:-1]
  
  query = query.split()


  #----------CURRENT_TIME-------------
  if ("time" in query):
    result = current_time()
  #-----------------------------------
        
        
  #----------WIKIPEDIA----------------
  elif (query[0] == "who") or (query[0] == "whom"):
    if (len(query) > 2):
      if (query[1] == "is") or (query[1] == "are") or (query[1]):
        result = wikir(query)  #Wikipedia
      else:
        result = "Sorry, I don't think that question made sense."
    else:
      result = "Sorry, I don't think that question made sense."
  #-----------------------------------
    
    
  #----------TRANSLATOR--------------
  elif(query[0] == "translate"):
    result = translator(query)
  #----------------------------------
    
    
  #----------IP_ADDRESS--------------
  elif(("my" in query) and ("ip" in query)):
    result = ip_address()
  #---------------------------------
  
  #-------------MATH----------------
  elif((unformatted_query[0] == "(") or (str.isdigit(unformatted_query[0]))):
      result = math_solver(unformatted_query)
  #---------------------------------

  #-----------BIRTHDAY--------------
  elif("birthday" in query or "born" in query):
      first_name = query[2]
      if len(query) >= 4:
          last_name = query[3]
      else:
          last_name = ""
      name = first_name + " " + last_name
          
      result = birthday_finder(name)
  #---------------------------------   
      
  #-----------DEATHDAY--------------
  elif(query[0:2] == ["when","did"]) and (query[-1] == "die"):
      first_index = 2
      current_index = first_index
      last_index = len(query)-1
      name = ""
      while (current_index < last_index):
          name += str(query[current_index])
          name += " "
          current_index += 1
      result = deathday_finder(name)
  #--------------------------------- 
  
  #-------TONGUE_TWISTERS-----------
  elif("tongue" in query and "twister" in query):
      result = tongue_twisters()
  #---------------------------------
  
  #--------TODAYS_DATE--------------
  elif("today's" in query and "date" in query):
      result = todays_date()
  #---------------------------------
      
  #--------COUNTRY_CAPITALS---------
  elif(query[0:5] == ["what","is","the","capital","of"]):
      result = capitals(query)
  #---------------------------------
  
  #----------DEFINITIONS------------
  elif(query[0:5] == ["what","is","the","definition","of"]):
      result = definitions(query[-1])
  #---------------------------------
      
  

  #-------------QUIT------------------
  elif((len(query) == 1) and (query[0] == "quit")):
    repeat = False
    result = "Goodbye."


  #-------------IDK------------------
  else:
    result = "Sorry, I don't know what to do with that question yet."
  #----------------------------------





  #Print----------
  print()
  print(result)
