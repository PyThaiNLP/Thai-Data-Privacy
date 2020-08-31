# -*- coding: utf-8 -*-
import unittest
from thaidp.filter import *


class TestFilterPackage(unittest.TestCase):
    def test_email(self):
        self.assertEqual(
            clean_email('ผมมีอีเมล wannaphong@kkumail.com และ วรรณพงษ์@คน.ไทย'),
            'ผมมีอีเมล [email] และ [email]'
        )
    def test_phone(self):
        self.assertEqual(
            clean_phone("ผมมีเบอร์ 0888444444 ,02-123-1234,0 2345 6789 ,042-415600,042-415699,+66 2123 4567,+6621234567,+66 42 415699,+668 1123 4567,+66811234567"),
            "ผมมีเบอร์ [phone] ,[phone],[phone] ,[phone],[phone],[phone],[phone],[phone],[phone],[phone]"
        )
    def test_url(self):
        self.assertEqual(
            clean_url("https://auth.geeksforgeeks.org https://จดหมาย.คน.ไทย"),
            "[url] [url]"
        )
    def test_thai_id_card_number(self):
        self.assertEqual(
            clean_thai_id_card_number("1 2345 67890 12 3,1-2345-67890-12-3,1234567890123"),
            "[thai_id_card_number],[thai_id_card_number],[thai_id_card_number]"
        )
    def test_personname(self):
        self.assertEqual(
            clean_personname("ผมชื่อนายวรรณพงษ์ ภัททิยไพบูลย์"),
            "ผมชื่อ[person_name]"
        )