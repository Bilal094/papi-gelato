# Time import ---

from time import sleep

# Variabelen --- 

Herhalen = True
Bolsmaak = 1
Smaken = ["A", "C", "M", "V", "a", "c", "m", "v", "Aardbei", "Chocolade", "Munt", "Vanille", "aardbei", "chocolade", "munt", "vanille"]

# User-Defined functions ---

def showIntro():
    print('Welkom bij Papi Gelato')

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
    Bolletjes = input('Hoeveel bolletjes wilt u? ')
    
    # Als de klant tussen de 1 of 3 bolletjes wilt
    if Bolletjes.isdigit() >= 1 and Bolletjes.isdigit() <= 3:

        # Hier wordt de klant gevraagd om de smaken voor zijn bolletjes
        while Bolsmaak <= int(Bolletjes):
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
            else:
                showError()
        
        # Hier wordt de klant gevraagd of hij een bakje of een hoorntje wilt en daarna wordt de code afgesloten of, als de klant het wilt, opnieuw 'gerund'
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
                Herhalen = True
        else:
            showError()
        
    # Als de klant tussen de 4 of 8 bolletjes wilt
    elif Bolletjes.isdigit() >= 4 and Bolletjes.isdigit() <= 8:
        print('Dan krijgt u van mij een bakje met '+ str(Bolletjes) +' bolletjes.')
        while Bolsmaak <= int(Bolletjes):
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
        Herhalen = False
    
    # Als de klant meer dan 8 bolletjes wilt, dan krijgt de klant een foutmelding te zien
    elif Bolletjes.isdigit() > 8:
        showErrorBakje()
        Herhalen = True
    # De klant kan niet voor 0 bolletjes kiezen, hij laat dan deze foutmelding zien
    elif Bolletjes.isdigit() == 0:
        showError()
        Herhalen = True
    else:
        showError()
