from Encryption import *
from Decryption import *
from os import system
import platform

# clear_display()
def clear_display():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def isDuplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

while True:
    clear_display()
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        k = int(input("Type the key (Only unique integer): "))
        # text = "daffodilinternationaluniversity"
        # key = [3,7,2,9,1,5,4]
        
        key = [int(x) for x in str(k)]
        
        # Check if list has duplicate value or not 
        while isDuplicate(key):
            print("\n\n!Sorry This encryption could not possible\nYou must have to enter Only unique integer as Key\n\n")
            k = int(input("Type the key (Only unique integer): "))
            key = [int(x) for x in str(k)]
        
            
        if choice == "encode":
            encode(text, key)
        else:
            decode(text, key)
        
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    clear_display()
    if isContinue == 'n' or isContinue == 'N': break
    
print("\n\n---------------------------------------------------")
print("\nGoodbye\nThanks for using....")
print("---------------------------------------------------")

        
        


