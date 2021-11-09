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
    
    # Als de klant tussen de 1 of 3 bolletjes wilt
    if Bolletjes >= 1 and Bolletjes <= 3:
        AantalBolletjes = Bolletjes
        Bakje = input('Wilt u deze '+ str(Bolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje? ')
        if Bakje.upper() == 'A':
            Doorgaan = input('Hier is uw hoorntje met '+ str(Bolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
            if Doorgaan == 'Y':
                Herhalen = True
            elif Doorgaan == 'N':
                print('Bedankt en tot ziens!')
                Herhalen = False
            else:
                showError()
        elif Bakje.upper() == 'B':
            Doorgaan = input('Hier is uw bakje met '+ str(Bolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
            if Doorgaan == 'Y':
                Herhalen = True
            elif Doorgaan == 'N':
                Herhalen = False
                print('Bedankt en tot ziens!')
            else:
                showError()
        else:
            showError()
    
    # Als de klant tussen de 4 of 8 bolletjes wilt
    elif Bolletjes >= 4 and Bolletjes <= 8:
        AantalBolletjes = Bolletjes
        print('Dan krijgt u van mij een bakje met '+ str(Bolletjes) +' bolletjes.')
        Herhalen = False
    
    # Als de klant meer dan 8 bolletjes wilt, dan krijgt de klant een foutmelding te zien
    elif Bolletjes > 8:
        showErrorBakje()
        Herhalen = True
    # De klant kan niet voor 0 bolletjes kiezen, hij laat dan deze foutmelding zien
    elif Bolletjes == 0:
        showError()
        Herhalen = True
