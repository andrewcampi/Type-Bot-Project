

from countryinfo import CountryInfo



us_state_capitals = {"alabama":"Montgomery",
                     "alaska":"Juneau",
                     "arizona":"Phoenix",
                     "arkansas":"Little Rock	",
                     "california	":"Sacramento",
                     "colorado":"Denver",
                     "connecticut":"Hartford",
                     "delaware":"Dover",
                     "florida":"Tallahassee",
                     "georgia":"Atlanta",
                     "hawaii":"Honolulu",
                     "idaho":"Boise",
                     "illinois":"Springfield",
                     "indiana":"Indianapolis",
                     "iowa":"Des Moines",
                     "kansas":"Topeka",
                     "kentucky":"Frankfort",
                     "louisiana":"Baton Rouge",
                     "maine":"Augusta",
                     "maryland":"Annapolis",
                     "massachusetts":"Boston	",
                     "michigan":"Lansing",
                     "minnesota":"Saint Paul	",
                     "mississippi":"Jackson",
                     "missouri":"Jefferson City",
                     "montana":"	Helena",
                     "nebraska":"Lincoln",
                     "nevada":"Carson City",
                     "new hampshire":"Concord",
                     "new jersey":"Trenton",
                     "new mexico":"Santa Fe",
                     "new york":"Albany",
                     "north carolina	":"Raleigh",
                     "north dakota":"Bismarck",
                     "ohio":"Columbus",
                     "oklahoma":"Oklahoma City",
                     "oregon":"Salem",
                     "pennsylvania":"Harrisburg",
                     "rhode island":"Providence",
                     "south carolina":"Columbia",
                     "south dakota":"Pierre",
                     "tennessee":"Nashville",
                     "texas":"Austin",
                     "utah":"Salt Lake City",
                     "vermont":"Montpelier",
                     "virginia":"Richmond",
                     "washington":"Olympia",
                     "west virginia":"Charleston	",
                     "wisconsin":"Madison",
                     }





#query format : what is the capital of __(country)__

def capitals(query):
    
    content = query[5:]
    
    country = " ".join(content) 
    
    #remove question mark
    if (country[-1] == "?"):
        country = country[:-1]
    
    str_country = country
    state = country
    
    print("country:",country)
    try:
        #find capital of country
        country = CountryInfo(country)
    
        capital = country.capital()
        
        result = "The capital of " + str_country + " is " + str(capital) + "."
    
    except:
        #find capial of U.S. state
        print("state:",state)
        try:
            capital = us_state_capitals[state]
            
            result = "The capital of " + str(state.capitalize()) + " is " + str(capital) + "."
        
        except:
            result = "Sorry, I don't know the capital of that country."
            
            
    
    return result
    
