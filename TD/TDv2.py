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
        etudiant = {}
        """   
        for i in range(1,len(listeV)):
            print(f"{listeE[i]} : {listeV[i]}")

        print("-------------------\n")
        """
        dict2 ={}
        """
        dict2["Nom"] = listeV[2]
        dict2["Prénom"] = listeV[3]
        dict2["Groupe"] = listeV[4]
        dict2["Note"] = listeV[5]
        #print(dict2)
        """
        # remplace tous les lignes commentées au dessus.
        for i in range(2,len(listeV)):
            dict2[listeE[i]] = listeV[i]

        dict[listeV[1]] = dict2
        #print("-------------------")

    return dict

def affichage(etudiants):
    for value in etudiants.values():
        print(f"Nom={value['NOM']} {value['Prénom']} Note={value['Note']}")

def affichageAnonyme(etudiants):
    for key, value in etudiants.items():
        print(f"N° étudiant {key} : Note={value['Note']}")

def main():
    fichier = "files/un fichier de notes.txt"
    fic = ouvrir(fichier)
    if (fic != None):
        etudiants = exploiterFichier(fic)
        # affichage(etudiants)
        affichageAnonyme(etudiants)
 #       fichierAnonyme(etudiants,"files/fichier anonyme.txt")


if __name__ == "__main__":
    main()