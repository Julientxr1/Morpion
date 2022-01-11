import random as rd


def creation_tableau(liste): #  Création de la grille de jeu 
    print("*************")
    for i in range(0,3):
        print("|",liste[i][0],"|",liste[i][1],"|",liste[i][2],"|")
        print("*************")
    return 1


def condition_victoire(liste):
    for i in range(0,3): #  On vérifie les lignes
        if(liste[i][0]==liste[i][1]==liste[i][2]!=" "):
            if liste[i][0]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
    
    for i in range(0,3): #  On vérifie les colonnes
        if(liste[0][i]==liste[1][i]==liste[2][i]!=" "):
            if liste[0][i]=='X' :
                print("Victoire de", premier_joueur,"!")
            else :
                print("Victoire de", second_joueur,"!")
            return 0
    
    for i in range(0,3):  #  On vérifie les diagonales
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
        
    for i in range(0,3): #  On vérifie qu'il reste des cases vides
        for j in range(0,3):
            if(liste[i][j]==' '):
                return 1
    print("Fin de jeu, aucun gagnant")
    return 0


def numero_case(nb:int,signe:str)->None: #  Indication des cases 
    if nb == 1:
        position_case = (0,0)
    if nb == 2:
        position_case = (0,1)
    if nb == 3:
        position_case = (0,2)
    if nb == 4:
        position_case = (1,0)
    if nb == 5:
        position_case = (1,1)
    if nb == 6:
        position_case = (1,2)
    if nb == 7:
        position_case = (2,0)
    if nb == 8:
        position_case = (2,1)
    if nb == 9:
        position_case = (2,2)

    try:  #  Marque la case en fonction de signe, si la case est vide (si position_case n'est pas définie renvoie rien)
        if liste[position_case[0]][position_case[1]] == " ":
            liste[position_case[0]][position_case[1]] = signe
    except:
        return


if __name__== "__main__":
    joueur1 = input("Entrer le nom d'un Joueur : ")
    joueur2 = input("Entrer le nom de l'autre Joueur : ")
    try:  #  Les joueurs doivent entrés des noms différents
        assert joueur1!=joueur2
        bon_pseudo = True
    except AssertionError:
        print("Les 2 joueurs ne peuvent pas avoir les mêmes noms !")
        bon_pseudo = False

    if bon_pseudo :
        premier_joueur = joueur1 if rd.randint(0,1) == 0 else joueur2  #  On choisit qui commence de manière aléatoire
        second_joueur = joueur1 if premier_joueur == joueur2 else joueur2
        print(premier_joueur, "est le premier Joueur !")
        vide = " "
        liste = [[vide,vide,vide], [vide,vide,vide], [vide,vide,vide]]
        creation_tableau(liste)
        signe = 'X'
        tour = premier_joueur
        while (condition_victoire(liste)):
            case = input(f"{tour}, entrez le numéro de la case entre 1 et 9 : ")  # Le f"" ou f-string sert a remplacer le contenu des acolades das une chaine de caractère
            try: # On vérifie que les joueurs ont indiqué un chiffre entre 1 et 9
                case = int(case)
                assert 0<case<=9 
            except ValueError :
                print("La valeur indiquée est incorrect")
            except AssertionError:
                print("Veuillez saisir un numéro correct !")
            
            numero_case(case, signe)
            signe = 'O' if signe == 'X' else 'X'
            tour = premier_joueur if tour == second_joueur else second_joueur
            creation_tableau(liste)