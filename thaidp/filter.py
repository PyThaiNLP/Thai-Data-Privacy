# -*- coding: utf-8 -*-
from thaidp.rules import *
import re
from functools import reduce
from pythainlp.tag.named_entity import ThaiNameTagger

ner = ThaiNameTagger()
email_re = re.compile(email)
phone_number_re = re.compile(phone_number)
url_re = re.compile(url)
name_re = re.compile(name)
thai_id_card_number_re = re.compile(thai_id_card_number)
thainer = re.compile("<[^>]*>")

def _filter(regex,text:str,tag:str,output_tag:bool=False)->str:
  list_item2 = []
  list_item = regex.findall(text)
  list_item3 = []
  for i in list_item:
    if i not in list_item2:
      list_item2.append(i)
  for i,v in enumerate(list_item):
    _i = "["+tag+"-"+str(i+1)+"]"
    text = text.replace(v,_i)
    list_item3.append(_i)
  if output_tag:
    return (text,list_item3)
  return text

def filter_email(text:str,output_tag:bool=False)->str:
  return _filter(email_re,text,"email",output_tag)

def filter_phone(text:str,output_tag:bool=False)->str:
  return _filter(phone_number_re,text,"phone",output_tag)

def filter_url(text:str,output_tag:bool=False)->str:
  return _filter(url_re,text,"url",output_tag)

def filter_thai_id_card_number(text:str,output_tag:bool=False)->str:
  return _filter(thai_id_card_number_re,text,"thai_id_card_number",output_tag)

def filter_personname(text:str,output_tag:bool=False)->str:
  n = ner.get_ner(text,tag=True)
  temp = _filter(name_re,n,"person_name",output_tag)
  if output_tag:
    return (thainer.sub("",temp[0]),temp[1])
  return thainer.sub("",temp)

def filter(text:str, steps:object=[filter_personname, filter_email, filter_phone, filter_thai_id_card_number])->str:
  return reduce(lambda x, y : y(x), steps, text)