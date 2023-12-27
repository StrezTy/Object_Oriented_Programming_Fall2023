#A lambda expression is used to sort the list of names by last name and a second one is used to create a new list based
#on the first 5 letters of the last name and first two of the first name
names_list=['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']
#I use a lambda function combined with the sort function to sort over the list. We have to split the objects in the list in order to sort by last name
names_list.sort(key= lambda name:name.split()[-1].lower())
print(names_list)
#I use the map function to create a new list using the last name and first name and the respective amount of letters from each.
five_two= list(map(lambda name:name.split()[-1][0:5]+ name.split()[0][0:2], names_list))
print(five_two)