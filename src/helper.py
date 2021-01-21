# Fonction qui vérifie si deux strings sont "à peu près" égales
def isAlmostEqual(str1, str2):
    words1 = list(filter(None, str1.lower().replace(".", "").replace("'", " ").replace("!", "").split()))
    words2 = list(filter(None, str2.lower().replace(".", "").replace("'", " ").replace("!", "").split()))

    return words1 == words2