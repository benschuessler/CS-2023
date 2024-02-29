#Ben Schuessler
#This Program Asks a user for a name and will return information on that name
#No Known Bugs
#Bonuses #11 (palindrome check) #13 (make a menu), #15 (Title Distinction
#Code Tester: Max Rodgers

import random
def main():
    name = input("Enter your name")
    go = True

    print("Menu: Enter Choice or 'Q' to quit:")
    print("1) print name in reverse")
    print ("2) print number of vowels in name")
    print ("3) print number of consonants in name")
    print ("4) print first name")
    print ("5) print last name")
    print ("6) print middle name")
    print ("7) Last name has a hyphen")
    print ("8) Convert name to lowercase")
    print ("9) Convert name to uppercase")
    print ("10) Check if first name is palindrome")
    print ("11) Last name has a title")
    print ("12) Modify array")


   
    while go is True:
        answer = input("Number: ")
        if answer == "1":
            print(reverse(name))
        elif answer == "2":
            print(vowel_count(name))
        elif answer == "3":
            print(consonant_count(name))
        elif answer == "4":
            print(first_name(name))
        elif answer == "5":
            print(last_name(name))
        elif answer == "6":
            print(middle_name(name))
        elif answer == "7":
            print(hyphen_check(name))
        elif answer == "8":
            print(lowercase_name(name))
        elif answer == "9":
            print(uppercase_name(name))
        elif answer == "10":
            print(palindrome_check(name))
        elif answer == "11":
            print(title_check(name))
        elif answer == "12":
            print (modify_array(name))
        
       
    


def reverse(name):
    #Description: Function that reverses name
    #Takes user entered name
    #Returns reversed name
    name = name[::-1]
    return(name)
    
    
def vowel_count(name):
    #Description: Function counts number of vowels
    #Takes user entered name
    #Returns number of vowels in given name
    vowels = 0 
    for i in name:
       if i in "aeiouyAEIOUY":
            vowels += 1
    return(vowels)

def consonant_count(name):
    #Description: Function counts number of consonants
    #Takes user entered name
    #Returns number of consonants
    consonants = 0
    for i in name:
        if i in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
            consonants += 1
    return(consonants)

def first_name(name):
    #Description: Function returns first name of user entered name
    #Takes user entered name
    #Returns first name
    
    for a, i in enumerate(name):
       if i == " ":
           return(name[:a])
       
def last_name(name):
    #Description: Function returns last name of user entered name
    #Takes user entered name
    #Returns last name
    count = len(name) - 1
    while count <= len(name):
        letter = name[count]
        if letter == " ":
            return(name[count + 1:])
        else:
            count = count - 1
        
def middle_name(name):
    #Decription: Function returns middle name of user entered name
    #Takes user entered name
    #Returns middle name
    first_index = 0
    while first_index < len(name):
        letter = name[first_index]
        if letter == " ":
            break
        else:
            first_index = first_index + 1

    last_index = len(name) - 1

    while last_index <= len(name):
        letter = name[last_index]
        if letter == " ":
            break
        else:
            last_index = last_index - 1
    
    return(name[first_index + 1:last_index])
    
def hyphen_check(name):
   #Description: Function checks if name contains hyphen
   #Takes user entered name
   #Returns True or False whether name contains hyphen
   if "-" in name:
       return True
   else:
       return False

def lowercase_name(name):
    #Description: Function converts name to all lowercase
    #Takes user entered name
    #Returns name in all lowercase
    lowercase = ""
    for w in name:                                                     
        if w in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            lowercase += chr(ord(w) + 32)                             
        else:
            lowercase += w                                            
    return lowercase


def uppercase_name(name):
    #Description: Function converts name to all uppercase
    #Takes user entered name
    #Returns name in all caps
    uppercase = ""
    for w in name:                                                     
        if w in "abcdefghijklmnopqrstuvwxyz":
            uppercase += chr(ord(w) - 32)                             
        else:
            uppercase += w                                            
    return uppercase
   



def palindrome_check(name):
    #Description: Function checks if name is a palindrome
    #Takes user entered name
    #Returns true or false whether name is a palindrome
    boolean_palindrome = False
    first = first_name(name)    
    lowercase_first = lowercase_name(first)  
    
    front_index = 0
    back_index = 1
    while front_index < len(lowercase_first):
        if lowercase_first[front_index] == lowercase_first[-back_index]: 
            boolean_palindrome = True
            front_index +=1
            back_index += 1
        else:
            boolean_palindrome = False
            break
    return boolean_palindrome



def title_check(name):
    #Description: Function checks whether name contains title
    #Takes user entered name
    #Returns true or false whether name contains title
    if "Dr." in name or "Sir" in name or "Esq" in name or "Ph.d" in name:
        return True
    else:
        return False

def modify_array(name):
    #Description: Function randomises letters in name
    #Takes user entered name
    #Returns randomly arranged name
    letters = []
    removed = []
    new = []
    length = 0
    for i in name: 
            letters.append(i)
            removed.append(i)
    while length < len(letters):
            choice = random.choice(removed) 
            new.append(choice)
            length += 1
            removed.remove(choice)
    return(str(("".join(new))))








if __name__ == '__main__':
    main()