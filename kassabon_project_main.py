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
# words getting assigned to the dict1 for each category

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


#text = extract_text_from_image(select_image())
#extract words with nltk
#words = word_tokenize(text)

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
def extract_supermarket(text_receipt):
    for i in text_receipt:
        if i not in supermarkets:
            pass
        else:
            return i
    print('sorry supermarket not found, \'unknown\' will be entered')
    return 'unknown'

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
            p = input(f'no price found for {item} please enter price manually dd.dd: ')
            try:
                p_split = p.split('.')
                price = int(p_split[0]) + (int(p_split[1]) / 100)
                return price
            except ValueError:
                continue
            except IndexError:
                continue

def assign_cat_to_item(dict_,words,text):
    for w in words:
        if len(w) > 3 and w.isalpha() and w not in out and w.capitalize() not in supermarkets:
            print(w)
            print(dict_.keys())
            while True:
                x = input(f"Select a category for {w} from: ")
                if x in dict_.keys():  # if the category exists leave the while loop
                    break
                elif x == "":  # if the enter is pressed break
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
    for list in dict_.values():
        cat_count.append(len(list))
    return cat_count

def price_per_category(dict_):
    cat_sum=[]
    for list in dict_.values():
        for i in range (1,len(list)):
            sum = list[i][1] + list[i-1][1]
        cat_sum.append(sum)
    return cat_sum


#supermarket = extract_supermarket(words)
#date = extract_date(text)
#print(date, supermarket)
#dict1 = define_categories()
#assign_cat_to_item(dict1,words,text)
#print(dict1)
#print(price_per_category(dict1))

#populate database
#enter_data(dict1,date,supermarket)
#create pie plot
#create_plot_item_pie(count_items_per_cat(dict1),cat_labels)
#create_plot_price_pie(price_per_category(dict1),cat_labels)
