#from kassabon_project_create_db_sqalchemy import *
#from kassabon_project_create_plots import *
from PIL import Image
import re
from nltk.tokenize import word_tokenize
import pytesseract as tess
import os

# list of all possible supermarkets for this project
supermarkets = ['BILLA', 'SPAR', 'EUROSPAR', 'INTERSPAR', 'HOFER', 'PENNI', 'LIDL', 'MERKUR']
# list of words that can be discarded right away
out = ['Rabatt', 'EUR', 'SUMME', 'MAESTRO', 'WIEN', 'TELEFON', 'KARTE', []]


#starts the extraction machine
tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#checks if user input is available and returns the 4 digit code of the file
def select_image():
    while True:
        png_code = input ('Please enter 4 digit code for the receipt: ')
        if 'bon_'+png_code+'.png' in os.listdir():
            return png_code
        else:
            print('sorry the code you have enter is incorrect, please try again')
            continue

#extracts the text from the previously selected png file
def extract_text_from_image(png_code):
    img=Image.open('bon_'+png_code+'.png')
    #text = tess.image_to_string(img)
    return tess.image_to_string(img)

#user enters categories to popoulate a dictionary with categories as keys,
#when user is done entering categories, press 'x' to see a selection of categories
#and confirm with 'Y' or keep updating with 'N'
def define_categories():
    # create an empty list for categories
    global cat_labels
    cat_labels = []
    while True:
        cat = input('Please enter category name, \nEnter \'x\' when ready: ')
        if cat != 'x':
            cat_labels.append(cat) #populates th elist cat_labels
        else:
            print('you have selected the following categories: ')
            print(cat_labels)
            x = input ('confirm choice with \'Y\', keep updating with \'N\'')
            if x.capitalize() == 'Y':
                # return a dictionary with categories (taken from the list cat_labels) as keys
                return {k: [] for k in cat_labels}
            #keep updating when pressing 'N'
            elif x.capitalize() == 'N':
                continue

#extract a date with regex and save in variable date
def extract_date(text_receipt):
    date_pattern='\d\d\.\d\d\.\d\d\d\d'
    date=re.findall(date_pattern,text_receipt)
    try:
        return date[0]
    except IndexError:
        print('sorry no date found \'01.01.2001\' will be entered')
        return '01.01.2001'

#identify the type of super market supermarket:
def extract_supermarket(words):
    for word in words:
        if word.upper() not in supermarkets:
            pass
        else:
            return word.upper()
    print('sorry supermarket not found, \'unknown\' will be entered')
    return 'unknown'

#check the price of an individual item
def confirm_prices(item,text_):
    pattern = item + '.*[^n]'
    price_pattern = '\d+[\.\,]\d\d'
    line = re.findall(pattern, text_)
    p = re.findall(price_pattern,line[0])
    if len(p) >0:
        try:
            digi_list = p[0].split('.')
            price = int(digi_list[0]) + (int(digi_list[1])/100)
            return price
        except ValueError:
            digi_list = p[0].split(',')
            price = int(digi_list[0])+(int(digi_list[1])/100)
            return price
    else:
        while True:
            p = input(f'no price found for \'{item}\' please enter price manually dd.dd or exit with \'x\': ')
            if p.upper() == 'X':
                continue
            else:
                try:
                    p_split = p.split('.')
                    price = int(p_split[0]) + (int(p_split[1]) / 100)
                    return price
                except ValueError:
                    continue
                except IndexError:
                    continue

#assignes categories and prices to items and stores them in a dictionary
def assign_cat_to_item(dict_,words,text):
    for w in words:
        #is statement does some pre procsssing of words not to be proposed as items
        #if they are numbers, out of the 'out'-list or out of the supermarkets list
        #words have to be longer then 3 characters to be proposed
        if len(w) > 3 and w.isalpha() and w not in out and w.upper() not in supermarkets:
            print(w) #prints the proposed item
            print(dict_.keys()) #prints the categories to remember the user which ones were entered
            while True: #while loop in case invalid userinput for category
                x = input(f"Select a category for {w} from: ")
                if x in dict_.keys():  # if user input is available in the categories list break
                    break
                elif x == "":  # if the enter is pressed break the loop
                    break
                else:
                    print("Wrong category given!")  # if wrong category is put, ask for new input
                    continue
            if x == "":
                pass  # if enter was pressed keep iterating through the list of words
            else:  # otherwise append the word to the dictionary
                p = confirm_prices(w,text) #check the price and add to to the dictionary
                dict_[x].append((w,p))

    return dict_

def count_items_per_cat(dict_):
    cat_count = []
    for listi in dict_.values():
        cat_count.append(len(listi))
    return cat_count

def price_per_category(dict_):
    cat_sum=[]
    for listi in dict_.values():
        for i in range (1,len(listi)):
            sum_ = listi[i][1] + listi[i-1][1]
        try:
            cat_sum.append(sum_)
        except UnboundLocalError: #excpet statement in case one of the catgeories is unused and sum_ is not insstanciated
            cat_sum.append(0)
    return cat_sum



