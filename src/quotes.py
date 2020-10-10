# Import du random
from random import choices, randint



# Structure des citations
class Quote:
    """
    L'objet Quote est utilisé pour représenter une citation d'un professeur, ou autre.\n
    Il est composé de plusieurs attributs :
     - text : Cela représente le texte de la citation, qui sera affiché à l'écran, cela doit être un string
     - author : Cela représente l'auteur de la citation, ce sera affiché en dessous du texte de la citation
     - weight : Cela représente la pondération de la citation, ses chances d'être choisie. Valeur si non fourni : 100
    Finalement, il existe une variable de classe currentTotalWeight, qui est utilisée pour calculer les poids cumulés.\n
    Cette variable contient la somme des poids de tout les poids des citations.
    """

    # Initialisation d'une variable de classe, pour définir des poids cumulatifs
    currentTotalWeight = 0

    def __init__(self, text, author, weight = 100):
        # Initialisation de attributs
        self.text = text
        self.author = author

        # On ajoute le poids de la quote au total des poids, cela sert à calculer les poids cumulatifs
        Quote.currentTotalWeight += weight

        # Ajout dans les listes, pour pouvoir être choisi par la fonction choices
        quotes.append(self)
        quotesWeight.append(Quote.currentTotalWeight)



global quotesToPull
quotesToPull = []

# Tirage d'une citation
def random_quote():
    """ Tire une citation au hasard dans la liste pondéré des citations """
    # On définit la liste comme global, ainsi elle sera maintenue entre plusieurs appels de la fonction
    global quotesToPull

    # On regarde si la liste contient des quotes
    if len(quotesToPull) == 0:
        # Si la liste est vide, on prend 12 éléments de la liste, avec répétition, car on peut pas faire autrement
        quotesToPull = choices(quotes, cum_weights = quotesWeight, k = 12)
        
        # On prepare une liste pour y stocker les index des valeurs à supprimer
        toDelete = []

        # On cherche les répétitions
        for i in range(len(quotesToPull)):
            for j in range(len(quotesToPull)):

                # On vérifie que seule une des deux valeurs se fasse supprimer
                if quotesToPull[i] == quotesToPull[j] and i < j:

                    # On évite les répétions dans la liste
                    if j not in toDelete:
                        toDelete.append(j)

        # On trie la liste dans l'ordre décroissant, pour éviter les éléments de changer d'index
        toDelete.sort()
        toDelete.reverse()

        # Et on les éliminent un par un
        for i in toDelete:
            del quotesToPull[i]

    # Puis on return une citation au hasard et l'enlève de la liste
    return quotesToPull.pop(randint(0, len(quotesToPull) - 1))

# Création des listes des citations
quotes = []
quotesWeight = []



""" Definition des citations """

# Guide pour pondérer les citations :
# Vide si c'est une citation commune/emblématique d'un prof
# 80 si elle est un peu plus rare
# 70 si elle vient d'un philosophe/auteur ...
# 50 si elle vient d'un élève
# 30 si c'est plus une blague qu'autre chose


# Citations de Vincent
Quote("C'est moins simple.", "Vincent V.K.")
Quote("C'est moins marrant.", "Vincent V.K.")
Quote("On va pas être copain.", "Vincent V.K.")
Quote("C'est presque évident.", "Vincent V.K.")
Quote("Je ressemble plus à une vache que vous à des scientifiques.", "Vincent V.K.")
Quote("C'est **tragique !**", "Vincent V.K.")
Quote("Ça, c'est tout à fait remarquable.", "Vincent V.K.")
Quote("Pas de regrets, vous avez pas le niveau !", "Vincent V.K.")
Quote("Oui, bien sûr!", "Vincent V.K.")
Quote("N'utilisez pas de blanco, n'utilisez pas de gomme. Encadrez vos erreurs !", "Vincent V.K.")
Quote("Bon les enfants, c'est l'heure !", "Vincent V.K.")
Quote("Tout le reste, c'est une question d'échelle.", "Vincent V.K.", 80)
Quote("Ce qui est un signe de maladie mentale.", "Vincent V.K.", 80)
Quote("Pôle Emploi va vous recevoir ... vous aurez pas de travail, mais il va vous recevoir !", "Vincent V.K.", 80)
Quote("Vous tapez sur des clous, vous vous tapez une fois sur le doigt.\n Ça vous a plu, du coup vous allez le refaire !", "Vincent V.K.", 80)


