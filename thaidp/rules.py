# -*- coding: utf-8 -*-
email = r"[\u0E00-\u0E7Fa-zA-Z0-9_.+-]+@[\u0E00-\u0E7Fa-zA-Z0-9-]+\.[\u0E00-\u0E7Fa-zA-Z0-9-.]+"
phone_number = r"\d{10}|\d{2}\-\d{3}\-\d{4}|\d{1}\s\d{4}\s\d{4}|\d{3}\-\d{6}|\+\d{2}\s\d{4}\s\d{4}|\+\d{2}\s\d{2}\s\d{6}|\+\d{3}\s\d{4}\s\d{4}|\+\d{11}|\+\d{10}"
url = r'https?://[^\s<>"]+|www\.[^\s<>"]+' # thank https://stackoverflow.com/a/10475272/11952699
name = r'<PERSON>(.*?)</PERSON>'
thai_id_card_number = r"\d{1}[\s\-]\d{4}[\s\-]\d{5}[\s\-]\d{2}[\s\-]\d{1}|\d{13}"