messages_gr3 = {
    "pseudo" : "DebugWoman",
    "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
    "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
}

messages_decrypte=[]
liste_alphabet=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
liste_nombres=['1','2','3','4','5','6','7','8','9']

for message in messages_gr3["cryptes"]:
    decrypte = ""
    for caractere in message:
        if caractere in liste_alphabet:
            decrypte += liste_alphabet[liste_alphabet.index(caractere)-4]
        elif caractere in liste_nombres:
            decrypte += liste_nombres[liste_nombres.index(caractere) - 4]
        else:
            decrypte+=caractere
    messages_decrypte.append(decrypte)

for i in range(len(messages_decrypte)):
    if messages_decrypte[i]!=messages_gr3["messages"][i]:
        print(f"Attention, le message {i+1} a été intercepté")
