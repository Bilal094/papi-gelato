# Time import ---

from time import sleep

# Variabelen --- 
ToppingBool = True
Topping = 1
Herhalen = True
MeerBestellen = True
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
TotaalTopping = 0
TotaalHoorntje = 0
Slagroom = 0.50
Sprinkels = 0.30
CaramelSausHorrentje = 0.60
CaramelSausBakje = 0.90
TotaalBollen = 0
AantalCaramel = 0
AantalSprinkels = 0
AantalSlagroom = 0
# User-Defined functions ---

def showIntro():
    print('Welkom bij Papi Gelato')

def pause():
    sleep(1.5)

def showError():
    print('Sorry, dat snap ik niet...')

def showErrorBakje():
    print('Sorry, zulke grote bakken hebben we niet.')

def topping():
    global AantalSlagroom, AantalSprinkels
    while ToppingBool:
        Topping = 0

        ToppingVraag = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ').upper()
        if ToppingVraag == "A" or ToppingVraag == "Geen":
            Topping = 0
        elif ToppingVraag == "B" or ToppingVraag == "Slagroom":
            AantalSlagroom += Slagroom
            Topping += 1
        elif ToppingVraag == "C" or ToppingVraag == "Sprinkels":
            AantalSprinkels += Sprinkels
            Topping += 1
        elif ToppingVraag == "D" or ToppingVraag == "Caramel saus" or ToppingVraag == "Caramel":
            global Bakje
            if Bakje == "A" or Bakje == "Hoorntje":
                global AantalCaramel
                AantalCaramel += CaramelSausHorrentje
                Topping += 1
            if Bakje == "B" or ToppingVraag == "Bakje":
                AantalCaramel += CaramelSausBakje
                Topping += 1


        global TotaalTopping
        TotaalTopping = AantalCaramel + AantalSlagroom + (AantalSprinkels * AantalBolletjes)
        return Topping and TotaalTopping and ToppingVraag
        
# Code start ---
showIntro()
pause()


while Herhalen:
    AantalBolletjes = int(input('Hoeveel bolletjes wilt u? '))
    
    # Als de klant tussen de 1 of 3 bolletjes wilt
    if AantalBolletjes >= 1 and AantalBolletjes <= 3:

        # Hier wordt de klant gevraagd om de smaken voor zijn bolletjes
        Bolsmaak = 1
        while Bolsmaak <= AantalBolletjes:
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
            else:
                showError()
        
        Bakje = input('Wilt u deze '+ str(AantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje? ').upper()

    
        topping()

        
        # Hier wordt de klant gevraagd of hij een bakje of een hoorntje wilt en daarna wordt de code afgesloten of, als de klant het wilt, opnieuw 'afgespeeld'
        if Bakje.upper() == 'A':
            AantalHorrentjes += 1
            while MeerBestellen:
                Doorgaan = input('Hier is uw hoorntje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
                if Doorgaan == 'Y':
                    Herhalen = True
                    MeerBestellen = False
                elif Doorgaan == 'N':
                    print('Bedankt en tot ziens!') 
                    Herhalen = False
                    MeerBestellen = False
                else:
                    showError()
                    MeerBestellen = True
                
        elif Bakje.upper() == 'B':
            AantalBakjes += 1
            while MeerBestellen:
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
        AantalBakjes += 1
        Bolsmaak = 1
        print('Dan krijgt u van mij een bakje met '+ str(AantalBolletjes) +' bolletjes.')
        Bakje = "B" or "Bakje"
        while Bolsmaak <= AantalBolletjes:
            Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak in Smaken:
                Bolsmaak += 1
            else:
                showError()
                
        topping()

        while MeerBestellen:
            Doorgaan = input('Hier is uw bakje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
            if Doorgaan == 'Y':
                Herhalen = True
                MeerBestellen = False
            elif Doorgaan == 'N':
                print('Bedankt en tot ziens!')
                Herhalen = False
                MeerBestellen = False
            else:
                showError()
                MeerBestellen = True


    
    # Als de klant meer dan 8 bolletjes wilt, dan krijgt de klant een foutmelding te zien
    elif AantalBolletjes > 8:
        AantalBolletjes = 0
        showErrorBakje()
        Herhalen = True
    
    # De klant kan niet voor 0 bolletjes kiezen, hij laat dan deze foutmelding zien
    elif AantalBolletjes == 0:
        showError()
        Herhalen = True
    else:
        showError()

    TotaalBollen += AantalBolletjes

Topping += Topping
TotaalBol = TotaalBollen * BolletjePrijs
TotaalHoorntje = AantalHorrentjes * HorrentjePrijs
TotaalBak = AantalBakjes * BakjePrijs
TotaalBedrag = TotaalBol + TotaalHoorntje + TotaalBak + TotaalTopping


print('--------------[Papi Gelato]--------------')
print()
if AantalBolletjes >= 1:
    print('Bolletjes        '+ str(TotaalBollen) +' x €1,10 = €'+ str(round(TotaalBol, 3)))

if AantalHorrentjes >= 1:
    print('Horrentje        '+ str(AantalHorrentjes) +' x €1,25 = €' + str(round(TotaalHoorntje, 3)))

if AantalBakjes >= 1:
    print('Bakje            '+ str(AantalBakjes) +' x €0,75 = €'+ str(TotaalBak))

if Topping >= 1:
    print('Topping          '+ str(Topping) +' x €'+ str(TotaalTopping) +' = €'+ str(round(TotaalTopping, 3)))


print('                             ----- +')
print('Totaal:                      €'+ str(round(TotaalBedrag, 3)))