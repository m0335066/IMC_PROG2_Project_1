import kassabon_project_main as kassa
from nltk.tokenize import word_tokenize
from kassabon_project_create_db_sqalchemy import *
from kassabon_project_create_plots import *


text = kassa.extract_text_from_image(kassa.select_image())
words = word_tokenize(text)

#print(text)
#print(words)
#exit()

#creates a dictionary with categories as keys and list of tuples as values, where each tuple has item and price
dict1 = kassa.define_categories()

# words getting distributed into the dict1 for each category
kassa.assign_cat_to_item(dict1,words,text)

#supermarket = kassa.extract_supermarket(words)
#date = kassa.extract_date(text)

#populate database with data from dictionary
enter_data(dict1,kassa.extract_date(text),kassa.extract_supermarket(words))
print(dict1)
#create pie plots
create_plot_item_pie(kassa.count_items_per_cat(dict1),dict1.keys())
create_plot_price_pie(kassa.price_per_category(dict1),dict1.keys())