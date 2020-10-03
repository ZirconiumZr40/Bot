# Import des ressources
import pytest
from quotes import random_quote

# Test du tirage d'une citation
def test_random_quote():
    # On tire une quote
    quote = random_quote()

    # On check qu'elle existe
    assert(quote.text and quote.author)