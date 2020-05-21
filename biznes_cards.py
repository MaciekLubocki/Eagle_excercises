from faker import Faker
fake = Faker()


class BaseContact:
  def __init__(self, first_name, second_name, phone, email):
       self.first_name = first_name
       self.second_name = second_name
       self.phone = phone
       self.email = email

       self._contact = f' Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.second_name}'
       self._label_length= 0

  def __str__(self):
      return f' {self._contact} / {self.email}, ilość liter (im/naz): {self.label_length}'

  @property
  def label_length(self):
     fn_count = len(self.first_name)
     sn_count = len(self.second_name)
     return fn_count, sn_count

class BusinessContact(BaseContact):
  def __init__(self, position, company, work_phone,  *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company = company
       self.work_phone = work_phone

      # variables       
       self._contact = f' Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.second_name}'
       self._label_length= 0

  def __str__(self):
      return f'{self._contact} / {self.email} na stanowisku: {self.position} w: {self.company} tel.: {self.work_phone} ilość liter (im/naz): {self.label_length}'

  @property
  def label_length(self):
   fn_count = len(self.first_name)
   sn_count = len(self.second_name)
   return fn_count, sn_count


def cards_creator(amount, base_amount, business_amount):
  card_list=''  
  card_sum = 0
  lp = 1
  i = 0
  amount = str.split(input("Provide splited by comma how much cards do you need to create (1.Base_type, 2.Business_type): "))
  base_amount= amount[0]
  business_amount = amount[1]
  if int(base_amount) != 0 and int(base_amount) > 0:
    type_card = "BaseCard"
    for i in range(int(base_amount)):
      card_list += (f""" {lp} = BaseContact(first_name={fake.first_name()}, second_name={fake.last_name()}, phone={fake.phone_number()}, email={fake.email()} )""") + "\n"
      lp = lp + 1
  if int(business_amount) != 0 and int(business_amount) > 0:
    for i in range(int(business_amount)):
      card_list +=  (f""" {lp} = BusinessContact(first_name={fake.first_name()}, second_name={fake.last_name()}, position={fake.job()},  company={fake.company()},  work_phone={fake.phone_number()})""") + "\n"
      lp = lp + 1
      card_sum = (int(base_amount) + int(business_amount))  
  print(card_list)
  
  cards_creator.contact_list = [(item + 1) for item  in range(card_sum)]
  print(cards_creator.contact_list)
  
cards_creator('','','') 

# base_contact = str(1)
# for person in cards_creator.contact_list:
#    if person == cards_creator.card_list:
#     base_contact += base_contact + type(person)

base_contact = [item for item in cards_creator.contact_list if type(item) == BaseContact]
business_contact = [item for item in cards_creator.contact_list if type(item) == BusinessContact]

print(*base_contact, sep="\n")
print('')
print('')
print(*business_contact, sep="\n")

