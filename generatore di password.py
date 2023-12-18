import random 

charArr = [
'a','b','c','d','e','f','g',
'h','i','j','k','l','m','n',
'o','p','q','r','s','t','u',
'v','w','x','y','z','A','B',
'C','D','E','F','G','H','I',
'J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W',
'X','Y','Z','0','1','2','3',
'4','5','6','7','8','9','!',
'£','$','%','&','?','#','@',
"-", "_", "*", "|", "/", "§"]

def randomize_char(arr):
    return random.randrange(len(arr)) #randomizza tutti i caratteri dell'array

def gen_psw(arr, lung):
    my_psw = ''

    for _ in range(lung): 
        my_psw += arr[randomize_char(arr)] #randomizza una lettera per il massimo definito in len_psw
    
    return my_psw

if __name__ == '__main__':
    
    piccolaLunghezza = 8
    mediaLunghezza = 16
    massimaLunghezza = 32

    print("""
GENERATORE PASSWORD:
Inserisci la lunghezza della password:
          
[8] Password ad otto caratteri
[16] Password a sedici caratteri 
[32] Password a trentadue caratterri
[0] Esci dal programma
""")

while True:
    lunghezza = int(input("Inserisci la lunghezza: "))
    if lunghezza == piccolaLunghezza:
        print("La password scelta di " + str(piccolaLunghezza)+ " è: ", gen_psw(charArr, lunghezza))
        break
    elif lunghezza == mediaLunghezza:
         print("La password scelta di " + str(mediaLunghezza)+ " è: ", gen_psw(charArr, lunghezza))
         break
    elif lunghezza == massimaLunghezza:
         print("La password scelta di " + str(massimaLunghezza)+ " è: ", gen_psw(charArr, lunghezza))
         break
    elif lunghezza == 0:
        
        esci = input("Per uscire premi S altrimenti premi un pulsante qualsiasi: ")

        if esci.lower() == "s":
            print("PROGRMMA TERMINATO...")
            break
    else:
        print("Inserisci un valore valido.")
