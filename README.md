# Thai-Data-Privacy
ThaiDP = Thai Data Privacy Tool For Python

Google Colab: https://colab.research.google.com/drive/1yK6LM4cVzEMabZbNUbKJ130QozHBXcnt?usp=sharing

## Features
- It's can fiter a data privacy. (email, phone, url, thai id cardnumber, person name)
- It's can fake data to replace a data privacy.

## Docs
### fiter

- filter_email(text:str,output_tag:bool=False)
- filter_phone(text:str,output_tag:bool=False)
- filter_url(text:str,output_tag:bool=False)
- filter_thai_id_card_number(text:str,output_tag:bool=False)
- filter_personname(text:str,output_tag:bool=False)
- filter(text:str)

### clean

- clean_name(text:str)
- clean_phone(text:str)
- clean_email(text:str)
- clean_thai_id_card_number(text:str)
- clean(text:str)