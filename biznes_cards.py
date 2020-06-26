# import biblioteki zewnętrznej

from faker import Faker
fake = Faker()

# deklaracja klasy BaseContact


class BaseContact:
    def __init__(self, first_name, second_name, phone, email):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.email = email
        self.fname_length = len(first_name)
        self.sname_length = len(second_name)

    @classmethod
    def generate(cls, number_of_contacts):
        cards = []
        for i in range(0, int(number_of_contacts)):
            first_name = fake.first_name()
            second_name = fake.last_name()
            phone = fake.phone_number()
            email = fake.ascii_company_email()
            base_card = BaseContact(first_name, second_name, phone, email)
            cards.append(base_card)
            print(first_name, second_name, phone, email)
        return cards

# deklaracja klasy BusinessContact


class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone


def create_contacts(card_type, amount):
    cards = []
    card_string = ''
    lp = 1
    i = 0
    query = input("Provide splited by comma \n type of cards you need \n (Please choose by number 1. Base Type, 2.Business Type) \n and how many of those do you need : ").split(",")
    card_type = query[0]
    amount = query[1]
    for i in range(int(amount)):
        first_name = fake.first_name()
        second_name = fake.last_name()
        fname_length = len(first_name)
        sname_length = len(second_name)
        if int(card_type) == 1:
            card_string += (f""" {(first_name.lower() + '_' + second_name.lower())} = BaseContact(first_name="{first_name}", second_name="{second_name}", phone="{fake.phone_number()}", email="{fake.email()}", ilość liter (im/naz): "{fname_length}/{sname_length}" )""") + "\n"
        else:
            card_string += (f""" {(first_name.lower() + '_' + second_name.lower())} = BusinessContact(first_name="{first_name}", second_name="{second_name}", phone="{fake.phone_number()}", position="{fake.job()}", company="{fake.company()}", work_phone="{fake.phone_number()}", email="{fake.email()}",  ilość liter (im/naz): "{fname_length}/{sname_length}")""") + "\n"
        lp = lp + 1
    print(card_string)
    return card_type, amount


if __name__ == "__main__":

    create_contacts('', '')

    print('')
    BaseContact.generate(5)
    print('')
    print('')
    BusinessContact.generate(5)
