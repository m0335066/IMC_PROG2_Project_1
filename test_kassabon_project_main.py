import pytest
import builtins
import mock
import re
from kassabon_project_main import *


#def check1():
#    x = input('enter a letter')
#    return x

#def test_check1():
#    with mock.patch.object(builtins, 'input' , lambda x: '19'):
#        assert check1() == '19'


def test_extract_date():
    #what is multiple dates occur
    assert extract_date('16.03.2021 text text text 16.03.2021') == '16.03.2021'
    #if one date occurs
    assert extract_date('bla bla bla 16.03.2021') == '16.03.2021'
    #no date occurs
    assert extract_date('bla bla bla') == '01.01.2001'

def test_extract_supermarket():
    #word matches exactely
    assert extract_supermarket(['SPAR']) == 'SPAR'
    #not case sensitive
    assert extract_supermarket(['SpAr']) == 'SPAR'
    #no supermarket found
    assert extract_supermarket([]) == 'unknown'
    #wrong input format
    assert extract_supermarket('SPAR') == 'unknown'

def test_confirm_prices():
    item = 'Bananen'
    text_ = '''Ja! Bio Bananen 8 0.79

regionale Melanzani 8 1.59

Bio Grahanwecker] 8 1.54
2x 3,89'''
    text2_ = '''Ja! Bio Bananen 8 0,79

regionale Melanzani 8 1.59

Bio Grahanwecker] 8 1.54
2x 3,89'''
    text3_ = '''Ja! Bio Bananen 8 

regionale Melanzani 8 1.59

Bio Grahanwecker] 8 1.54
2x 3,89'''
    assert confirm_prices(item,text_) == 0.79
    assert confirm_prices(item,text2_) == 0.79
    #assert confirm_prices(item,text3_) != 0.79

def test_assign_cat_to_item():
    dict1 = {'sweets':[]}
    dict2 = {'sweets':[],'other':[]}
    words =['chocolate']
    text = 'Milka chocolate X 1.99\\n'
    #checks if the items gets assigned in a dictionary
    with mock.patch.object(builtins, 'input', lambda x: 'sweets'):
        assert assign_cat_to_item(dict1,words,text) == {'sweets':[('chocolate',1.99)]}

    # checks if the items gets assigned at the right place in a dictionary when 2 categories exists
    with mock.patch.object(builtins, 'input', lambda x: 'other'):
        assert assign_cat_to_item(dict2,words,text) == {'sweets':[],'other':[('chocolate',1.99)]}

def test_count_items_per_cat():
    dict1 = {'sweets':[('biskuits',0.99),('chocolate',0.99),('fizzers',0.99)],'other':[('toothpaste',1.99)]}
    dict2 = {}
    dict3 = {'sweets':[],'other':[('toothpaste',1.99)]}
    #checks if categories are counted properly
    assert count_items_per_cat(dict1) == [3,1]
    #checks if empty list is returned when empty dictionary is present
    assert count_items_per_cat(dict2) == []
    #checks if categories are counted properly if one category is empty
    assert count_items_per_cat(dict3) == [0, 1]

def test_price_per_categor():
    dict1 = {'sweets': [('biskuits', 1), ('chocolate', 2), ('fizzers', 3)], 'other': [('toothpaste', 1.99)]}
    assert len(price_per_category(dict1)) == 2


