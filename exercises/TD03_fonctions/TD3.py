#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    "la fonction prend 4 parametre qui est un tuple"
    return temps[3] + temps[2] * 60 + temps[1] * 3600 + temps[0] * 3600 * 24

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))  
print(tempsEnSeconde((0, 0, 0, 33)))  
print(tempsEnSeconde((0, 0, 1, 12)))  



def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    return (seconde // (3600 * 24), seconde//3600 % 24, seconde // 60 % 60, seconde % 60 ) 

temps = secondeEnTemps(342094) 

print(temps)s

#fonction auxiliaire ici

def afficheTemps(temps):
    if temps [0] == 1 :
        print("1 jour")
    elif temps[0] > 1 :
        print(temps[0], "jours")

    if temps[1] == 0:
        print("1 heure")
    elif temps[1] > 1 :
        print(temps[1], "heures")

    if temps[2] == 0 :
        print("1 minutes")
    elif temps[2] > 0 :
        print(temps[2], "minutes")

    if temps[3] == 1 :
        print("1 seconde")
    elif temps[3] > 1 :
        print(temps[3], "secondes")

    
afficheTemps((1,0,14,23))

def demandeTemps():
    n = int(input("enter a day"))
    h = 24
    while h > 24 :
        h = int(input("enter a hours"))
    m = 60
    while m >= 60 :
        m = int(input("enter a minute"))
    s = 60 
    while s >= 60 :
        s = int(input("enter a seconde"))
    return(n, h, m, s)

afficheTemps(demandeTemps())
'''
# on veut etre capable d'additionner 2 temps , donner une fonction qui fait ce calcul 
'''
def sommeTemps(temps1,temps2):
    temps1Ensec = tempsEnSeconde(temps1)
    temps2Ensec = tempsEnSeconde(temps2)
    sommeEnSec = temps1Ensec + temps2Ensec 
    return secondeEnTemps(sommeEnSec)



afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))
'''
def proportionTemps(temps,proportion):
    
    return secondeEnTemps(int(tempsEnSeconde(temps))*proportion)



afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments

def testBisextile(Annee):
    if Annee % 4 == 0 and (not Annee % 100 == 0 or Annee % 400 == 0):
        return(True)
    else:
        return(False)

def LongueurMois(Mois,Annee):
    if Mois % 2 == 1 and Mois < 8 :
        return(31)
    elif Mois == 2 and testBisextile(Annee) == True:
        return(29)
    elif Mois == 2 and testBisextile(Annee) == False:
        return(28)
    elif Mois % 2 == 0 and Mois < 8:
        return(30)
    elif Mois % 2 == 1 and Mois >= 8:
        return(30)
    elif Mois % 2 == 0 and Mois >= 8:
        return(31)

def tempsEnDate(temps):
    Date = list((1970,1,1,0,0,0))
    Date[5] += temps[3]
    Date[4] += temps[2]
    Date[3] += temps[1]
    Date[2] += temps[0]
    while Date[2] > LongueurMois(Date[1],Date[0]):
        Date[2] -= LongueurMois(Date[1],Date[0])
        Date[1] += 1
        while Date[1] > 12:
            Date[1] -= 12
            Date[0] += 1
    Date = tuple((Date[0],Date[1],Date[2],Date[3],Date[4],Date[5]))
    return(Date)
    pass

def afficheDate(date):
    date2 = list(date)
    if date2[1] == 1:
        date2[1] = 'Janvier'
    elif date2[1] == 2:
        date2[1] = 'Fevrier'
    elif date2[1] == 3:
        date2[1] = 'Mars'
    elif date2[1] == 4:
        date2[1] = 'Avril'
    elif date2[1] == 5:
        date2[1] = 'Mai'
    elif date2[1] == 6:
        date2[1] = 'Juin'
    elif date2[1] == 7:
        date2[1] = 'Juillet'
    elif date2[1] == 8:
        date2[1] = 'Aôut'
    elif date2[1] == 9:
        date2[1] = 'Septembre'
    elif date2[1] == 10:
        date2[1] = 'Octobre'
    elif date2[1] == 11:
        date2[1] = 'Novembre'
    else:
        date2[1] = 'Décembre'
    print(date2[2]," ",date2[1]," ",date2[0]," ",date2[3],":",date2[4],":",date2[5],sep='')
    pass
    
temps = secondeEnTemps(4000000000)
afficheDate(tempsEnDate(temps))


temps = secondeEnTemps(1000000000)
afficheDate(tempsEnDate(temps))
