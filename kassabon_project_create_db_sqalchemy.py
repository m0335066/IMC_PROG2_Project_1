# -*- coding: utf-8 -*-
from sqlalchemy import update, create_engine, Table, Column, Integer, String, Date, MetaData, Float, select, ForeignKey
import uuid
from datetime import datetime
#######################################################################DATABASE
engine = create_engine ('sqlite:///example1.db', echo = True)
meta = MetaData()

#creating the table
master_table = Table(
    'Einkauf', meta,
    Column('id', String, primary_key = True),
    Column('date', Date), #should be DATE instead
    Column('supermarket', String),
    Column('item', String),
    Column('price', Float),
    Column('category', String))

meta.create_all(engine)

#adding data to the table
def enter_data(dicti,date,supermarket):
    y = int(date[-4:])
    m = int(date[3:5])
    d = int(date[:2])
    for k,v in dicti.items():
        for item in v:
            id_ = str(uuid.uuid1())
            connection = engine.connect()
            insert_1 = master_table.insert().values(id = id_, date = datetime(y,m,d), supermarket = supermarket, item = item[0], price = item[1], category = k)
            print(insert_1)
            connection.execute(insert_1)
    connection.close()
