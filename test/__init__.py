# -*- coding: utf-8 -*-
"""
Code from PyThaiNLP
https://github.com/PyThaiNLP/pythainlp/blob/dev/tests/__init__.py
"""
import sys
import unittest

sys.path.append("../thaidp")

loader = unittest.TestLoader()
testSuite = loader.discover("tests")
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)