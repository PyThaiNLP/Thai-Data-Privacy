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
thainer = re.compile("<[^>]*>")

def _filter(regex:re.Pattern,text:str,tag:str)->str:
  list_item2 = []
  list_item = regex.findall(text)
  for i in list_item:
    if i not in list_item2:
      list_item2.append(i)
  for i,v in enumerate(list_item):
    text = text.replace(v,"["+tag+"-"+str(i+1)+"]")
  return text

def filter_email(text:str)->str:
  return _filter(email_re,text,"email")

def filter_phone(text:str)->str:
  return _filter(phone_number_re,text,"phone")

def filter_url(text:str)->str:
  return _filter(url_re,text,"url")

def filter_thai_id_card_number(text:str)->str:
  return _filter(thai_id_card_number_re,text,"thai_id_card_number")

def filter_personname(text:str)->str:
  n = ner.get_ner(text,tag=True)
  return thainer.sub("",_filter(name_re,n,"person_name"))

def filter_all(text:str)->str:
  text = filter_thai_id_card_number(filter_url(filter_phone(filter_email(filter_personname(text)))))
  return text