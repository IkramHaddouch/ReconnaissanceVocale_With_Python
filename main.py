from fonctions import *

#les traitement sur le mot hello
ErreurclientH1, ErreurimposteurH1, client1, imposteur1 = traitement1('1', 'hello', '3', '4', '6')
ErreurclientH2, ErreurimposteurH2, client2, imposteur2  = traitement1('2', 'hello', '1', '7', '5')
ErreurclientH3, ErreurimposteurH3,client3, imposteur3 = traitement2('3', 'hello', '7', '8', '9', '10')

''' resultat '''

print("pour le mot hello ")
print("test 1 ")
print("l'erreur de client = "+str((ErreurclientH1/7)*100))
print("l'erreur de impostor = "+str((ErreurimposteurH1/19)*100))
print("test 2 ")
print("l'erreur de client = "+str((ErreurclientH2/7)*100))
print("l'erreur de impostor = "+str((ErreurimposteurH2/19)*100))
print("test 3 ")
print("l'erreur de client = "+str((ErreurclientH3/6)*100))
print("l'erreur de impostor = "+str((ErreurimposteurH3/19)*100))

print(client1)
print(imposteur1)
print(client2)
print(imposteur2)
print(client3)
print(imposteur3)
