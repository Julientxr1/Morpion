import random as rd
def creation_tableau(liste):
    print("*************")
    for i in range(0,3):
        print("|",liste[i][0],"|",liste[i][1],"|",liste[i][2],"|")
        print("*************")
    return 1

def condition_victoire(liste):
    for i in range(0,3):
        if(liste[i][0]==liste[i][1]==liste[i][2]!=" "):
            if liste[i][0]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
    
    for i in range(0,3):
        if(liste[0][i]==liste[1][i]==liste[2][i]!=" "):
            if liste[0][i]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
    
    for i in range(0,3):
        if(liste[0][0]==liste[1][1]==liste[2][2]!=" "):
            if liste[1][1]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
        
        if(liste[0][2]==liste[1][1]==liste[2][0]!=" "):
            if liste[1][1]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
        
    for i in range(0,3):
        for j in range(0,3):
            if(liste[i][j]==' '):
                return 1
    print("Fin de jeu, aucun gagnant")
    return 0

def numero_case(nb:int,signe:str)->None:
    if nb == 1:
        liste[0][0] = signe
    if nb == 2:
        liste[0][1] = signe
    if nb == 3:
        liste[0][2] = signe
    if nb == 4:
        liste[1][0] = signe
    if nb == 5:
        liste[1][1] = signe
    if nb == 6:
        liste[1][2] = signe
    if nb == 7:
        liste[2][0] = signe
    if nb == 8:
        liste[2][1] = signe
    if nb == 9:
        liste[2][2] = signe

joueur1=input("Entrer le nom d'un Joueur : ")
joueur2=input("Entrer le nom de l'autre Joueur : ")
premier_joueur = joueur1 if rd.randint(0,1) == 0 else joueur2
second_joueur = joueur1 if premier_joueur == joueur2 else joueur2
print(premier_joueur, "est le premier Joueur !")
vide=" "
liste=[[vide,vide,vide], [vide,vide,vide], [vide,vide,vide]]
creation_tableau(liste)
signe='X'
while (condition_victoire(liste)):
    case=int(input("Entrer le numéro de case entre 1 et 9 : "))
    assert 0<case<=9, "Le numéro indiqué est incorrect"
    numero_case(case,signe)
    signe='O' if signe=='X' else 'X'
    creation_tableau(liste)

