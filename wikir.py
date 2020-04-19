import wikipedia


def wikir(query):

    #Extract meaningful content from query
    verb_index = 2
    meaningful_content = query[verb_index:]
    meaningful_content = " ".join(meaningful_content) 
    try:
        result = wikipedia.summary(meaningful_content, sentences = 1)
        #convert result into a breakable string
        converted_result = ""
        for x in range(len(result)):
            converted_result += result[x]
        return converted_result
    
    except:
        #Reformat the split query to a string
        query = " ".join(query)
        result = "Sorry, no page was found matching the query for " + str (query)
        return result