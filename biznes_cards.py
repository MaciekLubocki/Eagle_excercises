class Card:
  def __init__(self, first_name, second_name, phone, position, company, work_phone, email):
       self.first_name = first_name
       self.second_name = second_name
       self.phone = phone
       self.position = position
       self.company = company
       self.work_phone = work_phone
       self.email = email
       
class BaseContact(Card):
  def __init__(self, first_name, second_name, phone, email):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class BiznesContact(Card):
  def __init__(self, position, company, work_phone):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

    # variables       

       self._contact = "Kontaktuję się z …"
       self._letters_count= 0


  @property
  def letters_count(self):
   fn_count = len(self.first_name)
   sn_count = len(self.second_name)
   
   return fn_count, sn_count

  def __str__(self):
      return f'{self._contact} {self.first_name} {self.second_name} {self.email} {self.letters_count}'

andrzej_witkowski = Card(first_name="Andrzej", second_name="Witkowski", phone="123-454-654", position="police officer", company="Dark sides", work_phone="111-555-888", email="awitkowski@ggmail.pl")
wojciech_sumliński = Card(first_name="Wojciech", second_name="Sumliński", phone="133-554-634", position="journalist", company="Real Truth", work_phone="222-444-", email="wsumlinski@op.pl")
paweł_chojecki = Card(first_name="Paweł", second_name="Chojecki", phone="153-464-634", position="office worker", company="Witness of Smith", work_phone="", email="pchojecki@ipex.pl")
marcin_rola = Card(first_name="Marcin", second_name="Rola", phone="323-424-594", position="office assistant", company="Tower Office", work_phone="", email="mrola@waw.pl")
stanisław_michalkiewicz = Card(first_name="Stanisław" , second_name="Michalkiewicz", phone="123-454-654", position="author", company="self employed", work_phone="", email="smichalkiewicz@edu.pl")

Card = [andrzej_witkowski, wojciech_sumliński, paweł_chojecki, marcin_rola, stanisław_michalkiewicz]
by_first_name = sorted(Card, key=lambda Card: Card.first_name)
by_second_name = sorted(Card, key=lambda Card: Card.second_name)
by_email = sorted(Card, key=lambda Card: Card.email)

# print('By first name')
# print(*by_first_name, sep='\n')
# print('By second name')
# print(*by_second_name, sep='\n')
# print('By email')
print(*by_email, sep='\n')

