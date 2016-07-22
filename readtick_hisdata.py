#!/usr/bin/python
# -*- coding: latin-1 -*-

__author__ = 'jonepol'


#lit les fichiers ihsda et en fait des tranches de 10 secondes (ou 1 minute)
#lus sur histdata.com
#ouvre le zip
#fait une moyenne sur timebin secondes timebin =10
#calcule qq parametres temporels style bollinger, etc.


chemin ="c:\\essais\\hisdata"

#lire un zip
import zipfile
import csv
import io

def scanzip(paire,annee, mois):
    nomfich = "c:\\essais\\hisdata"+"\\"+"HISTDATA_COM_ASCII_EURUSD_T201606"+".zip"
    lezip = zipfile.ZipFile(nomfich)
    lecsv = lezip.open("DAT_ASCII_EURUSD_T_201606.csv","rU")

    lecsv_file  = io.TextIOWrapper(lecsv)

    reader = csv.reader(lecsv_file,  delimiter=',')
    for row in reader: #chaque ligne est un tple
        annee = int(row[0][0:4])
        mois = int(row[0][4:6])
        jour = int(row[0][6:8])
        heure = int(row[0][9:11])
        minute = int(row[0][11:13])
        seconde = int(row[0][13:15])
        milli = int(row[0][15:])
        nb1 = float(row[1])
        nb2 = float(row[2])
       #check : c'est bon ca importe bien
       #print(annee,mois,jour,heure,minute,seconde,milli,nb1,nb2)


    #print data

    #for line in lecsv:
    #    print(line)



scanzip("EURUSD",2016,5)