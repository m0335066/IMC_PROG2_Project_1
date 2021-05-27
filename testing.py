import pytest
from kassabon_project_main import *


#creates a dictionary with categories as values
def test_define_categories():
    pass
    #invalid user input for a category

#extracts a pattern (date) from a string
def test_extract_date(text_receipt):
    pass
    #can happen no date is found
    #dot might be mistaken as a comma, instead of 01.01.2021 tesseract might see 01,01.2021


#sxtracts supermarket name from a string
def test_extract_supermarket(text_receipt):
    pass
    #no name found from the list of supermarkets
    #string doesnt match with capitalized letters
    #tesseract might misinterpret single letters and then supermarket is not found, maybe add an option to insert manually

#fills the dictionary values to the according key
def test_assign_cat_to_item(text_receipt):
    pass


#counts the length of the list in the dictionaries values
def test_count_items_per_cat(dict_):
    pass

