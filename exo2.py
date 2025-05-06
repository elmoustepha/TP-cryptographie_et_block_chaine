def decrypter():
    Res = ""  
   
    i = 0  
    if len(CH)>5:
          return "la caractere depasse a 5"
    
    while i < len(CH) :

            lettre = CH[i + 1] 

            num = int(CH[i])

            Res +=  num * lettre
           
            i += 2 
       
    return Res


CH = input("Entrez une chaîne cryptée : ")
print("Résultat décrypté :", decrypter())