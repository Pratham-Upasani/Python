#XOR Encryption using numerical key
print("XOR Encryption using numerical key:")
text=input("Enter your message: ")
key=int(input("Enter a numerical key: "))

def encryption(text,key):
    cipher=""
    for x in text:
        cipher=cipher+chr(ord(x)^key)
    return cipher
cipher=encryption(text,key)
print("Plain text after encryption with key",key," is: ",cipher)

def decryption(cipher,key):
    plain=""
    for x in cipher:
        plain+=chr(ord(x)^key)
    return plain
plain=decryption(cipher,key)
print("Cipher text after decryption with key ",key," is: ",plain) 

#XOR Encryption using String key
print("\nXOR Encryption using Password(String)")
text=input("Enter your message: ")
key=input("Enter password: ")

def encryption(text,key):
    cipher=""
    if len(text)<=len(key):
        i=0
        for x in text:
            x=chr(ord(x)^ord(key[i]))
            cipher=cipher+x
            i=i+1
        return cipher
    else:
        i=0
        for x in text:
            x=chr(ord(x)^ord(key[i]))
            cipher=cipher+x
            i=i+1
            if i>=len(key):
                i=0
        return cipher

cipher=encryption(text,key)
print("Plain text after encryption with key",key," is: ",cipher)

def decryption(cipher,key):
    plain=""
    if len(cipher)<=len(key):
        i=0
        for x in cipher:
            x=chr(ord(x)^ord(key[i]))
            plain=plain+x
            i=i+1
        return plain
    else:
        i=0
        for x in cipher:
            x=chr(ord(x)^ord(key[i]))
            plain=plain+x
            i=i+1
            if i>=len(key):
                i=0
        return plain

plain=decryption(cipher,key)
print("Cipher text after decryption with key",key," is: ",plain)
    
