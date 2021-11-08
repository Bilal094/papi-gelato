# Time import ---

from time import sleep

# Variabelen --- 

Herhalen = True

# User-Defined functions ---

def showIntro():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def pause():
    sleep(1.5)

def showError():
    print('Sorry, dat snap ik niet...')

def showErrorBakje():
    print('Sorry, zulke grote bakken hebben we niet.')

# Code start ---
showIntro()
pause()

while Herhalen == True:
    Bolletjes = int(input('Hoeveel bolletjes wilt u? '))
    if Bolletjes >= 1 and Bolletjes <= 3:
        Herhalen = False
        AantalBolletjes = Bolletjes
        Bakje = input('Wilt u deze '+ str(Bolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje? ')
        if Bakje.upper() == 'A':
            print('test')
        elif Bakje.upper() == 'B':
            print('test2')
    elif Bolletjes >= 4 and Bolletjes <= 8:
        AantalBolletjes = Bolletjes
        print('Dan krijgt u van mij een bakje met '+ str(Bolletjes) +' bolletjes.')
        Herhalen = False
    elif Bolletjes > 8:
        showErrorBakje()
    elif Bolletjes == 0:
        showError()