# Citations de Stefano
Quote("Le cahier de prépa est à jour.", "Stefano S.")
Quote("Reviens dans une heure.", "Stefano S.")
Quote("Ne seront lues que les réponses dont les __résultats ou mots importants sont ENCADRÉS__, et dont on a vérifié l'__HOMOGÉNÉITÉ__.", "Stefano S.")
Quote("On connait une tension, on cherche une tension.", "Stefano S.")
Quote("On passe au plat de résistance ?", "Stefano S.")
Quote("Les notes, on s'en fout ! Si tu veux, je te mets un 20.", "Stefano S.")
Quote("Il y a ampère à gauche et il y a ampère à droite.", "Stefano S.")
Quote("Là la tension elle fluctue donc c'est pas facile.", "Stefano S.")
Quote("Quelle horreur !", "Stefano S.")
Quote("On ne peut pas faire de physique sans schéma.", "Stefano S.")
Quote("Non, ça sonne à 13h05.", "Stefano S.", 80)


# Citations de Baptiste
Quote("Tout seul on va plus vite, ensemble on va plus loin.", "Baptiste H. (proverbe africain)")
Quote("Oh, c'est pas très sympatique ça.", "Baptiste H.")
Quote("Il y a des normes.", "Baptiste H.", 80)


# Citations de René
Quote("M. RINGOT, **DEVANT !**", "René L.")
Quote("Il n'y a que des vielles version à la noix de coco !", "René L.")
Quote("Je veux pas d'élèves comme ça, il sait tout faire, je peux pas lui crier dessus !", "René L.")
Quote("Toi, cours jusqu'à la salle des profs et fait moi 15 photocopies du sujet !", "René L.", 80)
Quote("Toi, t'as envie d'aller au tableau ? Bien sûr que tu as envie !", "René L.", 80)


# Citations de Claire
Quote("Ok guys!", "Claire T.B.")
Quote("Guys?!", "Claire T.B.")
Quote("Salut, ça va ? Il va comment ton chat ?\nAh bas, c'est un chat effrayé par les concombres !", "Claire T.B.")
Quote("Un panda, c'est pas un raton-laveur.", "Claire T.B.")
Quote("C'est vraiment cette heure là.", "Claire T.B.")
Quote("Le truc, c'est que si il marche sur ses petits *paws*. Sur ses petits pots. Sur ses coussinets.", "Claire T.B.", 80)
Quote("A washing raton.", "Claire T.B.", 80)


# Citations de philosophes/auteurs
Quote("Quiconque lutte contre des monstres devrait prendre garde, dans le combat, à ne pas devenir monstre lui-même.\n" + \
      "Et quant à celui qui scrute le fond de l'abysse, l'abysse le scrute à son tour.", "Friedrich Nietzsche", 70)
Quote("Dieu est mort ! Dieu reste mort ! Et c'est nous qui l'avons tué !\nComment nous consoler, nous les meurtriers des meurtriers ?", "Friedrich Nietzsche", 70)
Quote("Seule deux choses sont infinies, l'univers et la bêtise humaine.\nMais pour l'univers, je n'en ai pas encore la certitude absolue.", "Albert Einstein", 70)
Quote("Maintenant j'ai devenu la Mort, le destructeur de monde.", "J. Robert Oppenheimer", 70) # La faute est authentique à la citation originelle


# Citations des élèves - Note, pas fait pour les insultes, juste pour quand quelqu'un sort quelque chose de mémorable
# De plus, ne rajouter pas vos propres citation, ça ne se fait pas. Si c'était assez mémorable, quelqu'un d'autre le rajoutera à votre place
Quote("Le masque il faut le brancher à un avion.", "Nathan F.", 50)


# Citations anonymes
Quote("Tout est relatif, sauf la vodka, qui est absolute !", "Anonyme", 30)


# Citiations diverses
Quote("We can be do, to do. What we want to do!", "François Hollande", 30)
Quote("Yes, **WE CAN!**", "Barrack Obama", 30)
Quote("Ich bin ein Berliner!", "John F. Kennedy", 30)
Quote("Il ne faut jamais croire les citations trouvées sur Internet.", "Albert Einstein", 30)