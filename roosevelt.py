#This program will take the famous quote by  President Franklin Roosevelt and manipulate it turning it into a strange string.
og_phrase= "The only thing we have to fear is fear itself"
word_list= og_phrase.split()
mod_word_list= []
#In this for loop we loop over the list created from the string and examine each word to modify it based on criteria.
for word in word_list:
    if word[0] in "aeiou" :
        mod_word_list.append(word + "way")
    else:
       mod_word_list.append(word[1:] + word[0] + "ay") 

#after the for loop makes a new list we join the list together separating each element with a space and print the modified string out
new_string= " ".join(mod_word_list)
print(new_string.capitalize())
