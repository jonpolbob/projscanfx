# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jonepol"
__date__ = "$29 juil. 2015 11:38:04$"


import datetime
import types

if __name__ == "__main__":
    print ("pas le bon main ! appeler projscanfx")

#paires=("EUR/USD","USD/JPY","GBP/USD","USD/CHF","AUD/USD","USD/CAD","NZD/USD")
paires=("EUR/USD","AUD/USD")

lstvaleurs=dict();

def gettimeutc():
    utc_datetime = datetime.datetime.utcnow()
    return utc_datetime.strftime("%Y-%m-%d %H:%M:%S")

wdays=("lun","mar","mer","jeu","ven","sam","dim")

#decode la string heure et en deduit le couple date-heure
#la date est corrigee si la date en argument est superieure a 23 et la date courante ==0
# car dans ce cas la date courante n'st pas applicabale a la date en argument, il fautrerer un jour
# ce qu'on fait
def decodeheure(heure):
    hh = int(heure[0:2])
    mm = int(heure[3:5])
    ss = int(heure[-2:])
    utc_datetime = datetime.datetime.utcnow()
    
    #getion du changemet e date : l'heure courante peut etre en avance su l'heure lue
    if utc_datetime.hour >=23 and hh==0:
        print ("correction date",utc_datetime.strftime(" %Y-%m-%d "))
        utc_datetime = utc_datetime - timedelta(hour=1) #on passe la date courante a l'heure prec pour avoir le jour prec 
    
    #jour de la semaine
    wd = wdays[utc_datetime.weekday()]    
    return wd+utc_datetime.strftime(" %Y-%m-%d=")+"%i:%i:%i"%(hh,mm,ss),wd,(utc_datetime.year,utc_datetime.month,utc_datetime.day,hh,mm,ss)

    
def decode(lastring):
    
    global lstvaleurs
    #print lstvaleurs
    tosave = 0
    #netttoyage de la chaine et reperage des champs
    if lastring.find(r"%")!=-1:
        lastring = lastring.replace("\n","")
        lastring = lastring.replace("\r","")
        paire = lastring[0:7]
        heure = lastring[-8:]
        numberstring = lastring[7:-8].replace(',','.')
        
        posvariation = numberstring.find("+")
        if posvariation==-1:
            posvariation =   numberstring.find("-")
        if posvariation==-1:
            posvariation = len(numberstring)-12
            print ("--------",lastring)
            
        #on rajoute artificiellement un point en plus a la fin 
        nombreok = numberstring[0:posvariation]+"0."    
        debpos=0
        
        nbentiere=nombreok.find(".") #regarde la position du premier decimal
        
        pospt = nombreok.find(".")
        debnbre = nombreok[pospt-nbentiere:pospt+1] #debut avant le pt
        nombreok = nombreok[pospt+1:] #on reaprt juste apres le pt decimal
        resu=[]

        #decodage des 4 valeurs
        for i in range(0,4):
            pospt = nombreok.find(".") #point suivant
            if pospt == 0: # c'est le dernier nombre (rien a decoder car on avait rajoute un . a la fin
                break;                
                
            finnbre = nombreok[0:pospt-nbentiere] #fin du nombre precedent
            txtvaleur =debnbre+finnbre
            #calcul en tics sur la premiere valeur
            if i==0:
                txttics = txtvaleur.replace(".","")
                valtics = float(txttics[0:5]+"."+txttics[5:])
                #print "tics:",valtics
                
            debnbre = nombreok[pospt-nbentiere:pospt+1] #fin : du point au debut du suivant
            nombreok = nombreok[pospt+1:] #nouveau nombre pile au debut du suivant
            resu.append(float(txtvaleur))
        
        #on ajoute la valeur  en tics comme erniere valeur
        #print txtvaleur,"->",nombreok
        resu.append(float(valtics))  #index 5 : valeur en tics    
        
        
        for lavaleur in range(0,5):
            if lstvaleurs[paire][lavaleur] != resu[lavaleur]:
                tosave=1                
                break;
                
        if tosave ==1:
            #valeur a sauver
            
            datetxt, joursem,datetuple = decodeheure(heure)
            #le premier arg de decodeheure et la date en texte
        
            nbsecs=0
            recordvalue=1
            #on calcule la duree de la periode deuis la dereniere mesure
            #l'heure est le tuple en position 6 ('est un int avant la premiere lecture)
            if type(lstvaleurs[paire][5]) is types.IntType : # on a encore un int en lieu et palce de derniere heure : pas initialise
                deltatime =0
            else:
                lastyy = lstvaleurs[paire][5][0]
                lastmm = lstvaleurs[paire][5][1]
                lastdd = lstvaleurs[paire][5][2]
                lasthh = lstvaleurs[paire][5][3]
                lastmn = lstvaleurs[paire][5][4]
                lastsec = lstvaleurs[paire][5][5]
                lstdate = datetime.datetime(lastyy,lastmm,lastdd,lasthh,lastmn,lastsec)
                curdate= datetime.datetime(datetuple[0],datetuple[1],datetuple[2],datetuple[3],datetuple[4],datetuple[5])
                deltatime = curdate-lstdate
                nbsecs = deltatime.seconds
                refdate = datetime.datetime(2010,1,1,0,0,0)
                deltatime = curdate-refdate
                absdate = deltatime.seconds
                
                #valeurs du tic precedent a renrgistrer dans la base, complete par sa duree
                recordduree = nbsecs               #duree du tick prec
                recordtime = lstvaleurs[paire][5]  #heure du tic prec
                recordvalue = lstvaleurs[paire][0] #valeur du tic prec
                recordtics = lstvaleurs[paire][4]
                recordabsdate = absdate #date assolue de puis 1 jan 2010
                recordjoursem = joursem #attention c'est pas la bonne date, il faut enregistrer la date du tic prec
                recordprvvalue = lstvaleurs[paire][0] #valeur du tic prec
               
                
            #on met  a jour la derniere tranche et on sauvegarde les valeurs et sa date
            lstvaleurs[paire][5] = datetuple
            for lavaleur in range(0,5):
                lstvaleurs[paire][lavaleur] = resu[lavaleur]
           
           #petit afficahge de resu , resu en tics et delat de variatuion
            if deltatime !=0:
                print( paire+" "+datetxt,"(",nbsecs,"sec) :",resu[0],resu[4],recordtics,"delte ",(resu[4]-recordtics)," ",datetuple)
            else:
                print (paire+" "+datetxt,"(",nbsecs,"sec) :",resu,datetuple)
            
    return tosave    
