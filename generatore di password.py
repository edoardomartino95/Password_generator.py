import random 
import time

charArr = [
'a','b','c','d','e','f','g',
'h','i','j','k','l','m','n',
'o','p','q','r','s','t','u',
'v','w','x','y','z','A','B',
'C','D','E','F','G','H','I',
'J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W',
'X','Y','Z','0','1','2','3',
'4','5','6','7','8','9','@',
'!','|','$','%','&','?','-',
'_','+','*','#','£','=','€'
]

def genPsw(arr):
    lunghezza = 16 #lunghezza della password
    psw = ''

    for i in range(lunghezza): 
        psw += charArr[random.randrange(len(charArr))] #randomizza una lettera per il massimo definito in long
    
    return psw
    
print(genPsw(charArr))
    


