def crypter_chaines():
    res = ""

    for char in CH:
        if char.isalpha():
            
            res += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            res += char
    
    return res

# Demande à l'utilisateur d'entrer une chaîne
CH = input("Entrez une chaîne à crypter : ")
print("La chaîne cryptée est :", crypter_chaines())