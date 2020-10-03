# Structure des citations
class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

# Définition des citations
quotes = [
    # Citations de VVK
    Quote("C'est moins simple", "Vincent Van Kerckhove"),
    Quote("C'est moins marant", "Vincent Van Kerckhove"),
    Quote("On va pas être copain", "Vincent Van Kerckhove"),

    # Citations de Stefano
    Quote("Le cahier de prépa est à jour", "Stefano Sanguinetti"),
    Quote("Reviens dans une heure", "Stefano Sanguinetti"),

    # Citations de Baptiste
    Quote("Tout seul on va plus vite, ensemble on va plus loin", "Baptiste Huber (proverbe africain)"),
]
