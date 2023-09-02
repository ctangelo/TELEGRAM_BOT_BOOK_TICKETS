from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from dispatcher import bot, dp
from keyboard.client_kb import inline_menu, visa_btn, visa_cities, charter_btn, charter_cities, yes_no_btn, number_of_persons_btn, number_of_childrens_btn
from keyboard.client_kb import tour_btn, tour_cities, tour_resort, tour_night, hotel_stars_btn, hotel_btn, back_btn, visa_90_btn, speed_visa_btn
from keyboard.admin_kb import gen_inline_main_menu
from handlers.admin import ID
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from database import sqlite_db
import math


# @dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('👋 Привет! Я charter- бот, созданный для общения и помощи в различных задачах. Чтоб начать пользоваться нажми /menu')


# @dp.message_handler(commands=['menu'], state="*")
async def menu(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:  
        await state.finish()
    
    if message.from_user.id == ID:
        await message.answer('Здравствуйте, вот список заявок', reply_markup=gen_inline_main_menu())
    else:
        await message.answer('Чем я могу Вам помочь сегодня?', reply_markup=inline_menu)


# @dp.callback_query_handler(text=['menu'])
async def menu_2(callback: types.CallbackQuery):
    await callback.message.delete()
    
    await callback.message.answer('Чем я могу Вам помочь сегодня?', reply_markup=inline_menu)

# @dp.message_handler(commands=['consultant'], state="*")
async def consultant(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:  
        await state.finish()
    await message.answer('Ваша заявки принята, консультант свяжется с вами в ближайшее время')
    await sqlite_db.add_consultant(message.from_user.id)
    

# @dp.callback_query_handler(text=['consultant'])
async def consultant_2(callback: types.CallbackQuery):
    await callback.message.answer('Ваша заявки принята, консультант свяжется с вами в ближайшее время')
    await sqlite_db.add_consultant(callback.from_user.id)
    

# ____________EVISA_____________________________

# @dp.callback_query_handler(commands=['evisa'])
async def evisa_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Стандартное оформление визы 5 рабочих дней\n90 дней Single 40 USD\n90 дней Multiple 70 USD\nСрочное оформление \n1 рабочий день 120 USD\n2 рабочих дня 100 USD \n\nПриступим?',
                                reply_markup=visa_btn)


class FSMVisa(StatesGroup):
    visa = State()
    visa_2 = State()
    name = State()
    occupation = State()
    citizenship = State()
    passport_number = State()
    religion = State()
    old_passport_1 = State()
    old_passport_2 = State()
    double_citizenship = State()
    home_adress = State()
    phone = State()
    contact_person = State()
    job = State()
    adress_vietnam = State()
    vietnam_stay_last_year = State()
    vietnam_stay_last_year_date1 = State()
    vietnam_stay_last_year_date2 = State()
    budget = State()
    insurance = State()
    date = State()
    location = State()
    passport = State()
    photo = State()



# @dp.callback_query_handler(text=['visa_yes'], state=None)
async def visa_start(callback: types.CallbackQuery):
    await callback.message.delete()
    await FSMVisa.visa.set()
    await callback.message.answer('Выберите Визу:', reply_markup=visa_90_btn)


# @dp.callback_query_handler(text=['visa_yes'], state=None)
async def visa_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['user_id'] = callback.message.chat.id
        data['visa'] = callback.data
    await FSMVisa.next()
    await callback.message.answer('Срочность оформления:', reply_markup=speed_visa_btn)

# @dp.callback_query_handler(text=['visa_yes'], state=None)
async def visa_2_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['visa_2'] = callback.data
    await FSMVisa.next()
    await callback.message.answer('Ваше Имя Латиницей:')

# @dp.message_handler(state=FSMVisa.name)
async def name_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['name'] = message.text
    # await message.delete()
    await FSMVisa.next()
    await message.answer('Гражданство:')


# @dp.message_handler( state=FSMVisa.occupation)
async def ocupation_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['occupation'] = message.text
    
    await FSMVisa.next()
    await message.answer('Место рождения:')


# @dp.message_handler( state=FSMVisa.citizenship)
async def citizenship_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['citizenship'] = message.text
    
    await FSMVisa.next()
    await message.answer('Номер заграничного паспорта:')


# @dp.message_handler( state=FSMVisa.passport_number)
async def passport_number_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['passport_number'] = message.text
    
    await FSMVisa.next()
    await message.answer('Религия:')


# @dp.message_handler( state=FSMVisa.religion)
async def religion_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['religion'] = message.text
    
    await FSMVisa.next()
    await message.answer('Использовали ли Вы другие паспорта для въезда во Вьетнам ранее?', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMVisa.old_passport_1)
async def old_passport_load(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'no':
        async with state.proxy() as data:
                data['old_passport'] = callback.data
        
        await FSMVisa.next()
        await FSMVisa.next()
        await callback.message.answer('Имеете ли двойное гражданство?', reply_markup=yes_no_btn)

    else:
        
        await FSMVisa.next()
        await callback.message.answer('Напишите, через запятую\n\nФамилия Имя, Гражданство, Дата рождения, Номер паспорта')
        

# @dp.message_handler( state=FSMVisa.old_passport_2)
async def old_passport_2_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['old_passport'] = message.text
    
    await FSMVisa.next()
    await message.answer('Имеете ли двойное гражданство?', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMVisa.double_citizenship)
async def double_citizenship_load(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
            data['double_citizenship'] = callback.data
    
    await FSMVisa.next()
    await callback.message.answer('Адрес проживания в стране гражданства?')


# @dp.message_handler( state=FSMVisa.home_adress)
async def home_adress_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['home_adress'] = message.text
    
    await FSMVisa.next()
    await message.answer('Ваш номер телефона?')


# @dp.message_handler( state=FSMVisa.phone)
async def phone_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    
    await FSMVisa.next()
    await message.answer('Контакт для экстренной связи (Контактное лицо)?\nФамилия Имя, Контактный номер телефона, Адрес')


# @dp.message_handler( state=FSMVisa.contact_person)
async def contact_person_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_person'] = message.text
  
    await FSMVisa.next()
    await message.answer('Место работы и Должность?')


# @dp.message_handler( state=FSMVisa.job)
async def job_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job'] = message.text
 
    await FSMVisa.next()
    await message.answer('Адрес проживания во Вьетнаме?')


# @dp.message_handler( state=FSMVisa.adress_vietnam)
async def adress_vietnam_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress_vietnam'] = message.text

    await FSMVisa.next()
    await message.answer('Были ли во Вьетнаме за последний год?', reply_markup=yes_no_btn)


# @dp.callback_query_handler( state=FSMVisa.vietnam_stay_last_year)
async def vietnam_stay_last_year_load(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'no':
        async with state.proxy() as data:
            data['adress_vietnam'] = callback.data
            data['vietnam_stay_last_year_date1'] = callback.data
            data['vietnam_stay_last_year_date2'] = callback.data
    
        await FSMVisa.next()
        await FSMVisa.next()
        await FSMVisa.next()
        await callback.message.answer('Ваш планируемый бюджет расходов? (USD)?')
    else:
     
        await FSMVisa.next()
        await callback.message.answer('Дата въезда?', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(state=FSMVisa.vietnam_stay_last_year_date1, simple_cal_callback.filter())
async def vietnam_stay_last_year_date1_load(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
           
            data['vietnam_stay_last_year_date1'] = date.strftime("%d/%m/%Y")

        await FSMVisa.next()
        await callback.message.answer('Дата вsезда?', reply_markup=await SimpleCalendar().start_calendar())



# @dp.callback_query_handler(state=FSMVisa.vietnam_stay_last_year_date2, simple_cal_callback.filter())
async def vietnam_stay_last_year_date2_load(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
           
            data['vietnam_stay_last_year_date2'] = date.strftime("%d/%m/%Y")

        await FSMVisa.next()
        await callback.message.answer('Ваш планируемый бюджет расходов? (USD)')


# @dp.callback_query_handler( state=FSMVisa.budget)
async def budget_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['budget'] = message.text

    await FSMVisa.next()
    await message.answer('Ваша медицинская страховка? (если нет, то пишите "нет")')



# @dp.callback_query_handler( state=FSMVisa.insurance)
async def insurance_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['insurance'] = message.text

    await FSMVisa.next()
    await message.answer('Выберите дату пересечения границы:', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(state=FSMVisa.date, simple_cal_callback.filter())
async def visa_load_date(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
           
            data['date'] = date.strftime("%d/%m/%Y")

        await FSMVisa.next()
        await callback.message.answer('Теперь введите место пересечения границы', reply_markup=visa_cities)


# @dp.callback_query_handler(state=FSMVisa.location)
async def visa_load_location(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
            data['location'] = callback.data

    await FSMVisa.next()
    await callback.message.answer('Теперь загрузите скан паспорта')


# @dp.callback_query_handler(content_types=['photo'], state=FSMVisa.passport)
async def visa_load_passport(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['passport'] = message.photo[0].file_id
    await FSMVisa.next()

    await message.answer('Теперь загрузите ваше фото на белом фоне')


# @dp.callback_query_handler(content_types=['photo'], state=FSMVisa.photo)
async def visa_load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
 
    await sqlite_db.add_visa(state)
    await state.finish()
    await message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')

# __________________Чартерные билеты_________________________

class FSMCharter(StatesGroup):
     departure = State()
     arrival = State()
     date_departure = State()
     one_two_way = State()
     date_back = State()
     number_of_persons = State()
     children = State()
     number_of_childrens = State()


# @dp.callback_query_handler(text=['charter'])
async def charter(callback: types.CallbackQuery):
     await callback.message.delete()
     await callback.message.answer('⚠️ Авиабилеты на чартерные рейсы обмену и возврату не подлежат.\n\n'
                                   '🧳 Включен багаж - 20 кг, ручная кладь - 8 кг\n\nПриступим?', reply_markup=charter_btn)


# @dp.callback_query_handler(text=['charter_yes'], state=None)
async def charter_start(callback: types.CallbackQuery):
     await FSMCharter.departure.set()
     await callback.message.delete()
     await callback.message.answer('Выберите город вылета', reply_markup=charter_cities)


# @dp.callback_query_handler(state=FSMCharter.departure)
async def departure_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['user_id'] = callback.from_user.id
         data['departure'] = callback.data
    await FSMCharter.next()
    await callback.message.delete()
    await callback.message.answer('Выберите город прилета:', reply_markup=charter_cities)


# @dp.callback_query_handler(state=FSMCharter.arrival)
async def arrival_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['arrival'] = callback.data
    await FSMCharter.next()
    await callback.message.delete()
    await callback.message.answer('Выберите дату отправления', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(simple_cal_callback.filter(), state=FSMCharter.date_departure)
async def date_departure_load(callback: types.CallbackQuery, callback_data: dict, state=FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
            data['date_departure'] = date.strftime("%d/%m/%Y")
    
        await FSMCharter.next()
        await callback.message.delete()
        await callback.message.answer('Нужны ли билеты обратно?', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMCharter.one_two_way)
async def one_two_way_load(callback: types.CallbackQuery, state=FSMContext):
    
    if callback.data == 'yes':
         async with state.proxy() as data:
            data['one_two_way'] = 'в обе'
         await FSMCharter.next()
         await callback.message.delete()
         await callback.message.answer('Выберите дату отправления', reply_markup=await SimpleCalendar().start_calendar())

    else:
         async with state.proxy() as data:
            data['one_two_way'] = 'в одну'
         await FSMCharter.next()
         async with state.proxy() as data:
            data['date_back'] = callback.data
         await FSMCharter.next()
         await callback.message.delete()
         await callback.message.answer('Сколько человек?', reply_markup=number_of_persons_btn)


# @dp.callback_query_handler(simple_cal_callback.filter(), state=FSMCharter.date_back)
async def date_back_load(callback: types.CallbackQuery, callback_data: dict, state=FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
            data['date_back'] = date.strftime("%d/%m/%Y")
    
        await FSMCharter.next()
        await callback.message.delete()
        await callback.message.answer('Сколько человек?', reply_markup=number_of_persons_btn)


# @dp.callback_query_handler(state=FSMCharter.number_of_persons)
async def number_of_persons_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_persons'] = callback.data

    await FSMCharter.next()
    await callback.message.delete()
    await callback.message.answer('Путешествуют ли с Вами младенцы до 2 лет', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMCharter.children)
async def children_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['children'] = callback.data

    if callback.data == 'no':
         await FSMCharter.next()
         async with state.proxy() as data:
            data['number_of_children'] = 0
         await callback.message.delete()
         await sqlite_db.add_charter(state)
         await state.finish()
         await callback.message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')

    else:
         await FSMCharter.next()
         await callback.message.delete()
         await callback.message.answer('Выберите количество младенцев', reply_markup=number_of_childrens_btn)


# @dp.callback_query_handler(state=FSMCharter.number_of_childrens)
async def number_of_childrens_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_childrens'] = callback.data
    async with state.proxy() as data:
         await callback.message.delete()
         await sqlite_db.add_charter(state)
         await state.finish()
         await callback.message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')


# __________________Пакетные Туры_________________________

class FSMTour(StatesGroup):
     departure = State()
     resort = State()
     date_departure = State()
     amount_of_nights = State()
     number_of_persons = State()
     children = State()
     number_of_childrens = State()
     age_children = State()
     hotel = State()
     hotel_name = State()
     stars = State()


# @dp.callback_query_handler(text=['tour'])
async def tour(callback: types.CallbackQuery):
     await callback.message.delete()
     await callback.message.answer('Каждый тур включает в себя:\n\n✈️ Авиаперелет туда-обратно\n🏨 Проживание\n😋'
                                   'Питание (опция)\n🚌 Трансфер\n🏥 Мед.страховка\n\nПриступим?', reply_markup=tour_btn)


# @dp.callback_query_handler(text=['tour_yes'], state=None)
async def tour_start(callback: types.CallbackQuery):
     await FSMTour.departure.set()
     await callback.message.delete()
     await callback.message.answer('Выберите город вылета', reply_markup=tour_cities)


# @dp.callback_query_handler(state=FSMTour.departure)
async def tour_departure_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['user_id'] = callback.from_user.id
         data['departure'] = callback.data
    await FSMTour.next()
    await callback.message.delete()
    await callback.message.answer('Выберите курорт:', reply_markup=tour_resort)


# @dp.callback_query_handler(state=FSMTour.resort)
async def resort_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['resort'] = callback.data
    await FSMTour.next()
    await callback.message.delete()
    await callback.message.answer('Выберите дату вылета:', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(simple_cal_callback.filter(), state=FSMTour.date_departure)
async def tour_date_departure_load(callback: types.CallbackQuery, callback_data: dict, state=FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
            data['date_departure'] = date.strftime("%d/%m/%Y")
    
        await FSMTour.next()
        await callback.message.delete()
        await callback.message.answer('Количество ночей?', reply_markup=tour_night)


# @dp.callback_query_handler(state=FSMTour.amount_of_nights)
async def tour_amount_of_nights_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['amount_of_nights'] = callback.data
    await FSMTour.next()
    await callback.message.delete()
    await callback.message.answer('Количество человек:', reply_markup=number_of_persons_btn)


# @dp.callback_query_handler(state=FSMTour.number_of_persons)
async def tour_number_of_persons_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_persons'] = callback.data
    await FSMTour.next()
    await callback.message.delete()
    await callback.message.answer('Путешествуют ли с Вами дети', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMTour.children)
async def tour_children_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['children'] = callback.data
    if callback.data == 'no':
         await FSMTour.next()
         async with state.proxy() as data:
            data['number_of_childrens'] = callback.data
         await FSMTour.next()
         async with state.proxy() as data:
            data['age_children'] = callback.data
         await FSMTour.next()
         await callback.message.delete()
         await callback.message.answer('Есть ли у вас отель на примете?', reply_markup=yes_no_btn)
    else:
        await FSMTour.next()
        await callback.message.delete()
        await callback.message.answer('Тур пакет\nКоличество детей:', reply_markup=number_of_childrens_btn)


# @dp.callback_query_handler(state=FSMTour.number_of_childrens)
async def tour_number_of_childrens_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_childrens'] = callback.data
    await FSMTour.next()
    await callback.message.delete()
    await callback.message.answer('Введите возраст детей через пробел')


# @dp.message_handler(state=FSMTour.age_children)
async def tour_age_children(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
         data['age_children'] = message.text
    await FSMTour.next()
    await message.delete()
    await message.answer('Есть ли у вас отель на примете?', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMTour.hotel)
async def tour_hotel_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['hotel'] = callback.data
    if callback.data == 'no':
        await FSMTour.next()
        async with state.proxy() as data:
            data['hotel_name'] = callback.data
        await FSMTour.next()
        await callback.message.delete()
        await callback.message.answer('Выберите кол-во звед в отеле', reply_markup=hotel_stars_btn)

    else:
        await FSMTour.next()
        await callback.message.delete()
        await callback.message.answer('Тур пакет\nНапишите название отеля')


# @dp.message_handler(state=FSMTour.hotel_name)
async def tour_hotel_name_load(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['hotel'] = message.text
        data['hotel_name'] = message.text
        
    await FSMTour.next()
    async with state.proxy() as data:
        data['stars'] = 'no'
    
    await message.delete()
    await sqlite_db.add_tour(state)
    await message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')
    await state.finish()

# @dp.register_callback_query_handler(state=FSMTour.stars)
async def tour_stars_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['stars'] = callback.data
   
    await callback.message.delete()
    await sqlite_db.add_tour(state)
    await callback.message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')
    await state.finish()


# __________________Бронирование отелей_________________________

class FSMHotel(StatesGroup):
    resort = State()
    hotel = State()
    hotel_name = State()
    stars = State()
    arrival_day = State()
    amount_of_nights = State()
    amount_of_person = State()
    children = State()
    number_of_childrens = State()
    age_of_children = State()


# @dp.callback_query_handler(text=['hotel'])
async def hotel(callback: types.CallbackQuery):
     await callback.message.delete()
     await callback.message.answer('Мы бронируем отели во Вьетнаме по лучшим тарифам.\n\nПриступим?', reply_markup=hotel_btn)


# @dp.callback_query_handler(text=['hotel_yes'], state=None)
async def hotel_start(callback: types.CallbackQuery):
     await FSMHotel.resort.set()
     await callback.message.delete()
     await callback.message.answer('Выберите курорт:', reply_markup=tour_resort)


# @dp.callback_query_handler(state=FSMHotel.resort)
async def hotel_resort_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['user_id'] = callback.from_user.id
        data['resort'] = callback.data
    await FSMHotel.next()
    await callback.message.delete()
    await callback.message.answer('Есть ли у вас отель на примете?', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMHotel.hotel)
async def hotel_load(callback: types.CallbackQuery, state=FSMContext):
    
    
    if callback.data == 'no':
        async with state.proxy() as data:
            data['hotel'] = 'не важно'
        await FSMHotel.next()
        async with state.proxy() as data:
            data['hotel_name'] = callback.data
        await FSMHotel.next()
        await callback.message.delete()
        await callback.message.answer('Выберите кол-во звезд в отеле', reply_markup=hotel_stars_btn)
    
    else:
        async with state.proxy() as data:
            data['hotel'] = callback.data
        await FSMHotel.next()
        await callback.message.delete()
        await callback.message.answer('Напишите название отеля')


# @dp.message_handler(state=FSMHotel.hotel_name)
async def hotel_name_load(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['hotel_name'] = message.text
        data['hotel'] = message.text
    await FSMHotel.next()
    async with state.proxy() as data:
        data['stars'] = 'no'
    await FSMHotel.next()
    await message.delete()
    await message.answer('Выберите дату заселения:', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(state=FSMHotel.stars)
async def stars_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['stars'] = callback.data
    await FSMHotel.next()
    await callback.message.delete()
    await callback.message.answer('Выберите дату заселения:', reply_markup=await SimpleCalendar().start_calendar())


# @dp.callback_query_handler(simple_cal_callback.filter(), state=FSMHotel.arrival_day)
async def arrival_day_load(callback: types.CallbackQuery, callback_data: dict, state=FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
            data['arrival_day'] = date.strftime("%d/%m/%Y")
        await FSMHotel.next()
        await callback.message.delete()
        await callback.message.answer('Напишите количество ночей:')


# @dp.callback_query_handler(state=FSMHotel.amount_of_nights)
async def amount_of_nights_load(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['amount_of_nights'] = int(message.text)
    await FSMHotel.next()
    await message.delete()
    await message.answer('Количество человек:', reply_markup=number_of_persons_btn)


# @dp.message_handler(state=FSMHotel.amount_of_person)
async def hotel_number_of_persons_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_persons'] = callback.data
    await FSMHotel.next()
    await callback.message.delete()
    await callback.message.answer('Путешествуют ли с Вами дети', reply_markup=yes_no_btn)


# @dp.callback_query_handler(state=FSMHotel.children)
async def hotel_children_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['children'] = callback.data
    if callback.data == 'no':
         await FSMHotel.next()
         async with state.proxy() as data:
            data['number_of_childrens'] = callback.data
         await FSMHotel.next()
         async with state.proxy() as data:
            data['age_children'] = callback.data
         await callback.message.delete()
         await sqlite_db.add_hotel(state)
         await state.finish()
         await callback.message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')
         
         
    else:
        await FSMHotel.next()
        await callback.message.delete()
        await callback.message.answer('Количество детей:', reply_markup=number_of_childrens_btn)


# @dp.callback_query_handler(state=FSMHotel.number_of_childrens)
async def hotel_number_of_childrens_load(callback: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
         data['number_of_childrens'] = callback.data
    await FSMHotel.next()
    await callback.message.delete()
    await callback.message.answer('Введите возраст детей через пробел')


# @dp.message_handler(state=FSMHotel.age_of_children)
async def hotel_age_children(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
         data['age_children'] = message.text
    await message.delete()
    await sqlite_db.add_hotel(state)
    await state()
    await message.answer('Спасибо, ваша заявка приянта, оператор свяжется с вами в ближайшее время')


# __________________Обмен денег _________________________



# @dp.callback_query_handler(text=['exchange'])
async def exchange(callback: types.CallbackQuery):
     await callback.message.delete()
     await callback.message.answer('Для оформления заявки напишите сюда\n\nhttps://t.me/TourObmen_bot', reply_markup=back_btn)





# __________________Регистрация хендлеров _________________________


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(menu, commands=['menu'], state="*")
    dp.register_callback_query_handler(menu_2, text=['main_menu'])

    dp.register_message_handler(consultant, commands=['consultant'], state="*")
    dp.register_callback_query_handler(consultant_2, text=['consultant'])

    dp.register_callback_query_handler(evisa_menu, text=['evisa'])
    dp.register_callback_query_handler(visa_start, text=['visa_yes'], state=None)
    dp.register_callback_query_handler(visa_load, state=FSMVisa.visa)
    dp.register_callback_query_handler(visa_2_load, state=FSMVisa.visa_2)
    dp.register_message_handler(name_load, state=FSMVisa.name)
    dp.register_message_handler(ocupation_load, state=FSMVisa.occupation)
    dp.register_message_handler(citizenship_load, state=FSMVisa.citizenship)
    dp.register_message_handler(passport_number_load, state=FSMVisa.passport_number)
    dp.register_message_handler(religion_load, state=FSMVisa.religion)
    dp.register_callback_query_handler(old_passport_load, state=FSMVisa.old_passport_1)
    dp.register_message_handler(old_passport_2_load, state=FSMVisa.old_passport_2)
    dp.register_callback_query_handler(double_citizenship_load, state=FSMVisa.double_citizenship)
    dp.register_message_handler(home_adress_load, state=FSMVisa.home_adress)
    dp.register_message_handler(phone_load, state=FSMVisa.phone)
    dp.register_message_handler(contact_person_load, state=FSMVisa.contact_person)
    dp.register_message_handler(job_load, state=FSMVisa.job)
    dp.register_message_handler(adress_vietnam_load, state=FSMVisa.adress_vietnam)
    dp.register_callback_query_handler(vietnam_stay_last_year_load, state=FSMVisa.vietnam_stay_last_year)
    dp.register_callback_query_handler(vietnam_stay_last_year_date1_load, simple_cal_callback.filter(), state=FSMVisa.vietnam_stay_last_year_date1)
    dp.register_callback_query_handler(vietnam_stay_last_year_date2_load, simple_cal_callback.filter(), state=FSMVisa.vietnam_stay_last_year_date2)
    dp.register_message_handler(budget_load, state=FSMVisa.budget)
    dp.register_message_handler(insurance_load, state=FSMVisa.insurance)
    dp.register_callback_query_handler(visa_load_date, simple_cal_callback.filter(), state=FSMVisa.date)
    dp.register_callback_query_handler(visa_load_location, state=FSMVisa.location)
    dp.register_message_handler(visa_load_passport, content_types=['photo'], state=FSMVisa.passport)
    dp.register_message_handler(visa_load_photo, content_types=['photo'], state=FSMVisa.photo)
    


    dp.register_callback_query_handler(charter, text=['charter'])
    dp.register_callback_query_handler(charter_start, text=['charter_yes'], state=None)
    dp.register_callback_query_handler(departure_load, state=FSMCharter.departure)
    dp.register_callback_query_handler(arrival_load, state=FSMCharter.arrival)
    dp.register_callback_query_handler(date_departure_load, simple_cal_callback.filter(), state=FSMCharter.date_departure)
    dp.register_callback_query_handler(one_two_way_load, state=FSMCharter.one_two_way)
    dp.register_callback_query_handler(date_back_load, simple_cal_callback.filter(), state=FSMCharter.date_back)
    dp.register_callback_query_handler(number_of_persons_load, state=FSMCharter.number_of_persons)
    dp.register_callback_query_handler(children_load, state=FSMCharter.children)
    dp.register_callback_query_handler(number_of_childrens_load, state=FSMCharter.number_of_childrens)


    dp.register_callback_query_handler(tour, text=['tour'])
    dp.register_callback_query_handler(tour_start, text=['tour_yes'], state=None)
    dp.register_callback_query_handler(tour_departure_load, state=FSMTour.departure)
    dp.register_callback_query_handler(resort_load, state=FSMTour.resort)
    dp.register_callback_query_handler(tour_date_departure_load, simple_cal_callback.filter(), state=FSMTour.date_departure)
    dp.register_callback_query_handler(tour_amount_of_nights_load, state=FSMTour.amount_of_nights)
    dp.register_callback_query_handler(tour_number_of_persons_load, state=FSMTour.number_of_persons)
    dp.register_callback_query_handler(tour_children_load, state=FSMTour.children)
    dp.register_callback_query_handler(tour_number_of_childrens_load, state=FSMTour.number_of_childrens)
    dp.register_message_handler(tour_age_children, state=FSMTour.age_children)
    dp.register_callback_query_handler(tour_hotel_load, state=FSMTour.hotel)
    dp.register_message_handler(tour_hotel_name_load, state=FSMTour.hotel_name)
    dp.register_callback_query_handler(tour_stars_load, state=FSMTour.stars)
 

    dp.register_callback_query_handler(hotel, text=['hotel'])
    dp.register_callback_query_handler(hotel_start, text=['hotel_yes'], state=None)
    dp.register_callback_query_handler(hotel_resort_load, state=FSMHotel.resort)
    dp.register_callback_query_handler(hotel_load, state=FSMHotel.hotel)
    dp.register_message_handler(hotel_name_load, state=FSMHotel.hotel_name)
    dp.register_callback_query_handler(stars_load, state=FSMHotel.stars)
    dp.register_callback_query_handler(arrival_day_load, simple_cal_callback.filter(), state=FSMHotel.arrival_day)
    dp.register_message_handler(amount_of_nights_load, state=FSMHotel.amount_of_nights)
    dp.register_callback_query_handler(hotel_number_of_persons_load, state=FSMHotel.amount_of_person)
    dp.register_callback_query_handler(hotel_children_load, state=FSMHotel.children)
    dp.register_callback_query_handler(hotel_number_of_childrens_load, state=FSMHotel.number_of_childrens)
    dp.register_message_handler(hotel_age_children, state=FSMHotel.age_of_children)


    dp.register_callback_query_handler(exchange, text=['exchange'])
   

    