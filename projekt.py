from random import *
a="A"
A="A"
b="B"
B="B"
c="C"
C="C"
d="D"
D="D"
ckrivo=0
cpitanja=0
ctocno=0
ulaz=open("quiz.txt","r")
par=ulaz.readlines()
for i in range (len(par)-1):
    par[i] = par[i].strip("\n")

rjecnik_stalni={}
for i in range(len(par)):
    newlist=par[i].split("/")
    rjecnik_stalni.update({newlist[0]:newlist[1]})
rjecnik_pitanja=rjecnik_stalni.copy()

while ckrivo < 3:
    cpitanja+=1
    par=rjecnik_pitanja.items()
    rng=randint(0,len(par)-1)
    pitanje_odgovori=list(par[rng])
    pitanje=pitanje_odgovori[0]

    rjecnik_pitanja.pop(pitanje_odgovori[0])
    
    newlist=pitanje_odgovori[1].split(" ")
    tocno=newlist[0]
    print(pitanje + "\n")

    rng = randint(0,3)
    print("A:" + newlist[rng])
    if newlist[rng] == tocno:
        odgovor = "A"
    newlist.remove(newlist[rng])
    rng = randint(0,2)
    print("B:" + newlist[rng])
    if newlist[rng] == tocno:
        odgovor = "B"
    rng = randint(0,1)
    print("C:" + newlist[rng])
    if newlist[rng] == tocno:
        odgovor = "C"
    newlist.remove(newlist[rng])
    print("D:" + newlist[0] + "\n")
    if newlist[0] == tocno:
        odgovor = "D"

    mojodgovor=input()
    if mojodgovor.upper() == odgovor:
        ctocno+=1
        if cpitanja == len(rjecnik_stalni):
            print("\n" + "VICTORY ROYALE!!!" + "\n")
            print("Osvojio/la si {}/{} bodova".format(ctocno,len(rjecnik_stalni)) + "\n")
            break
        else:
            print("\n" + "tocno" + "\n" + "Trenutno imaš {} bodova".format(ctocno) + "\n")
    elif ckrivo < 2:
        ckrivo+=1
        print("\n" + "Krivo!!" + "\n" + "Imaš još {} pokušaja".format(3-ckrivo) + "\n")
    else:
        print("\n" + "YOU LOSE NUB!!" + "\n")
        print("Osvojio/la si {}/{} bodova".format(ctocno,len(rjecnik_stalni)) + "\n")
        break
