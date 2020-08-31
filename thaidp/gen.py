# -*- coding: utf-8 -*-
import random
from pythainlp.corpus import thai_female_names, thai_male_names
from faker import Faker
fake = Faker()

list_name = list(thai_female_names()) + list(thai_male_names())

def gen_name(full_name:bool = False) -> str:
    name = random.choice(list_name)
    if full_name:
        name += " "+random.choice(list_name)
    return name

def gen_thai_phone_number(mobile:bool = True) -> str:
    num = "0"
    last_i = 7
    if mobile:
        last_i = 8
    num += str(random.randint(1, 9))
    for i in range(0,last_i):
        num += str(random.randint(0, 9))
    return num

def gen_email() -> str:
    global fake
    return fake.email()

def gen_thai_id_card_number(thai_format:bool = False) -> str:
    t = ""
    if thai_format:
        t = "-"
    output = str(random.randint(1, 8))
    output += t
    for i in range(0,4):
        output += str(random.randint(0, 9))
    output += t
    for i in range(0,5):
        output += str(random.randint(0, 9))
    output += t
    for i in range(0,2):
        output += str(random.randint(0, 9))
    output += t
    output += str(random.randint(0, 9))
    return output