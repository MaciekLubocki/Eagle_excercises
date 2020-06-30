# import biblioteki zewnętrznej

from faker import Faker
fake = Faker()

# deklaracja klasy BaseContact


class BaseContact:
    def __init__(self, first_name, second_name, email, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.phone = phone

    @property
    def label_length(self):
        return len(self.first_name), len(self.second_name)

    def __str__(self):
        return f"{self.first_name} {self.second_name}, email: {self.email}, phone: {self.phone}"

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.second_name}"


card_id1 = BaseContact(first_name=fake.first_name(
), second_name=fake.last_name(), email=fake.email(), phone=fake.phone_number())

# deklaracja klasy BusinessContact


class BusinessContact(BaseContact):
    def __init__(self, position, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company

    def __str__(self):
        return f"{self.first_name} {self.second_name}, company: {self.company}, position: {self.position}, email: {self.email}, phone: {self.phone}"


def create_contacts(card_type, amount):
    if card_type == "base":
        basic = [
            BaseContact(
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()) for _ in range(amount)]
        print(*basic, sep="\n")
    if card_type == "business":
        business = [
            BusinessContact(
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                position=fake.job(),
                company=fake.company())for _ in range(amount)]
        print(*business, sep="\n")


if __name__ == "__main__":

    print("Base cards", sep="\n")
    create_contacts("base", 10)
    print('')
    print("Business cards", sep="\n")
    create_contacts("business", 10)
    print('')
    print(card_id1)
    print(card_id1.contact())
