numbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63'
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
encode_ref = dict(zip(numbers.split(),list(characters)))     #DICTIONARY THAT WILL BE USED FOR ENCODED TEXT
decode_ref = dict(zip(list(characters),numbers.split()))     #DICTIONARY THAT WILL BE USED FOR DECODED TEXT

def encode(plain_text):
    binary = []
    total_bin = ''
    divisions_six = []
    final = ''
    
    for ch in plain_text:
        a = bin(ord(ch))[2:]
        extra = 8 - len(a)
        binary += [(extra * '0') + a]
    for i in binary:
        total_bin += i

    total_bin_list = list(total_bin)    #CREATES LIST OF THE COMBINED BITS

    length = len(total_bin_list)        #TO CHECK THE LENGTH FOR 6 DIVISION
    leftover = length % 6               #IF NUMBER NOT PROPERLY DIVISIBLE BY 6
    extra = 6 - leftover
    length -= leftover                  #REMAINING LENGTH IN MULTIPLE OF 6
    leftover_list = total_bin_list[-(leftover):]    #LIST OF EXTRA ELEMENTS

    for dlt in range(leftover):         #TO REMOVE EXTRA ELEMENTS
        total_bin_list.pop()

    if extra < 6:                       #TO DEAL WITH THE EXTRA BITS THAT ARE LESS THAN 6
        for m in range(extra):
            leftover_list.append('0')

    m = 0
    for i in range(6,length + 1,6):     #FOR CREATING 6 BITS
        n = i
        divisions_six += [''.join(total_bin_list[m:n])]
        m = n
        if m == length + 1:
            break

    for sm in divisions_six:
        total = 0
        total = total + int(sm[0])*32 + int(sm[1])*16 + int(sm[2])*8 + int(sm[3])*4 + int(sm[4])*2 + int(sm[5])
        final += encode_ref[str(total)]
    if len(leftover_list) == 6:
        total = 0
        total = total + int(leftover_list[0])*32 + int(leftover_list[1])*16 + int(leftover_list[2])*8 + int(leftover_list[3])*4 + int(leftover_list[4])*2 + int(leftover_list[5])
        final += encode_ref[str(total)]

    return final

def decode(plain_text):
    binary = []
    total_bin = ''
    divisions_eight = []
    final = ''

    for ch in plain_text:
        a = bin(int(decode_ref[ch]))[2:]
        extra = 6 - len(a)
        binary += [(extra * '0') + a]
    for i in binary:
        total_bin += i

    total_bin_list = list(total_bin)

    length = len(total_bin)
    leftover = length % 8
    length -= leftover
    for j in range(leftover):
        total_bin_list.pop()

    m = 0
    for k in range(8,length + 1,8):     #FOR CREATING 8 BITS
        n = k
        divisions_eight += [''.join(total_bin_list[m:n])]
        m = n
        if m == length + 1:
            break

    for sm in divisions_eight:
        total = 0
        total = total + int(sm[0])*128 + int(sm[1])*64 + int(sm[2])*32 + int(sm[3])*16 + int(sm[4])*8 + int(sm[5])*4 + int(sm[6])*2 + int(sm[7])
        final += chr(total)

    return final
