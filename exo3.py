def crypter_mot(mot):
    # Vérification que le mot est non vide et contient uniquement des lettres majuscules
    if not mot.isalpha() or not mot.isupper():
        return "Le mot doit être non vide et composé uniquement de lettres majuscules."

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longueur_alphabet = len(alphabet)
    mot_crypte = ""

    for lettre in mot:
        # Calcul du nombre d'occurrences de la lettre
        n = mot.count(lettre)

        # Détermination de K
        if n % 2 == 1:  # n est impair
            k = 2 * n
        else:  # n est pair
            k = n // 2

        # Index de la lettre cryptée
        index_actuel = alphabet.index(lettre)
        nouvel_index = (index_actuel + k) % longueur_alphabet
        lettre_cryptee = alphabet[nouvel_index]

        # Ajout de la lettre cryptée au mot crypté
        mot_crypte += lettre_cryptee

    return mot_crypte


# Saisie du mot
mot = input("Entrez un mot non vide (lettres majuscules uniquement) : ")
mot_crypte = crypter_mot(mot)
print("Mot crypté :", mot_crypte)