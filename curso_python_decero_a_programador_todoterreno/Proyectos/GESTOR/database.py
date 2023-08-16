import csv


class Customer:
    def __init__(self, dni, name, surname) -> None:
        self.dni = dni
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"({self.dni}) {self.name} {self.surname}"


class Customers:
    customers_list: list = []
    with open("customers.csv", newline="\n") as file:
        reader = csv.reader(file, delimiter=";")
        for dni, name, surname in reader:
            customer = Customer(dni, name, surname)
            customers_list.append(customer)

    @staticmethod
    def find(dni):
        for customer in Customers.customers_list:
            if customer.dni == dni:
                return customer

    @staticmethod
    def create(dni, name, surname):
        customer = Customer(dni, name, surname)
        Customers.customers_list.append(customer)
        Customers.save()
        return customer

    @staticmethod
    def update(dni, name, surname):
        for index, customer in enumerate(Customers.customers_list):
            if customer.dni == dni:
                Customers.customers_list[index].name = name
                Customers.customers_list[index].surname = surname
                Customers.save()
                return Customers.customers_list[index]

    @staticmethod
    def delete(dni):
        for index, customer in enumerate(Customers.customers_list):
            if customer.dni == dni:
                customer = Customers.customers_list.pop(index)
                Customers.save()
                return customer

    @staticmethod
    def save():
        with open("customers.csv", "w", newline="\n") as file:
            writer = csv.writer(file, delimiter=";")
            for customer in Customers.customers_list:
                writer.writerow((customer.dni, customer.name, customer.surname))