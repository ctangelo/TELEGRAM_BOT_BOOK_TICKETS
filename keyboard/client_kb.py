from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from dispatcher import bot



main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(main_kb)


inline_menu = InlineKeyboardMarkup(row_width=1)
inline_charter_btn = InlineKeyboardButton('✈️ Чартерные Рейсы', callback_data='charter')
schedule_btn = InlineKeyboardButton('🗓 Чартерное Расписание', url='https://taplink.cc/chartervietnam')
inline_tour_btn = InlineKeyboardButton('🌴 Пакетные Туры', callback_data='tour')
inline_hotel_btn = InlineKeyboardButton('🏨 Бронирование Отелей', callback_data='hotel')
inline_visa_btn = InlineKeyboardButton('🛂 🇻🇳 Оформление Евизы', callback_data='evisa')
inline_exchange_btn = InlineKeyboardButton('💰 Обмен Валюты', url='https://t.me/TourObmen_bot')
inline_consultant_btn = InlineKeyboardButton('👨‍💻 Консультация Менеджера', callback_data='consultant')
inline_menu.add(inline_charter_btn).add(schedule_btn).add(inline_tour_btn).add(inline_hotel_btn).add(inline_visa_btn).add(inline_exchange_btn).add(inline_consultant_btn)

# __________________EVISA__________________________
continue_btn = ReplyKeyboardMarkup(resize_keyboard=True)
cont = KeyboardButton('Продолжить заполнение')
back_to_menu = KeyboardButton('Отмена')
continue_btn.add(cont, back_to_menu)


yes_no_evisa = ReplyKeyboardMarkup(resize_keyboard=True)
yes_btn = KeyboardButton('Да')
no_btn = KeyboardButton('Нет')
return_btn = KeyboardButton('Предыдущий вопрос')
yes_no_evisa.row(yes_btn, no_btn).add(return_btn)

visa_btn = InlineKeyboardMarkup(row_width=1)
yes_visa_btn = InlineKeyboardButton('Да', callback_data='visa_yes')
menu_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
visa_btn.add(yes_visa_btn).add(menu_btn)

visa_cities = ReplyKeyboardMarkup(row_width=1)
bo_y_btn = KeyboardButton('Bo-Y')
Tan_Son_btn = KeyboardButton('Tan Son Nhat Airport (Ho Chi Minh city)')
PhuQuoc_btn = KeyboardButton('Phu Quoc International airport')
Hanoi_btn = KeyboardButton('Noi Bai Airport (Hanoi)')
Nhatrang_btn = KeyboardButton('CamRanh Airport (Nhatrang)')
Moc_Bai_btn = KeyboardButton('Moc Bai Landport')
Da_Nang_btn = KeyboardButton('Da Nang Airport')
return_btn = KeyboardButton('Предыдущий вопрос')
visa_cities.add(bo_y_btn, Tan_Son_btn, PhuQuoc_btn, Hanoi_btn, Nhatrang_btn, Moc_Bai_btn, Da_Nang_btn, return_btn)


visa_90_btn = ReplyKeyboardMarkup(resize_keyboard=True)
visa_90_single = KeyboardButton('🌐 90 дней Single')
visa_90_multi = KeyboardButton('🌐 90 дней Multiple')
visa_90_btn.add(visa_90_single, visa_90_multi)


approve_btn = ReplyKeyboardMarkup(resize_keyboard=True)
approve = KeyboardButton('Ок, понял')
approve_btn.add(approve)

previous = ReplyKeyboardMarkup(resize_keyboard=True)
prev_btn = KeyboardButton('Предыдущий вопрос')
previous.add(prev_btn)
# _______________Чартерные билеты_________________

charter_btn = InlineKeyboardMarkup(row_width=1)
yes_charter_btn= InlineKeyboardButton('Да', callback_data='charter_yes')
no_charter_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
charter_btn.add(yes_charter_btn).add(no_charter_btn)

