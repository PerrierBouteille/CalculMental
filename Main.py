import random
from time import *
import os

#Variable
L = ['+','-','*']
score = 0
para = 1
clear = lambda: os.system('cls')

print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print(' Bienvenue')
print()
print(' | Jeu: Calcul Mental')
print('')
print(' > Préparation en cours..')
print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print()
sleep(1.5)

while para:
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print(' Paramètre:')
    print(' | Choisissez le nombre max')
    print(' | 10')
    print(' | 100')
    print(' | 1000')
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print()
    max = int(input('[> Nombre max: '))
    if(max == 10 or max == 100 or max == 1000):
        para = 0
    else:
        para = 1
        print()
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print('Erreur')
        print(' | Le nombre donné n\'est pas valide.')
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print()
        sleep(1)


#1er input demande a l'utilisateur le nombre de question qu'il veut.
print()
print()
x = int(input('[> Entrer le nombre de question voulu: '))
clear()

for i in range(x):
    #Génération du calcul
    a = random.randint(1,max)
    b = random.randint(1,max)
    signe = random.randint(0,2)
    # r = resultat 
    r = str(a) + '' + L[signe] + '' + str(b)
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print('Question n°' + str(i+1))
    print()
    print('Calculez:')
    print(' | ' + str(a) + '' + L[signe] + '' + str(b))
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print()

    #Logs admin
    #print(eval(r))

    rep = input('[> Votre réponse : ')
    
    #print(str(rep) + " " + str(eval(r)))

    #Vérification de la réponse de la personne par rapport au calcul demandé
    #eval est pour demander a python de faire un calcul a paritr d'un string.
    if(str(rep) == str(eval(r))):
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print('     Bien  joué !')
        print()
        print(' Effectivement: '+ str(a) + '' + L[signe] + '' + str(b) + ' = ' + str(eval(r)))
        print()
        print(' + 1 de score')
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

        score+=1
    else:
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print('     Dommage !')
        print()
        print(' |> '+ str(a) + '' + L[signe] + '' + str(b) + ' = ' + str(eval(r)) + ' et non ' + str(rep)) #Ecriture du calcul avec la reponse correct
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    clear()

#Calcul pourcentage reponse correct
totalScore = (score / x) * 100
print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print('                    FIN                        ')
print('  Tu as',score,'questions correcte sur', x)
print('  soit ',totalScore,'% de réponse correct.')
print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')




