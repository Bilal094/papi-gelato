# Time import ---

from time import sleep

# Variabelen --- 
ZakelijkOfParticulier = True
ZakelijkBool = True
Herhalen = True
MeerBestellen = True
Bolsmaak = 1
Smaken = ["A", "C", "M", "V", "a", "c", "m", "v", "Aardbei", "Chocolade", "Munt", "Vanille", "aardbei", "chocolade", "munt", "vanille"]
BolletjePrijs = 1.10
HorrentjePrijs = 1.25
BakjePrijs = 0.75
Slagroom = 0.50
Sprinkels = 0.30
CaramelHoorntje = 0.60
CaramelBakje = 0.90
SmaakLiter = 1
TotaalLiter = 0
LiterPrijs = 9.80
AantalBakjes = 0
AantalHoorntjes = 0
AlleBolletjes = 0
Topping = 0
AantalSlagroom = 0
AantalSprinkels = 0
AantalCaramel = 0
# User-Defined functions ---

def showIntro():
    print('Welkom bij Papi Gelato')

def pause():
    sleep(1.5)

def showError():
    print('Sorry, dat snap ik niet...')

def showErrorBakje():
    print('Sorry, zulke grote bakken hebben we niet.')

def smaak():
    Bolsmaak = 1
    while Bolsmaak <= AantalBolletjes:
        Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
        if Smaak in Smaken:
            Bolsmaak += 1
        else:
            showError()

def topping(topping):
    global Topping, AantalSlagroom, AantalSprinkels, AantalCaramel

    
    if ToppingVraag == "A" or ToppingVraag == "Geen":
        Topping = 0
    elif ToppingVraag == "B" or ToppingVraag == "Slagroom":
        AantalSlagroom += Slagroom
        Topping += 1
    elif ToppingVraag == "C" or ToppingVraag == "Sprinkels":
        AantalSprinkels += Sprinkels * AantalBolletjes
        Topping += 1
    elif ToppingVraag == "D" or ToppingVraag == "Caramel saus" or ToppingVraag == "Caramel":
        if Bakje == "A" or Bakje == "Hoorntje":
            AantalCaramel += CaramelHoorntje
        if Bakje == "B" or Bakje == "Bakje":
            AantalCaramel += CaramelBakje
        Topping += 1
    return AantalSlagroom or AantalSprinkels or AantalCaramel



# Code start ---
showIntro()
pause()

# Zakelijke vragen
while ZakelijkOfParticulier:
    Zakelijk = input('Bent u 1) particulier of 2) zakelijk? ').upper()
    if Zakelijk == "1" or Zakelijk == "Particulier":
        ZakelijkOfParticulier = False
        Herhalen = True
    elif Zakelijk == "2" or Zakelijk == "Zakelijk":
        ZakelijkOfParticulier = False
        Herhalen = False
    else:
        showError()
        ZakelijkOfParticulier = True

# Zakelijke vragen
if Herhalen == False:
    Liter = int(input('Hoeveel liter ijs wilt u? '))

    while SmaakLiter <= Liter:
        SmaakLiterVraag = input('Welke smaak wilt u voor de '+ str(SmaakLiter) +'e liter? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
        if SmaakLiterVraag in Smaken:
            SmaakLiter += 1
        else:
            showError()

    ZakelijkBool = True

# Particuliere vragen
while Herhalen:
    ZakelijkBool = False
    AantalBolletjes = int(input('Hoeveel bolletjes wilt u? '))
    
    # Als de klant tussen de 1 of 3 bolletjes wilt
    if AantalBolletjes >= 1 and AantalBolletjes <= 3:

        # Hier wordt de klant gevraagd om de smaken voor zijn bolletjes
        smaak()
        
        Bakje = input('Wilt u deze '+ str(AantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje? ').upper()

        ToppingVraag = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ').upper()
        topping(ToppingVraag)

        
        # Hier wordt de klant gevraagd of hij een bakje of een hoorntje wilt en daarna wordt de code afgesloten of, als de klant het wilt, opnieuw 'afgespeeld'
        if Bakje.upper() == 'A':
            AantalHoorntjes += 1

            Doorgaan = input('Hier is uw hoorntje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
            if Doorgaan == 'Y':
                Herhalen = True
            elif Doorgaan == 'N':
                print('Bedankt en tot ziens!') 
                Herhalen = False
            else:
                showError()
                MeerBestellen = True
            
        elif Bakje.upper() == 'B':
            AantalBakjes += 1
            while MeerBestellen:
                Doorgaan = input('Hier is uw bakje met '+ str(AantalBolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').upper()
                if Doorgaan == 'Y':
                    Herhalen = True
                    MeerBestellen = False
                elif Doorgaan == 'N':
                    Herhalen = False
                    MeerBestellen = False
                    print('Bedankt en tot ziens!')
                else:
                    showError()
                    MeerBestellen = True



    # Als de klant tussen de 4 of 8 bolletjes wilt
    elif AantalBolletjes >= 4 and AantalBolletjes <= 8:
        AantalBakjes += 1
        print('Dan krijgt u van mij een bakje met '+ str(AantalBolletjes) +' bolletjes.')
        Bakje = "B" or "Bakje"
        smaak()
                
        ToppingVraag = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ').upper()
        topping(ToppingVraag)

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

    

# Particulier
if ZakelijkBool == False:
    AlleBolletjes += AantalBolletjes
    TotaalBol = AlleBolletjes * BolletjePrijs
    TotaalHoorntje = AantalHoorntjes * HorrentjePrijs
    TotaalBak = AantalBakjes * BakjePrijs
    TotaalTopping = AantalSlagroom + AantalCaramel + AantalSprinkels
    TotaalBedrag = TotaalBol + TotaalHoorntje + TotaalBak + TotaalTopping


# Zakelijk
if ZakelijkBool == True:
    TotaalBedragZakelijk = Liter * LiterPrijs
    BTW = TotaalBedragZakelijk * 0.09

if ZakelijkBool == False:
    print()
    print('--------------[Papi Gelato]--------------')
    print()
    if AantalBolletjes >= 1:
        print('Bolletjes        '+ str(AlleBolletjes) +' x €1,10 = €'+ str(round(TotaalBol, 3)))

    if AantalHoorntjes >= 1:
        print('Horrentje        '+ str(AantalHoorntjes) +' x €1,25 = €' + str(round(TotaalHoorntje, 3)))

    if AantalBakjes >= 1:
        print('Bakje            '+ str(AantalBakjes) +' x €0,75 = €'+ str(TotaalBak))

    if Topping >= 1:
        print('Topping          '+ str(Topping) +' x €'+ str(round(TotaalTopping, 3)) +' = €'+ str(round(TotaalTopping, 3)))


    print('                             ----- +')
    print('Totaal:                      €'+ str(round(TotaalBedrag, 3)))

if ZakelijkBool == True:
    print()
    print('--------------[Papi Gelato]--------------')
    print()
    print('Liter       '+ str(Liter) +' x €9.80 = €'+ str(round(TotaalBedragZakelijk, 3)))
    print('                        ------ +')
    print('Totaal                 = €'+ str(TotaalBedragZakelijk))
    print('BTW (9%)               = €'+ str(BTW))