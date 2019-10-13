''' Insert heading comments here.'''
import string
t1 = string.ascii_lowercase

answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
while answer.upper() != 'Q':
    answer = answer.lower()
    
    if answer=="e":
        key = input("Please enter a keyword: ")
        while len(key)>26 or not key.isalpha():
            print("There is an error in the keyword. It must be all"+
                  " letters and a maximum length of 26 Please enter a "+
                  "keyword: abcdefghijklmnopqrstuvwxyzz")
            key = input("Please enter a keyword: ")
            
        key = key.lower()
        
        t2 = ""
        for ch in key+t1:
            if not (ch in t2):
                t2 += ch
                
        t3 = ""
        for i in range(26):
            y = (5*i+8)%26
            t3 += t2[y]
            
        message = input("Enter your message: ")
        message = message.lower()
        
        secret = ""
        for ch in message:
            if ch in t1:
                ind = t1.find(ch)
                secret += t3[ind]
            else:
                secret += ch
            
        print("your encoded message:",secret)
    
    if answer=="d":
        print("Decrypt")
        
        key = input("Please enter a keyword: ")
        while len(key)>26 or not key.isalpha():
            print("There is an error in the keyword. It must be all"+
                  " letters and a maximum length of 26 Please enter a "+
                  "keyword: abcdefghijklmnopqrstuvwxyzz")
            key = input("Please enter a keyword: ")
            
        key = key.lower()
        
        t2 = ""
        for ch in key+t1:
            if not (ch in t2):
                t2 += ch
                
        t3 = ""
        for i in range(26):
            y = (5*i+8)%26
            t3 += t2[y]
            
        message = input("Enter your message: ")
        message = message.lower()
        
        secret = ""
        for ch in message:
            if ch in t1:
                ind = t3.find(ch)
                secret += t1[ind]
            else:
                secret += ch
            
        print("your decoded message:",secret)
      
    
    
    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
