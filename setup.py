import BASE_64
import ROT_13
import os

def OpSys(): 
    if os.name in 'posix':
        location = input("FULL DIRECTORY TO RECEIVE PASSWORD, EX. /Users/[NAME]--")
        file = open("/Users/"+os.listdir('/Users/')[1]+'location.txt','w')
        file.write(ROT_13.encrypt(BASE_64.encode(location)))
        try:
            f = open("/Users/"+os.listdir('/Users/')[1]+'roots.txt','x')
        except FileExistsError:
            pass
        else:
            f.close()
        file.close()
        os.rename("/Users/"+os.listdir('/Users/')[1]+'roots.txt',"/Users/"+os.listdir('/Users/')[1]+'roots.sii')
    elif os.name in 'nt':
        location = input("FULL DIRECTORY TO RECEIVE PASSWORD, EX.C:\\Users\\-- ")
        file = open("C:\\Users\\Public\\location.txt",'w')
        file.write(ROT_13.encrypt(BASE_64.encode(location)))
        try:
            f = open("C:\\Users\\Public\\roots.txt",'x')
        except FileExistsError:
            pass
        else:
            f.close()
        file.close()
        os.rename("C:\\Users\\Public\\roots.txt","C:\\Users\\Public\\roots.sii")

OpSys()
os.remove('setup.py')
