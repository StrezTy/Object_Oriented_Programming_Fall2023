#This program will take inputs from the user put them into a tuple and then take from the tuple to create an address.
#all of the user inputted vars are created below
lastname= input("Enter your last name: ")
firstname= input("Enter your first name: ")
streetnum= int(input("Enter your street number: "))
streetname= input("Enter your street name: ")
apartnum= (input("Enter your apartment or Box number if you have one: "))
city= input("Enter the name of your city: ")
state= input("Enter the name of your state: ")
zipcode= int(input("Enter your zip code: "))
#now that the user has entered all applicable information it is stored in a tuple
storage= lastname, firstname, streetnum, streetname, apartnum, city, state, zipcode
# now take the data from the tuple to print out an address
print(f'\n{storage[0].title()}, {storage[1].title()}')
print(f'{storage[2]} {storage[3].title()}')
if(apartnum):
    print(f'{storage[4].upper()}')
print(f'{storage[5].title()}, {storage[6].upper()} {storage[7]}')