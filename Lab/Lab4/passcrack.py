# Seung Ki Lee
import hashlib
import itertools
import time

# Hash Function altered from hash.py given.
def hash_password(input_password):
    return ((hashlib.sha256(input_password.strip().encode()).hexdigest()))

# brute force function
'''
Because the Brute Force often crashes the machine, I put the logic in a function and commented out the execution at the bottom of the code.
'''
def bruteforcing(hashed_password_set, string_type_set):
    # Create list of chars to accept
    chars = string_type_set
    bf_num = 0
    # starting from empty string, add in individual letters to see if it is the password
    # only 6 letters long
    for i in range (7):
        for letter in itertools.product(chars, repeat=i):
            letter = ''.join(letter)
            if (hash_password(letter) == hashed_password_set):
                bf_num += 1
                print ("Cracked with Brute Force ", bf_num, " ", hashed_password_set, " : ", letter)
            else:
                print ("Uncracked with Brute Force ", hashed_password_set, " : ")
                

# Seung Ki Lee

# Building Dictionary. Read in the file cuz IO is slow AF
dicked = []
# Read in the passwordlist.txt made.
# encoding cuz I use Korean system
with open('passwordlist.txt', 'r', encoding='utf-8') as dicktionary:
    for word in dicktionary:
        # strip the new line. I use Windows.
        word = word.replace('\n', '')
        dicked.append(word)

# Read in hashed from hashes.txt given.
hashed = []
with open('hashes.txt', 'r', encoding='utf-8') as fo:
    for hashtext in fo:
        hashtext = hashtext.replace('\n', '')
        hashed.append(hashtext)

dicktionary.close()
fo.close()

# Seung Ki Lee

# make and open a password.txt file to write to
passwordf = open("passsword.txt", 'w', encoding='utf-8')

dicked_num = 0

dastart_time = time.time()
# dictionary attack
for word in dicked:
    for hashtext in hashed:
        if (hash_password(word) == hashtext):
            dicked_num += 1
            print("Cracked with Dictionary Attack", dicked_num, " ", hashtext, " : ", word)
            passlog = hashtext + " : " + word + "\n"
            passwordf.write(passlog)
#        elif(hash_password(word)!= hashtext):
#            print("Uncracked with Dictionary Attack", hashtext, " : ")
#            passlog = hashtext + " : \n"
#            passwordf.write(passlog)

daend_time = time.time()
datotal_time = daend_time-dastart_time
print ("total time it took to crack using dictionary attack is : ", datotal_time, "seconds")

# close password file
passwordf.close()

# Seung Ki Lee

# Brute Force Execution
# Do not run this part it will crash if unlucky :(
# To test the functionality you can uncomment the last two lines and run the code. The logic is above.
string_type = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
# for hashtext in hashed:
#     bruteforcing(hashtext, string_type)

# Seung Ki Lee