# -*- coding: utf-8 -*-
import unittest
from thaidp.filter import *


class TestFilterPackage(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(
            filter('ผมมีอีเมล wannaphong@kkumail.com และ วรรณพงษ์@คน.ไทย'),
            'ผมมีอีเมล [email-1] และ [email-2]'
        )
    def test_email(self):
        self.assertEqual(
            filter_email('ผมมีอีเมล wannaphong@kkumail.com และ วรรณพงษ์@คน.ไทย'),
            'ผมมีอีเมล [email-1] และ [email-2]'
        )
    def test_phone(self):
        self.assertEqual(
            filter_phone("ผมมีเบอร์ 0888444444 ,02-123-1234,0 2345 6789 ,042-415600,042-415699,+66 2123 4567,+6621234567,+66 42 415699,+668 1123 4567,+66811234567"),
            "ผมมีเบอร์ [phone-1] ,[phone-2],[phone-3] ,[phone-4],[phone-5],[phone-6],[phone-7],[phone-8],[phone-9],[phone-10]"
        )
    def test_url(self):
        self.assertEqual(
            filter_url("https://auth.geeksforgeeks.org https://จดหมาย.คน.ไทย"),
            "[url-1] [url-2]"
        )
    def test_thai_id_card_number(self):
        self.assertEqual(
            filter_thai_id_card_number("1 2345 67890 12 3,1-2345-67890-12-3,1234567890123"),
            "[thai_id_card_number-1],[thai_id_card_number-2],[thai_id_card_number-3]"
        )
    def test_personname(self):
        self.assertEqual(
            filter_personname("ผมชื่อนายวรรณพงษ์ ภัททิยไพบูลย์"),
            "ผมชื่อ[person_name-1]"
        )