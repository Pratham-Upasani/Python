#Caesar Cipher Encryption
text=input("Enter your message: ")
key=int(input("Enter your key(1-25): "))

def encryption(text,key):  #Shifting every alphabet of text 'key' times forward
    cipher=""
    for x in text:
        if x.isalpha():
            x=chr(ord(x)+key)   #Using ASCII Values of alphabets to add with numerical key, then using chr() to get the character of new ascii value 
            if ord(x)>90 and ord(x)<97:             #Loop back to 'A' if x goes beyond Z
                x=chr(ord(x)-26)
            if ord(x)>122:          #Same for lowercase
                x=chr(ord(x)-26)
            cipher+=x
        else:
            cipher+=x
    return cipher

cipher=encryption(text,key)
print(text," after encryption with key ",key," is ",cipher)

def decryption(cipher,key):   #Shifting each alphabet backward 'key' times
    plain=""
    for x in cipher:
        if x.isalpha():
            x=chr(ord(x)-key)
            if ord(x)<65:
                x=chr(ord(x)+26)
            if ord(x)<97 and ord(x)>90:
                x=chr(ord(x)+26)
            plain+=x
        else:
            plain+=x
    return plain

originaltext=decryption(cipher,key)
print(cipher," after decryption with key ",key," is ",originaltext)
        
        
    
    
