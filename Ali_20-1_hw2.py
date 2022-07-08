class Company:

     def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):

    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name,)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.salary >= self.company_bank:
            print("У компании не достаточно средств!")
        else:
            self.company_bank -= self.salary

    def person_info(self):
        print(self.first_name, self.last_name, self.salary)


Ali = Person(100000, 'DRAGON', 'Ali', 'Khamitzhanov', 7777)
Eren = Person(10000, 'Google', 'Eren', 'KROSAVA', 500000)

Ali.get_salary()
Ali.person_info()
Eren.get_salary()
Eren.person_info()

