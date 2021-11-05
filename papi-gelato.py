from time import sleep

def tijd():
    sleep(2)

def error():
    print('Sorry, dat snap ik niet...')

def stap2():
   bakje = input('Wilt u deze '+ str(Bolletjes) +' in A) een hoorntje of B) een bakje? ').upper()
   if bakje == 'A':
       Doorgaan = input('Hier is uw hoorntje met '+ str(Bolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
   elif bakje == 'B':
       Doorgaan = input('Hier is uw bakje met '+ str(Bolletjes) +' bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
   else:
       error()
    

        
# Code start ---
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is')
tijd()
Bolletjes = int(input('Hoeveel bolletjes wilt u? '))
if Bolletjes >= 1 or 3 <= Bolletjes:
    stap2()
else:
    print('fout')
