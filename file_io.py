import pathlib;
import shutil;
#file manipulators have been imported 
#create a path to current directory and print it
path= pathlib.Path.cwd()
print(path)
#now make a new folder to put a txt file into
new_folder= path/"folder_week11"
new_folder.mkdir()
#make the txt file in week11
new_txt= new_folder/"week11.txt"
new_txt.touch()
#now have a string to import into new_txt
words= "Test: Writing to file"
#import into txt file and print out the contents using read. 
with new_txt.open(mode= 'w') as file:
    file.write(words)
with new_txt.open(mode= 'r') as file:
    print(file.read())

#now make a new directory and use the shutil to make a copy
path2= new_folder/"file_backups"
path2.mkdir()
copy= shutil.copy(new_txt, path2)
#go back to folder 11 and print out the created txt files

for texts in new_folder.rglob("*.txt"):
    print(texts)


