
#Import APIs
from googletrans import Translator


#query = "translate to __(Language2)__  __(Sentence)__" 



def translator(query):
  #Create translator object
  translator = Translator()
    
  #Determine language2
  language2 = query[2]
    
    
  langs = {
             "arabic":"ar",      "catalan":"ca",
             "danish":"da",      "dutch":"nl",
             "english":"en",     "finish":"fa",      
             "french":"fr",      "italian":"it",   
             "german":"de",      "greek":"el",
             "hawaiian":"haw",   "hindi":"hi",
             "icelandic":"is",   "portugese":"pt",
             "indonesian":"in",  "icelandic":"is",
             "italian":"it",     "irish":"ga",
             "galic":"ga",       "japanese":"ja",
             "javanese":"jw",    "korean":"su",
             "latin":"la",       "georgian":"co",   
             "latvian":"lv",     "lithuanian":"lt", 
             "macedonian":"bg",  "mongolian":"ta",  
             "matlese":"mt",     "norwegian":"no",
             "polish":"pl",      "russian":"ru",   
             "samoan":"sm",      "slovak":"sk",
             "somali":"so",      "albanian":"sq",
             "serbian":"hr",     "sundanese":"su",  
             "swedish":"sv",     "swahili":"sw", 
             "turkish":"tr",     "usbek":"uz",
             "vietnamese":"vi",  "welsh":"cy",
             "zulu":"zu"
            }
    
  try:
    language2 = langs[language2]
  except:
    return "Sorry, I cannot make the translation."
    
    
  content = query[3:]
  content = " ".join(content)
    

  translation = translator.translate(content,dest=language2)
    
  translation = str(translation)
  translation = translation[33:]
  index = 0
  content = ""
  while (content != ","):
    index +=1
    content = translation[index]

  translation = translation[:index]
        
  return translation
