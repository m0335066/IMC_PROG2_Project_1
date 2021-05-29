import pytest
import builtins
import mock
import re

def check1():
    x = input('enter a letter')
    return x

def test_check1():
    with mock.patch.object(builtins, 'input' , lambda x: '19'):
        assert check1() == '19'


#extract a date with regex and save in variable date
def extract_date(text_receipt):
    date_pattern='\d\d\.\d\d\.\d\d\d\d'
    date=re.findall(date_pattern,text_receipt)
    return date[0]


def test_extract_date():
    assert extract_date('16.03.2021 text text text 16.03.2021') == '16.03.2021'
    assert extract_date('bla bla bla 16.03.2021') == '16.03.2021'




