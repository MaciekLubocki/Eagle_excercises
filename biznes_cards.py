class Card:
  def __init__(self, first_name, second_name, email):
       self.first_name = first_name
       self.second_name = second_name
       self.email = email


# andrzej_witkowski = Card(first_name="Andrzej", second_name="Witkowski", company_name="Śledczy i ska", company_position="senior", email="awitkowski@sledczy.pl")
# wojciech_sumliński = Card(first_name="Wojciech", second_name="Sumliński", company_name="Wydawnictwo", company_position="autor", email="wsumlinski@wydawnictwo.pl")
# paweł_chojecki = Card(first_name="Paweł", second_name="Chojecki", company_name="IPP", company_position="pastor", email="pchojecki@ipp.pl")
# marcin_rola = Card(first_name="Marcin", second_name="Rola", company_name="wRealu24", company_position="redaktor", email="mrola@wrealu24.pl")
# stanisław_michalkiewicz = Card(first_name="Stanisław" , second_name="Michalkiewicz", company_name="Wydawnictwo 2", company_position="redaktor", email="smichalkiewicz@wydawnictwo2.pl")


andrzej_witkowski = Card(first_name="Andrzej", second_name="Witkowski", email="awitkowski@sledczy.pl")
wojciech_sumliński = Card(first_name="Wojciech", second_name="Sumliński", email="wsumlinski@wydawnictwo.pl")
paweł_chojecki = Card(first_name="Paweł", second_name="Chojecki", email="pchojecki@ipp.pl")
marcin_rola = Card(first_name="Marcin", second_name="Rola", email="mrola@wrealu24.pl")
stanisław_michalkiewicz = Card(first_name="Stanisław" , second_name="Michalkiewicz", email="smichalkiewicz@wydawnictwo2.pl")

Card = [andrzej_witkowski, wojciech_sumliński, paweł_chojecki, marcin_rola, stanisław_michalkiewicz]
by_first_name = sorted(Card, key=lambda Card: Card.first_name)
by_second_name = sorted(Card, key=lambda Card: Card.second_name)
by_email = sorted(Card, key=lambda Card: Card.email)


def __str__(self):
    return f'{self.first_name}. {self.second_name} {self.email}'
    print(andrzej_witkowski)

