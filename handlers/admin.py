from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from dispatcher import bot, dp
from keyboard.admin_kb import currency_btn, gen_inline_visa_orders, gen_inline_charter_orders, gen_inline_hotel_orders, gen_inline_tour_orders, \
        gen_inline_exchange_orders, gen_inline_main_menu, gen_inline_consultant_orders
from database import sqlite_db


ID = 'ADMIN'


# @dp.callback_query_handler(commands=['admin_menu'])
async def admin_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Здравствуйте, вот список заявок', reply_markup=gen_inline_main_menu())



# @dp.callback_query_handler(commands='consultant_order')
async def consultant_order(callback: types.CallbackQuery):
    await callback.message.delete()
    data = await sqlite_db.all_consultant()
    await callback.message.answer('Заявки на консультацию', reply_markup=gen_inline_consultant_orders(data))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('one_consultant|'))
async def consultant_one_order(callback: types.CallbackQuery):
    await callback.message.delete()
    order = await sqlite_db.one_consultant(callback.data.split('|')[1])
    chat_id = callback.data.split('|')[1]
    button_url = f'tg://user?id={chat_id}'
    markup = InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='написать пользователю', url=button_url))
    markup.add(InlineKeyboardButton(text='Удалить заявку', callback_data=f'delete|consultant|{order[0]}'))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='consultant_order'))
    await bot.send_message(ID, f'Заявка на консультацию {order[0]}', reply_markup=markup)


# @dp.message_handler(commands='evisa_order')
async def evisa_order(callback: types.CallbackQuery):
    await callback.message.delete()
    data = await sqlite_db.all_visa()
    await callback.message.answer('Заявки на оформление ЕВИЗЫ:', reply_markup=gen_inline_visa_orders(data))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('visa|'))
async def evisa_one_order(callback: types.CallbackQuery):
    await callback.message.delete()
    order = await sqlite_db.one_visa(callback.data.split('|')[1], callback.data.split('|')[2])
    chat_id = callback.data.split('|')[1]
    button_url = f'tg://user?id={chat_id}'
    markup = InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='написать пользователю', url=button_url))
    markup.add(InlineKeyboardButton(text='Удалить заявку', callback_data=f'delete|evisa|{order[0]}|{order[1]}'))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='evisa_order'))
    media = types.MediaGroup()
    media.attach_photo(order[20])
    media.attach_photo(order[21])
    await bot.send_media_group(ID, media=media)
    await bot.send_message(ID, f'Заявка на оформление E-Visa\n{order[1]} {order[2]}\n'
                                       f'Имя: {order[3]}\nГражданство: {order[4]}\nМесто рождения: {order[5]}\nНомер заграничного паспорта: {order[6]}\n'
                                       f'Религия: {order[7]}\nДругой паспорта: {order[8]}\nДвойное гражданство: {order[9]}\nДомашний адрес: {order[10]}\n'
                                       f'Номер телефона: {order[11]}\nМесто работы и Должность: {order[12]}\n'
                                       f'Адрес во Вьетнаме: {order[13]}\nБыли ли во Вьетнаме за последний год: {order[14]} - {order[15]}\n'
                                       f'Бюджет: {order[16]}\nСтраховка: {order[17]}\nДата и место пересечения границы: {order[18]} {order[19]}', reply_markup=markup)
   

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('delete|'))
async def delete_order(callback: types.CallbackQuery):
    # await callback.message.delete()
    data = callback.data.split('|')
    if data[1] == 'evisa':
        await sqlite_db.delete_visa(data[2], data[3])
        await evisa_order(callback)
    
    elif data[1] == 'charter':
        await sqlite_db.delete_charter(data[2], data[3])
        await charter_order(callback)

    elif data[1] == 'tour':
        await sqlite_db.delete_tour(data[2], data[3])
        await tour_order(callback)

    elif data[1] == 'hotel':
        await sqlite_db.delete_hotel(data[2], data[3])
        await hotel_order(callback)

    elif data[1] == 'consultant':
        await sqlite_db.delete_consultant(data[2])
        await consultant_order(callback)
    

# @dp.callback_query_handler(text='charter_order')
async def charter_order(callback: types.CallbackQuery):
    await callback.message.delete()
    data = await sqlite_db.see_charter()
    await callback.message.answer('Заявки на Чартеры:', reply_markup=gen_inline_charter_orders(data))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('one_charter|'))
