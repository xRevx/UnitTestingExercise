class Employee:
    def __init__(self, name: str, age: int, salary: int, email: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = email

    @property
    def forename(self):
        return self.name.split(" ")[0]

    @property
    def surname(self):
        name = self.name.split(" ")[-1]
        return name if name != self.forename else None

    def birthday_party(self):
        self.age += 1

    def raise_salary(self, amount: int):
        if amount < 1:
            raise ValueError('can not lower salary')
        else:
            self.salary *= amount  # intentional to see fails

    def is_valid_email(self):
        # has to have @
        if not self.email.__contains__('@'):
            raise ValueError('email does not contain @')
        else:
            # has to have at least 6 characters before @
            name = self.email.split("@")[0]
            if len(name) < 6:
                raise ValueError('email too short')

        return True