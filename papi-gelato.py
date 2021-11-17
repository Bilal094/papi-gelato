# Time import ---

from time import sleep

# Variabelen --- 

Herhalen = True
Bolsmaak = 1
Bolsmaak2 = 1
AantalBakjes = 0
AantalHorrentjes = 0
Smaken = ["A", "C", "M", "V", "a", "c", "m", "v", "Aardbei", "Chocolade", "Munt", "Vanille", "aardbei", "chocolade", "munt", "vanille"]
BolletjePrijs = 1.10
HorrentjePrijs = 1.25
BakjePrijs = 0.75
TotaalBol = 0
TotaalBak = 0
TotaalHoorntje = 0
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


while Herhalen:
    AantalBolletjes = int(input('Hoeveel bolletjes wilt u? '))
    
    # Als de klant tussen de 1 of 3 bolletjes wilt
    if AantalBolletjes >= 1 and AantalBolletjes <= 3:

        # Hier wordt de klant gevraagd om de smaken voor zijn bolletjes
        while Bolsmaak <= AantalBolletjes:
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
            else:
                showError()
        # Hier wordt de klant gevraagd of hij een bakje of een hoorntje wilt en daarna wordt de code afgesloten of, als de klant het wilt, opnieuw 'gerund'
        Bakje = input('Wilt u deze '+ str(AantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje? ').upper()
        if Bakje.upper() == 'A':
            AantalHorrentjes += 1
            Doorgaan = input('Hier is uw hoorntje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
            if Doorgaan == 'Y':
                Herhalen = True
            elif Doorgaan == 'N':
                print('Bedankt en tot ziens!') 
                Herhalen = False
            else:
                showError()
        elif Bakje.upper() == 'B':
            AantalBakjes += 1
            Doorgaan = input('Hier is uw bakje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
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
    elif AantalBolletjes >= 4 and AantalBolletjes <= 8:
        AantalHorrentjes += 1
        print('Dan krijgt u van mij een bakje met '+ str(AantalBolletjes) +' bolletjes.')
        while Bolsmaak <= AantalBolletjes:
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
        Herhalen = False
    # Als de klant meer dan 8 bolletjes wilt, dan krijgt de klant een foutmelding te zien
    elif AantalBolletjes > 8:
        showErrorBakje()
        Herhalen = True
    # De klant kan niet voor 0 bolletjes kiezen, hij laat dan deze foutmelding zien
    elif AantalBolletjes == 0:
        showError()
        Herhalen = True
    else:
        showError()

TotaalBol = AantalBolletjes * BolletjePrijs
TotaalHoorntje = AantalHorrentjes * HorrentjePrijs
TotaalBedrag = TotaalBol + TotaalHoorntje + TotaalBak
print('--------------[Papi Gelato]--------------')
print()
if AantalBolletjes >= 1:
    print('Bolletjes        '+ str(AantalBolletjes) +' x €1,10 = €'+ str(round(TotaalBol, 3)))
else:
    print()
if AantalHorrentjes >= 1:
    print('Horrentje        '+ str(AantalHorrentjes) +' x €1,25 = €' + str(round(TotaalHoorntje, 3)))
else:
    print()
if AantalBakjes >= 1:
    print('Bakje            '+ str(AantalBakjes) +' x €0,75 = €'+ str(TotaalBak))
else:
    print()
print('                             ----- +')
print('Totaal:                      €'+ str(round(TotaalBedrag, 3)))