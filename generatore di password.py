import random 

myCaratteri = [
'a','b','c','d','e','f','g',
'h','i','j','k','l','m','n',
'o','p','q','r','s','t','u',
'v','w','x','y','z','A','B',
'C','D','E','F','G','H','I',
'J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W',
'X','Y','Z','0','1','2','3',
'4','5','6','7','8','9','!',
'£','$','%','&','?','#','@']

def randomizzaCaratteri(arr):
    return random.randrange(len(arr)) #randomizza tutti i caratteri dell'array

def generaPassword(arr, lung):
    myPassword = ''

    for _ in range(lung): 
        myPassword += arr[randomizzaCaratteri(arr)] #randomizza una lettera per il massimo definito in len_psw
    
    return myPassword

if __name__ == '__main__':

    def main():
        run = True
        while run:
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

                lunghezza = int(input("Inserisci la lunghezza: "))
                if lunghezza == piccolaLunghezza:
                    print("La password scelta di " + str(piccolaLunghezza)+ " caratteri è: ", generaPassword(myCaratteri, lunghezza))
                elif lunghezza == mediaLunghezza:
                    print("La password scelta di " + str(mediaLunghezza)+ " caratteri è: ", generaPassword(myCaratteri, lunghezza))
                elif lunghezza == massimaLunghezza:
                    print("La password scelta di " + str(massimaLunghezza)+ " caratteri è: ", generaPassword(myCaratteri, lunghezza))
                elif lunghezza == 0:
                    
                    esci = input("Per uscire premi S altrimenti premi un pulsante qualsiasi: ")

                    if esci.lower() == "s":
                        print("PROGRMMA TERMINATO...")
                        run = False
                else:
                    print("Inserisci un valore valido.")
main()
