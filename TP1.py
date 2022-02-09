import os

def ouvrir(pathfile):
    if os.path.isfile(pathfile):
        fic = open(pathfile,"r",encoding='utf-8')
        return fic
    else:
        print (f"le fichier {pathfile} n'existe pas (mauvais chemin ou erreur dans le nom de fichier ")
        return None

def exploiterFichier(fichier):
    entete = fichier.readline()
    entete = entete.rstrip("\n\r")
    listeE = entete.split(';')
    dict={}
    n=1
    for ligne in fichier:
        ligne = ligne.rstrip("\n\r")
       # print(f"Ligne {n} : {ligne}")
        listeV = ligne.split(';')
        dict2 ={}
        for i in range(2,len(listeE)):
            dict2[str(listeE[i])] = listeV[i]
        if listeV[1] not in dict.keys():
            dict[str(listeV[1])] = dict2
        else :
            print(f"doublon N° étudiant détécté {listeV[1]}")
    return dict
def traitementLigne(ligne,entete):
    dict = {}
    listeE = entete.split(';')
    listeV = ligne.split(';')
    for i in range(1,len(listeE)):
        dict[str(listeE[i])] = listeV[i]
    print(f"{dict['N° Etudiant']} : {dict['Note']}")

def affichage(etudiants, groupe=None):
    for num, etu in etudiants.items():
        if groupe==None:
            print (f"{num} : {etu['NOM']} note {etu['Note']}")
        else:
            if etu['Groupe']==groupe:
                print(f"{num} : {etu['NOM']} note {etu['Note']}")

def fichierAnonyme(etudiants, fichierOut):

def main():
    fichier = "files/un fichier de notes.txt"
    fic = ouvrir(fichier)
    if (fic != None):
        etudiant = exploiterFichier(fic)
        affichage(etudiant)

if __name__ == "__main__":
    main()