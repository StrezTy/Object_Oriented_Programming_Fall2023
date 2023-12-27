#this program creates a while loop that ends with the letter q
#during the while loop the user can enter any amount of numbers and the sum, count, and average of the 
#numbers will be stored
sum= 0
count= 0
average=0
var= ""
#while loop that takes the values inputted by the user

while var != "q":
    var= input("Enter a number or enter the letter q to quit ")
    if var == "q":
        break
    
    var= int(var)
    sum+= var
    count+=1

#when while loop ends find the average of the inputted numbers and print out all values
average= sum/count
print(f'The sum of the numbers entered is {sum}')
print(f'The count of the numbers entered is {count}')
print(f'The average of the numbers entered is {average}')


    