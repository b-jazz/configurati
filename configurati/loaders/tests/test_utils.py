import os
import unittest

from configurati.loaders.utils import *


class SubstituteTest(unittest.TestCase):

  def test_no_substitution(self):
    assert substitute("abc") == "abc"

  def test_substitution(self):
    assert substitute("`1`2") == "12"

  def test_substitution_with_semicolon(self):
    assert substitute("`import os; os.getcwd()`") == os.getcwd()

  def test_substitution_with_newlines(self):
    assert substitute("`import os\nos.getcwd()`") == os.getcwd()
