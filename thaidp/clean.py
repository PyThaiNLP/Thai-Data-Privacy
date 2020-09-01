# -*- coding: utf-8 -*-
from thaidp.gen import *
from thaidp.filter import *
import random

def random_bool() -> bool:
    return random.choice([True,False])

def _replace(text_temp:str,list_index:list, list_replace:list) -> str:
    for i,v in zip(list_index,list_replace):
        text_temp = text_temp.replace(i,v)
    return 


def clean_name(text:str) -> str:
    temp = filter_personname(text,output_tag=True)
    text_temp = temp[0]
    list_index = temp[1]
    list_name = [gen_name(random_bool()) for i in range(0,len(list_index)) if len(list_index)!=0]
    return _replace(text_temp,list_index, list_name)