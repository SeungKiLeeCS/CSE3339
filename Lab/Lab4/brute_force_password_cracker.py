'''
This is basic password brute force cracker written in python using the itertools library.
Seung Ki Lee
'''
# for iteration
import itertools
# for time log
import time

# Brute force function
def leebruteforce(password_set, string_type_set):
    # Start time logging
    start = time.time()
    # all chars
    chars = string_type_set
    attempts = 0
    #using itertools to go through every possible combination
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            print(letter)
            if letter == password_set:
                # End time logging
                end = time.time()
                crack_time = end - start
                return (attempts, crack_time)

# Ask for input for now. Try dictionary later
password = input("Put Your Sample Password >>>")

# Possible Characters
string_type = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
# get the attemps and time that it took to crack from the function
tries, time_taken = leebruteforce(password, string_type)
# print
print(" Password Brute Forced : %s \n Number of Attempts : %s \n Time Spent %s seconds" % (password, tries, time_taken))
