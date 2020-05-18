Class Card:
  def_init_(self, first_name, second_name, company_name, company_position, email):
       self.first_name = first_name
       self.second_name = second_name
       self.company_name = company_name
       self.company_position = company_position
       self.email = email


        Andrzej_Witkowski = Card(first_name="Andrzej", second_name="Witkowski", company_name="Śledczy i ska", company_position="senior", email="awitkowski@sledczy.pl")
        Wojciech_Sumliński = Card(first_name="Wojciech", second_name="Sumliński", company_name="Wydawnictwo", company_position="autor", email="wsumlinski@wydawnictwo.pl")
        Paweł_Chojecki = Card(first_name="Paweł", second_name="Chojecki", company_name="IPP", company_position="pastor", email="pchojecki@ipp.pl")
        Marcin_Rola = Card(first_name="Marcin", second_name="Rola", company_name="wRealu24", company_position="redaktor", email="mrola@wrealu24.pl")
        Stanisław_Michalkiewicz = Card(first_name="Stanisław" , second_name="Michalkiewicz", company_name="Wydawnictwo 2", company_position="redaktor", email="smichalkiewicz@wydawnictwo2.pl")


 print(Card)


print(Marcin_Rola.email)