async def charter_one_order(callback: types.CallbackQuery):
    await callback.message.delete()
    order = await sqlite_db.one_charter(callback.data.split('|')[1], callback.data.split('|')[2])
    chat_id = callback.data.split('|')[1]
    button_url = f'tg://user?id={chat_id}'
    markup = InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='написать пользователю', url=button_url))
    markup.add(InlineKeyboardButton(text='Удалить заявку', callback_data=f'delete|charter|{order[0]}|{order[3]}'))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='charter_order'))
    if order[4] == 'в одну':
        await callback.message.answer(f'Чартер\n {order[1]} - {order[2]} {order[4]} сторону\nДата вылета:{order[3]}\n'
                                      f'Кол-во человек:{order[6]}\nДети:{order[7]} ({order[8]})', reply_markup=markup)
    else:
        await callback.message.answer(f'Чартер\n {order[1]} - {order[2]} - {order[1]}\nДата:{order[3]} - {order[5]}\n'
                                      f'Кол-во человек:{order[6]}\nДети:{order[7]} ({order[8]})', reply_markup=markup)


# @dp.callback_query_handler(text='hotel_order')
async def hotel_order(callback: types.CallbackQuery):
    await callback.message.delete()
    data = await sqlite_db.see_hotel()
    await callback.message.answer('Заявки на бронирование отелей:', reply_markup=gen_inline_hotel_orders(data))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('one_hotel|'))
async def hotel_one_order(callback: types.CallbackQuery):
    await callback.message.delete()
    order = await sqlite_db.one_hotel(callback.data.split('|')[1], callback.data.split('|')[2])
    chat_id = callback.data.split('|')[1]
    button_url = f'tg://user?id={chat_id}'
    markup = InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='написать пользователю', url=button_url))
    markup.add(InlineKeyboardButton(text='Удалить заявку', callback_data=f'delete|hotel|{order[0]}|{order[5]}'))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='hotel_order'))
    
    await callback.message.answer(f'Отель\nКурорт: {order[1]}\nНазвание: {order[2]} ({order[4]} звезды)\nДата:{order[5]} на {order[6]} ночей\n'
                                  f'Кол-во человек:{order[7]}\nДети:{order[9]} ({order[10]})', reply_markup=markup)


# @dp.callback_query_handler(text='tour_order')
async def tour_order(callback: types.CallbackQuery):
    await callback.message.delete()
    data = await sqlite_db.see_tour()
    await callback.message.answer('Заявки на Туры', reply_markup=gen_inline_tour_orders(data))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('one_tour|'))
async def tour_one_order(callback: types.CallbackQuery):
    await callback.message.delete()
    order = await sqlite_db.one_tour(callback.data.split('|')[1], callback.data.split('|')[2])
    chat_id = callback.data.split('|')[1]
    button_url = f'tg://user?id={chat_id}'
    markup = InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='написать пользователю', url=button_url))
    markup.add(InlineKeyboardButton(text='Удалить заявку', callback_data=f'delete|tour|{order[0]}|{order[3]}'))
    markup.add(InlineKeyboardButton(text='Назад', callback_data='tour_order'))
    
    await callback.message.answer(f'Тур\n{order[1]} - {order[2]}\nДата: {order[3]} на ({order[4]} ночей)\nОтель: {order[10]} ({order[11]} звезды)'
                                  f'\nКол-во человек:{order[5]}\nДети:{order[7]} ({order[8]} лет)', reply_markup=markup)


async def refresh_orders(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.refresh_orders('charter')
        await message.answer('Готово')

    else:
        await message.answer('Ты не админ!')

def register_admin_handler(dp: Dispatcher):

    dp.register_callback_query_handler(admin_menu, text='admin_menu')

    dp.register_callback_query_handler(consultant_order, text='consultant_order')
    dp.register_callback_query_handler(consultant_one_order, lambda x: x.data and x.data.startswith('one_consultant|'))


    dp.register_callback_query_handler(evisa_order, text='evisa_order')
    dp.register_callback_query_handler(evisa_one_order, lambda x: x.data and x.data.startswith('visa|'))
    dp.register_callback_query_handler(delete_order, lambda x: x.data and x.data.startswith('delete|')) 

    dp.register_callback_query_handler(charter_order, text='charter_order')
    dp.register_callback_query_handler(charter_one_order, lambda x: x.data and x.data.startswith('one_charter|'))

    dp.register_callback_query_handler(hotel_order, text='hotel_order')
    dp.register_callback_query_handler(hotel_one_order, lambda x: x.data and x.data.startswith('one_hotel|'))

    dp.register_callback_query_handler(tour_order, text='tour_order')
    dp.register_callback_query_handler(tour_one_order, lambda x: x.data and x.data.startswith('one_tour|'))

    dp.register_message_handler(refresh_orders, commands=['refresh'])