charter_cities = InlineKeyboardMarkup(row_width=1)
nha_trang = InlineKeyboardButton('Нячанг', callback_data='Нячанг')
phukok = InlineKeyboardButton('о.Фукуок', callback_data='о.Фукуок')
almaty = InlineKeyboardButton('Алматы', callback_data='Алматы')
astana = InlineKeyboardButton('Астана', callback_data='Астана')
tashkent = InlineKeyboardButton('Ташкент', callback_data='Ташкент')
charter_cities.add(nha_trang).add(phukok).add(almaty).add(astana).add(tashkent)

yes_no_btn = InlineKeyboardMarkup(row_width=1)
yes_btn = InlineKeyboardButton('Да', callback_data='yes')
no_btn = InlineKeyboardButton('Нет', callback_data='no')
yes_no_btn.add(yes_btn).add(no_btn)

number_of_persons_btn = InlineKeyboardMarkup(row_width=1)
one_btn = InlineKeyboardButton('1', callback_data='1')
two_btn = InlineKeyboardButton('2', callback_data='2')
three_btn = InlineKeyboardButton('3', callback_data='3')
four_btn = InlineKeyboardButton('4', callback_data='4')
five_btn = InlineKeyboardButton('5', callback_data='5')
six_btn = InlineKeyboardButton('6', callback_data='6')
number_of_persons_btn.row(one_btn, two_btn, three_btn).row(four_btn, five_btn, six_btn)

number_of_childrens_btn = InlineKeyboardMarkup(row_width=1)
one_btn = InlineKeyboardButton('1', callback_data='1')
two_btn = InlineKeyboardButton('2', callback_data='2')
three_btn = InlineKeyboardButton('3', callback_data='3')
number_of_childrens_btn.row(one_btn, two_btn, three_btn)

# __________________Пакетные Туры_______________________

tour_btn = InlineKeyboardMarkup(row_width=1)
yes_tour_btn= InlineKeyboardButton('Да', callback_data='tour_yes')
no_tour_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
tour_btn.add(yes_tour_btn).add(no_charter_btn)

tour_cities = InlineKeyboardMarkup(row_width=1)
almaty = InlineKeyboardButton('Алматы', callback_data='Алматы')
astana = InlineKeyboardButton('Астана', callback_data='Астана')
tashkent = InlineKeyboardButton('Ташкент', callback_data='Ташкент')
tour_cities.add(almaty).add(astana).add(tashkent)

tour_resort = InlineKeyboardMarkup(row_width=1)
nha_trang = InlineKeyboardButton('Нячанг', callback_data='Нячанг')
phukok = InlineKeyboardButton('о.Фукуок', callback_data='о.Фукуок')
muyne = InlineKeyboardButton('Муйне', callback_data='Муйне')
tour_resort.add(nha_trang).add(phukok).add(muyne)

tour_night = InlineKeyboardMarkup(row_width=1)
seven_btn = InlineKeyboardButton('7', callback_data='7')
eight_btn = InlineKeyboardButton('8', callback_data='8')
nine_btn = InlineKeyboardButton('9', callback_data='9')
ten_btn = InlineKeyboardButton('10', callback_data='10')
eleven_btn = InlineKeyboardButton('11', callback_data='11')
twelve_btn = InlineKeyboardButton('12', callback_data='12')
thirteen_btn = InlineKeyboardButton('13', callback_data='13')
fourteen_btn = InlineKeyboardButton('14', callback_data='14')
tour_night.row(seven_btn, eight_btn, nine_btn, ten_btn).row(eleven_btn, twelve_btn, thirteen_btn, fourteen_btn)

hotel_stars_btn = InlineKeyboardMarkup(row_width=1)
three_btn = InlineKeyboardButton('3', callback_data='3')
four_btn = InlineKeyboardButton('4', callback_data='4')
five_btn = InlineKeyboardButton('5', callback_data='5')
hotel_stars_btn.row(three_btn, four_btn, five_btn)

# ________________Бронирование отелей____________________

hotel_btn = InlineKeyboardMarkup(row_width=1)
yes_hotel_btn= InlineKeyboardButton('Да', callback_data='hotel_yes')
no_hotel_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
hotel_btn.add(yes_hotel_btn).add(no_hotel_btn)

# __________________Обмен валюты_________________________

back_btn = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton('Назад', callback_data='main_menu')
back_btn.add(back)