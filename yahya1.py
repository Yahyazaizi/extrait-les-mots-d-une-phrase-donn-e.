# Saisie de la phrase
phrase = input("Entrez une phrase : ")

# Utilisation de la fonction split pour extraire les mots
mots = phrase.split()

# Affichage des mots extraits
print("Les mots de la phrase sont :")
for mot in mots:
    print(mot)
