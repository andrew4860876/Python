import time
import os
import random
import sys



def remove_character(called_char):
    mylist = []

    string = input("word: ")
    for char in string:
        mylist.append(char)

    # print(mylist)

    num_of_char = mylist.count(called_char)

    for i in range(num_of_char):
        pos = mylist.index(called_char)
        mylist.pop(pos)

    mystr = ''
    for item in mylist:
        mystr += str(item)
    # os.system('clear')
    print(mystr)
    # os.system('echo "' + mystr + '" | pbcopy')

os.system('clear')
B = input("whats the character? ")
remove_character(B)
