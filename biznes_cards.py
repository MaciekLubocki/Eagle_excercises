# import biblioteki zewnętrznej

from faker import Faker
fake = Faker("pl_PL")

# deklaracja klasy BaseContact


class BaseContact:
    def __init__(self, intro, first_name, second_name, phone, email):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.email = email

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    @property
    def label_length(self):
        # return len(self.full_name)
        return len(self.first_name), len(self.second_name)

    @property
    def contact_number(self):
        return self.phone

    # @property
    # def intro(self):
    #     return "Biznes cards = "

    def contact(self):
        return f"Wybieram numer {self.contact_number} i dzownię do {self.full_name}"


# deklaracja klasy BusinessContact


class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    @property
    def contact_number(self):
        return self.work_phone


def create_contacts(card_type, amount):
    cards = []
    query = input("Provide splited by comma \n type of cards you need \n (Please choose by number 1. Base Type, 2.Business Type) \n and how many of those do you need : ").split(",")
    card_type = int(query[0])
    amount = int(query[1])
    for i in range(int(amount)):
        if card_type == 1:
            cards.append(
                BaseContact(
                    intro="Business cards = ",
                    first_name=fake.first_name(),
                    second_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.email(),

                )
            )
        elif card_type == 2:
            cards.append(
                BusinessContact(
                    intro="Base cards = ",
                    first_name=fake.first_name(),
                    second_name=fake.last_name(),
                    phone=fake.phone_number(),
                    position=fake.job(),
                    company=fake.company(),
                    work_phone=fake.phone_number(),
                    email=fake.email(),

                )
            )
    return cards


if __name__ == "__main__":
    cards = create_contacts('', '')
    for card in cards:
        print(card.contact(), '. Długość im/naz: ', card.label_length)
