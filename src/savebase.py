# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jonepol"
__date__ = "$31 juil. 2015 17:28:58$"

if __name__ == "__main__":
    print "Hello World"


def savebase(paire,heuretxt,joursem,heureabs,val, valprec, tics, duree):
    #mise en forme de la paire pour en afire un nom de base
    nomtable=paire.replace("/","")
    
    