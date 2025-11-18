cle_gr3 = [
    ['a','b','c','d','e','f','g','h','i'],['k','l','m','n','o','p','q','r'],['s','t','u','v','w','x','y','z','é'],
    ['1','2','3','4','5','6','7','8','9']
]

message='Je vais réussir cet examen'

"""
Pseudocode:
======================
Retirer les epaces dans message
Mettre les caractères de message en minuscule
Créer un string vide pour contenir le message crypté (message_crypte = "")

for lettre in message
    for liste in cle_gr3
        if liste contient lettre:
            caractère_crypté = cle_gr3[3][liste.index(lettre)]
            message_crypte += caractere_crypte
            break
"""