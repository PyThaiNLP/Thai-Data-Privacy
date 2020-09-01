# -*- coding: utf-8 -*-
from thaidp.gen import *
from thaidp.filter import *
import random

def random_bool() -> bool:
    return random.choice([True,False])

def _replace(text_temp:str,list_index:list, list_replace:list) -> str:
    for i,v in zip(list_index,list_replace):
        text_temp = text_temp.replace(i,v)
    return text_temp


def clean_name(text:str) -> str:
    temp = filter_personname(text,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_name = [gen_name(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_index, list_name)

def clean_phone(text:str) -> str:
    temp = filter_phone(text,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_phone = [gen_thai_phone_number(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_index, list_phone)

def clean_email(text:str) -> str:
    temp = filter_email(text,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_email = [gen_email() for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_index, list_email)

def clean_thai_id_card_number(text:str) -> str:
    temp = filter_thai_id_card_number(text,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_id = [gen_thai_id_card_number(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_index, list_id)

def clean_all(text:str) -> str:
    # name
    temp = filter_personname(text,output_tag=True)
    list_all = temp[1]
    text_temp = temp[0]
    list_index = temp[1]
    list_replace = [gen_name(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    # phone
    temp = filter_phone(text_temp,output_tag=True)
    list_all += temp[1]
    text_temp = temp[0]
    list_index = temp[1]
    list_replace+=[gen_thai_phone_number(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    # email
    temp = filter_email(text_temp,output_tag=True)
    list_all += temp[1]
    list_index = temp[1]
    text_temp = temp[0]
    list_replace+= [gen_email() for i in range(0,len(list_index)) if len(list_index)!=0]
    # thai_id_card_number
    temp = filter_thai_id_card_number(text_temp,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_all += temp[1]
    list_replace+= [gen_thai_id_card_number(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_all, list_replace)