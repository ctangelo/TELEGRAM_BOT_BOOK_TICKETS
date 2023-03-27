import sqlite3 as sq
from dispatcher import bot
from aiogram import types
from handlers.admin import ID
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from keyboard.admin_kb import order_visa_btn, order_exchange_btn, order_tour_btn, order_charter_btn, order_hotel_btn

def sql_start():
    global base, cur
    base = sq.connect('clients.db')
    cur = base.cursor()
    if base:
        print("Database connected successfully")
    base.execute('CREATE TABLE IF NOT EXISTS visa(user_id INTEGER, visa TEXT, date TEXT, location TEXT, id TEXT, photo TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS exchange(user_id INTEGER, currency TEXT, city TEXT, amount INTEGER, aprove TEXT, delivery TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS tour(user_id INTEGER, departure TEXT, resort TEXT, date_departure TEXT, amount_of_nights INTEGER, number_of_persons INTEGER, children TEXT, number_of_childrens INTEGER, age_children TEXT, hotel TEXT, hotel_name TEXT, stars TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS charter(user_id INTEGER, departure TEXT, arrival TEXT, date_departure TEXT, one_two_way TEXT, date_back TEXT, number_of_persons INTEGER, children TEXT, number_of_childrens INTEGER)')
    base.execute('CREATE TABLE IF NOT EXISTS hotel(user_id INTEGER, resort TEXT, hotel TEXT, hotel_name TEXT, stars TEXT, arrival_day TEXT, amount_of_nights INTEGER, amount_of_person INTEGER, children TEXT, number_of_childrens INTEGER, age_children TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS currency(rub INTEGER, kzt INTEGER, kgs INTEGER, uzs INTEGER, usdt INTEGER)')
    base.commit()



# ____________EVISA_____________________________


async def add_visa(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO visa VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    await bot.send_message(ID, 'У вас новая заявка на оформление евизы', reply_markup=order_visa_btn)
    


async def all_visa():
    with base:
        cur.execute('SELECT * FROM visa')
        return cur.fetchall()
    
async def one_visa(user_id, date):
    with base:
        cur.execute(f'SELECT * FROM visa WHERE (user_id = ?) AND (date = ?)', (user_id, date))
        return cur.fetchone()


async def delete_visa(user_id, date):
    with base:
        cur.execute('DELETE FROM visa WHERE (user_id=?) AND (date = ?)', (user_id, date))


def count_visa():
    with base:
        cur.execute('SELECT COUNT(user_id) from visa')
        return cur.fetchone()
    
# ____________exchange_____________________________

def count_exchange():
    with base:
        cur.execute('SELECT COUNT(user_id) from exchange')
        return cur.fetchone()[0]


async def add_exchange(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO exchange VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    await bot.send_message(ID, 'У вас новая заявка на обмен валюты', reply_markup=order_exchange_btn)


async def see_exchange():
    with base:
        cur.execute('SELECT * FROM exchange')
        return cur.fetchall()
    

async def one_exchange(user_id, amount):
    with base:
        cur.execute(f'SELECT * FROM exchange WHERE (user_id = ?) AND (amount = ?)', (user_id, amount))
        return cur.fetchone()


async def delete_exchange(user_id, amount):
    with base:
        cur.execute('DELETE FROM exchange WHERE (user_id = ?) AND (amount = ?)', (user_id, amount))



# ____________tour_____________________________

def count_tour():
    with base:
        cur.execute('SELECT COUNT(user_id) from tour')
        return cur.fetchone()[0]

async def add_tour(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO tour VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    await bot.send_message(ID, 'У вас новая заявка на бронирование тура', reply_markup=order_tour_btn)

async def see_tour():
    with base:
        cur.execute('SELECT * FROM tour')
        return cur.fetchall()
    

async def one_tour(user_id, date_departure):
    with base:
        cur.execute(f'SELECT * FROM tour WHERE (user_id = ?) AND (date_departure = ?)', (user_id, date_departure))
        return cur.fetchone()


async def delete_tour(user_id, date_departure):
    with base:
        cur.execute('DELETE FROM tour WHERE (user_id = ?) AND (date_departure = ?)', (user_id, date_departure))

# ____________charter_____________________________


def count_charter():
    with base:
        cur.execute('SELECT COUNT(user_id) from charter')
        return cur.fetchone()[0]
    

async def add_charter(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO charter VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    await bot.send_message(ID, 'У вас новая заявка на бронирования чартера', reply_markup=order_charter_btn)

async def see_charter():
    with base:
        cur.execute('SELECT * FROM charter')
        return cur.fetchall()
    

async def one_charter(user_id, date_departure):
    with base:
        cur.execute(f'SELECT * FROM charter WHERE (user_id = ?) AND (date_departure = ?)', (user_id, date_departure))
        return cur.fetchone()


async def delete_charter(user_id, date_departure):
    with base:
        cur.execute('DELETE FROM charter WHERE (user_id = ?) AND (date_departure = ?)', (user_id, date_departure))


# ____________hotel_____________________________

def count_hotel():
    with base:
        cur.execute('SELECT COUNT(user_id) from hotel')
        return cur.fetchone()[0]


async def add_hotel(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO hotel VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    await bot.send_message(ID, 'У вас новая заявка на бронирование отеля', reply_markup=order_hotel_btn)


async def see_hotel():
    with base:
        cur.execute('SELECT * FROM hotel')
        return cur.fetchall()


async def one_hotel(user_id, arrival_day):
    with base:
        cur.execute(f'SELECT * FROM hotel WHERE (user_id = ?) AND (arrival_day = ?)', (user_id, arrival_day))
        return cur.fetchone()


async def delete_hotel(user_id, arrival_day):
    with base:
        cur.execute('DELETE FROM hotel WHERE (user_id = ?) AND (arrival_day = ?)', (user_id, arrival_day))


# ____________currency_____________________________



async def add_currency(state):
    async with state.proxy() as data:
        cur.execute('DELETE FROM currency')
        cur.execute('INSERT INTO currency VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

def check_currency(currency):
    with base:
        cur.execute(f'SELECT {currency} FROM currency')
        
        return cur.fetchone()[0]
    

