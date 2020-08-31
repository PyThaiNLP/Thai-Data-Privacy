# -*- coding: utf-8 -*-
from thaidp.rules import *
import re
from pythainlp.tag.named_entity import ThaiNameTagger

ner = ThaiNameTagger()
email_re = re.compile(email)
phone_number_re = re.compile(phone_number)
url_re = re.compile(url)
name_re = re.compile(name)
thai_id_card_number_re = re.compile(thai_id_card_number)

def clean_email(text:str)->str:
  return email_re.sub("[email]",text)

def clean_phone(text:str)->str:
  return phone_number_re.sub("[phone]",text)

def clean_url(text:str)->str:
  return url_re.sub("[url]",text)

def clean_thai_id_card_number(text:str)->str:
  return thai_id_card_number_re.sub("[thai_id_card_number]",text)

def clean_personname(text:str)->str:
  n = ner.get_ner(text,tag=True)
  return name_re.sub("[person_name]",n)