import re
import os
import platform


def clean_screen():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")


def read_text(min_length=0, max_length=100, msg=None):
    print(msg) if msg else None
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text
        print(
            f"Error! The permitted length is (min){min_length} chars y (max){max_length} chars."
        )


def validate_dni(dni, customers_list):
    if not re.match("\d{8}[A-Z]$", dni):
        print("Incorrect DNI, must comply with the format.")
        return False
    for customer in customers_list:
        if customer.dni == dni:
            print("DNI used by another customer.")
            return False
    return True