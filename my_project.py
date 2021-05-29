import kassabon_project_main as kassa
from nltk.tokenize import word_tokenize
from kassabon_project_create_db_sqalchemy import *
from kassabon_project_create_plots import *


text = kassa.extract_text_from_image(kassa.select_image())
words = word_tokenize(text)

dict1 = kassa.define_categories()
kassa.assign_cat_to_item(dict1,words,text)

supermarket = kassa.extract_supermarket(words)
date = kassa.extract_date(text)

#populate database
enter_data(dict1,date,supermarket)
#create pie plots
create_plot_item_pie(kassa.count_items_per_cat(dict1),dict1.keys())
create_plot_price_pie(kassa.price_per_category(dict1),dict1.keys())