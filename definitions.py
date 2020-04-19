#definitions.py


from PyDictionary import PyDictionary

definitions_dictionary = PyDictionary()

def definitions(word):
    word = str(word)
    #get result
    result = definitions_dictionary.meaning(word)
    
    #result is type "dict". Format result.
    
    formatted_result = ""
    
    formatted_result += 'definition of "'
    formatted_result += word
    formatted_result += '":'
    formatted_result += "\n\n"
    
    for x in result:
        formatted_result += x
        formatted_result += ":"
        formatted_result += "\n"

        for y in range(len(result[x])):
            formatted_result += "   -  "
            formatted_result += str(result[x][y])
            formatted_result += "\n"
        
        formatted_result += "\n"
    
    return formatted_result