#import biblioteki zewnętrznej

from faker import Faker
fake = Faker()


#deklaracja klasy BaseContact

class BaseContact:
  def __init__(self, first_name, second_name, phone, email):
       self.first_name = first_name
       self.second_name = second_name
       self.phone = phone
       self.email = email
       
       # variables       
       self._label_length= 0
       self._contact= ''

  def __str__(self):
      return f' {self.contact} / {self.email}, ilość liter (im/naz): {self.label_length}'

  @property
  def contact(self):
      return f' Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.second_name}'
      
  @property
  def label_length(self):
     fn_count = len(self.first_name)
     sn_count = len(self.second_name)
     return fn_count, sn_count



#deklaracja klasy BusinessContact

class BusinessContact(BaseContact):
  def __init__(self, position, company, work_phone,  *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company = company
       self.work_phone = work_phone

      # variables       
       self._label_length= 0
  
  def __str__(self):
      return f'{self.contact} / {self.email} na stanowisku: {self.position} w: {self.company} tel.: {self.work_phone}, ilość liter (im/naz): {self.label_length}'

  @property
  def contact(self):
      return f' Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.second_name}'

  @property
  def label_length(self):
   fn_count = len(self.first_name)
   sn_count = len(self.second_name)
   return fn_count, sn_count



#Zmienne i ich instancje

erika_blackwell = BaseContact(first_name="Erika", second_name="Blackwell", phone="359.636.0108", email="feliciarodriguez@hotmail.com" )
george_bates = BaseContact(first_name="George", second_name="Bates", phone="736-734-4295x817", email="marilynsanchez@pope.com" )
brandon_clark = BaseContact(first_name="Brandon", second_name="Clark", phone="528.588.3188", email="nolanrose@parker-torres.com" )
katie_casey = BaseContact(first_name="Katie", second_name="Casey", phone="108.063.6397", email="rebecca74@gutierrez.com" )
daniel_chapman = BaseContact(first_name="Daniel", second_name="Chapman", phone="(793)624-0176", email="paynejennifer@hotmail.com" )
natasha_perkins = BaseContact(first_name="Natasha", second_name="Perkins", phone="(065)941-6883", email="cathyreynolds@pacheco.com" )
ronald_turner = BaseContact(first_name="Ronald", second_name="Turner", phone="488.293.2724x2570", email="christopher81@gmail.com" )
john_lyons = BaseContact(first_name="John", second_name="Lyons", phone="571.496.2375", email="pkelley@gmail.com" )
robert_rubio = BaseContact(first_name="Robert", second_name="Rubio", phone="(995)997-2850", email="juanconway@gmail.com" )
cole_franklin = BaseContact(first_name="Cole", second_name="Franklin", phone="(533)641-0259", email="owest@palmer.info" )

card = [erika_blackwell, george_bates, brandon_clark, katie_casey, daniel_chapman, natasha_perkins, ronald_turner, john_lyons, robert_rubio, cole_franklin]

print(*card, sep="\n")


#create_contacts function

def create_contacts(type, amount):
  card_string=''  
  card_sum = 0
  lp = 1
  i = 0
  query = input(" Provide splited by comma \n type of cards you need \n (Please choose by number 1. Base Type, 2.Business Type) \n and how many of those do you need : ").split(",")
  card_type= query[0]
  amount = query[1]
  for i in range(int(amount)):
    first_name = fake.first_name();
    second_name = fake.last_name();
    if int(card_type) == 1:
      card_string += (f""" {(first_name.lower() + '_' + second_name.lower())} = BaseContact(first_name="{first_name}", second_name="{second_name}", phone="{fake.phone_number()}", email="{fake.email()}" )""") + "\n"
    else:
      card_string +=  (f""" {(first_name.lower() + '_' + second_name.lower())} = BusinessContact(first_name="{first_name}", second_name="{second_name}", phone="{fake.phone_number()}", position="{fake.job()}", company="{fake.company()}", work_phone="{fake.phone_number()}", email="{fake.email()}")""") + "\n"
    lp = lp + 1

  def Convert(string): 
      card_list = list(card_string.split("\n")) 
      return card_list 
  card_list1 = (Convert(card_string)) 
  print(*card_list1, sep="\n")
  
create_contacts('','') 
