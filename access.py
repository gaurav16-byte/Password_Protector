import ROT_13
import BASE_64
import os
import platform
from random import choice
import sys

print("WELCOME TO THE DIARY",platform.node())
a = os.name

def rand():
    global IV
    init = BASE_64.encode(platform.machine())
    vector = ''
    for i in range(256 - len(init)):
        vector += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$%^&*()-_+?')
    IV = init + vector
    return IV

print('A) READ PASSWORDS')
print('B) ADD A PASSWORD')
print('C) WIPE AND START NEW FILE')
print('D) DELETE ALL FILES FOREVER')
print('E) EXIT')

def DARWIN():
    choice = input(">> ")
    while choice not in "ABCDEabcde":
        print("INVALID CHOICE")
        choice = input(">> ")
    else:
        if choice in 'Aa':
            iv = rand()
            location_file = open("/Users/"+os.listdir('/Users/')[1]+'/location.txt','r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.sii',"/Users/"+os.listdir('/Users/')[1]+'/roots.txt')
                file = open("/Users/"+os.listdir('/Users/')[1]+'/roots.txt','r')
                a = file.readlines()
                for i in a:
                    print(BASE_64.decode(ROT_13.decrypt(i[:-1])))
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.txt',"/Users/"+os.listdir('/Users/')[1]+'/roots.sii')
                file.close()
            else:
                sys.exit()
        elif choice in 'Bb':
            iv = rand()
            location_file = open("/Users/"+os.listdir('/Users/')[1]+'/location.txt','r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.sii',"/Users/"+os.listdir('/Users/')[1]+'/roots.txt')
                file = open("/Users/"+os.listdir('/Users/')[1]+'/roots.txt','a')
                password = input("ENTER THE DETEAILS ")
                file.write(ROT_13.encrypt(BASE_64.encode(password)) + '\n')
                file.close()
                print("DETAILS ADDED")
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.txt',"/Users/"+os.listdir('/Users/')[1]+'/roots.sii')
            else:
                sys.exit()
        elif choice in 'Cc':
            print("REMEMBER, IN THIS MODE ALL YOUR DATA WILL BE WIPED!!")
            iv = rand()
            location_file = open("/Users/"+os.listdir('/Users/')[1]+'/location.txt','r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.sii',"/Users/"+os.listdir('/Users/')[1]+'/roots.txt')
                file = open("/Users/"+os.listdir('/Users/')[1]+'/roots.txt','w')
                password = input("ENTER THE DETEAILS ")
                file.write(ROT_13.encrypt(BASE_64.encode(password)) + '\n')
                file.close()
                print("DETAILS ADDED")
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.txt',"/Users/"+os.listdir('/Users/')[1]+'/roots.sii')
            else:
                sys.exit()
        elif choice in 'Dd':
            print("ALL THE FILES INCLUDING YOUR CREDENTIALS WILL BE DELETED!")
            x = input("DELETE(Y), ABORT(N) ")
            while x not in 'YNyn':
                print("INVALID CHOICE")
                x = input("DELETE(Y), ABORT(N) ")
            else:
                if x in 'Nn':
                    sys.exit()
                elif x in 'Yy':
                    os.remove("/Users/"+os.listdir('/Users/')[1]+'/roots.txt')  #sii to txt
                    os.remove("/Users/"+os.listdir('/Users/')[1]+'/location.txt')
                    print('ALL RELATED DATA HAS BEEN REMOVED..')
        elif choice in 'Ee':
            if 'roots.sii' not in os.listdir("/Users/"+os.listdir('/Users/')[1]+'/'):
                #os.rename("/Users/"+os.listdir('/Users/')[1]+'/roots.txt',"/Users/"+os.listdir('/Users/')[1]+'/roots.sii')
                sys.exit()
            else:
                sys.exit()

def NT():
    choice = input(">> ")
    while choice not in "ABCDEabcde":
        print("INVALID CHOICE")
        choice = input(">> ")
    else:
        if choice in 'Aa':
            iv = rand()
            location_file = open("C:\\Users\\Public\\location.txt",'r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("C:\\Users\\Public\\roots.sii","C:\\Users\\Public\\roots.txt")
                file = open('C:\\Users\\Public\\roots.txt','r')
                a = file.readlines()
                for i in a:
                    print(BASE_64.decode(ROT_13.decrypt(i[:-1])))
                #os.rename("C:\\Users\\Public\\roots.txt","C:\\Users\\Public\\roots.sii")
                file.close()
            else:
                sys.exit()
        elif choice in 'Bb':
            iv = rand()
            location_file = open("C:\\Users\\Public\\location.txt",'r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("C:\\Users\\Public\\roots.sii","C:\\Users\\Public\\roots.txt")
                file = open("C:\\Users\\Public\\roots.txt",'a')
                password = input("ENTER THE DETEAILS ")
                file.write(ROT_13.encrypt(BASE_64.encode(password)) + '\n')
                file.close()
                print("DETAILS ADDED")
                #os.rename("C:\\Users\\Public\\roots.txt","C:\\Users\\Public\\roots.sii")
            else:
                sys.exit()
        elif choice in 'Cc':
            print("REMEMBER, IN THIS MODE ALL YOUR DATA WILL BE WIPED!!")
            iv = rand()
            location_file = open("C:\\Users\\Public\\location.txt",'r')
            location = BASE_64.decode(ROT_13.decrypt(location_file.read()))
            location_file.close()
            f = open(location + 'password.txt','w')
            f.write(iv)
            f.close()
            answer = input("ENTER THE PASSWORD SENT TO YOUR DESIRED LOCATION ")
            if answer == iv:
                #os.rename("C:\\Users\\Public\\roots.sii","C:\\Users\\Public\\roots.txt")
                file = open("C:\\Users\\Public\\roots.txt",'w')
                password = input("ENTER THE DETEAILS ")
                file.write(ROT_13.encrypt(BASE_64.encode(password)) + '\n')
                file.close()
                print("DETAILS ADDED")
                #os.rename("C:\\Users\\Public\\roots.txt","C:\\Users\\Public\\roots.sii")
            else:
                sys.exit()
        elif choice in 'Dd':
            print("ALL THE FILES INCLUDING YOUR CREDENTIALS WILL BE DELETED!")
            x = input("DELETE(Y), ABORT(N) ")
            while x not in 'YNyn':
                print("INVALID CHOICE")
                x = input("DELETE(Y), ABORT(N) ")
            else:
                if x in 'Nn':
                    sys.exit()
                elif x in 'Yy':
                    os.remove("C:\\Users\\Public\\roots.txt")   #sii to txt
                    os.remove("C:\\Users\\Public\\location.txt")
                    print('ALL RELATED DATA HAS BEEN REMOVED..')
        elif choice in 'Ee':
            if 'roots.txt' not in os.listdir("C:\\Users\\Public\\"):
                #os.rename("C:\\Users\\Public\\roots.txt","C:\\Users\\Public\\roots.sii")
                sys.exit()
            else:
                sys.exit()

if a == 'nt':
    NT()
elif a == 'Darwin':
    DARWIN()
