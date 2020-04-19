
import wikipedia


def deathday_finder(name):
    
    try:
        result = wikipedia.summary(name, sentences = 1)
        
        #convert result into a breakable string
        converted_result = ""
        for x in range(len(result)):
            converted_result += result[x]
            
        #find birthday and deathday in string
        left_parenthesis_index = None
        dash_index = None
        right_parenthesis_index = None
        for x in range(len(converted_result)):
            if (converted_result[x] == "(") and (left_parenthesis_index == None):
                left_parenthesis_index = x
            elif (converted_result[x] == "–") and (dash_index == None):
                dash_index = x
            elif (converted_result[x] == ")") and (right_parenthesis_index == None):
                right_parenthesis_index = x
            
        parenthesis_content = str(converted_result[left_parenthesis_index+1:right_parenthesis_index])
        
        
        for x in range(len(parenthesis_content)):
            if (parenthesis_content[x] == "–") or (parenthesis_content[x] == "-"):
                dash_index = x
        #if dash_index is not none, then the left side is birthday and the right side is deathday
        if (dash_index != None):
            birthday = parenthesis_content[0:dash_index]
            deathday = parenthesis_content[dash_index+1:]
        
        #if dash_index is none, then the last three words is the birthday
        else:
            splitted_content = parenthesis_content.split()
            day = splitted_content[-3]
            month = splitted_content[-2]
            year = splitted_content[-1]
            birthday = day + " " + month + " " + year
            deathday = "That person is still alive."
    
        return deathday

    except:
        result = "Sorry, no deathday was found."
        return result
