
def fare_calculator(dist):
    """"Returns the total fare owed based on the distance inputted. The returned value will be a float in the format $x.xx"""
    #first the variables are initialized so the math can be performed optimally. 
    #The base fare starts at 4, then convert the distance to meters and find the instances needed to count the rate. 
    #Then the required math to determine the fare is performed

    FARE= 4.00
    inmeter= float(dist)*1000
    instances= inmeter//140
    rate= 0.25
    total= FARE + (instances*rate)
    message= f'${total}'
    
    return message
    #Many of these variables might not have been needed in this example however should a more complicated action 
    # be needed to be performed in a function it is best to have all values in a variable
x= input("Enter a number")
print(fare_calculator(x))
