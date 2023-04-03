from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from dispatcher import bot


main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(main_kb)


inline_menu = InlineKeyboardMarkup(row_width=1)
inline_charter_btn = InlineKeyboardButton('✈️ Чартерные рейсы', callback_data='charter')
inline_tour_btn = InlineKeyboardButton('🌴 Пакетные туры', callback_data='tour')
inline_hotel_btn = InlineKeyboardButton('🏨 Бронирование отелей', callback_data='hotel')
inline_visa_btn = InlineKeyboardButton('🛂 Оформление Евизы во Вьетнам ', callback_data='evisa')
inline_exchange_btn = InlineKeyboardButton('💰 Обмен валюты', callback_data='exchange')
inline_consultant_btn = InlineKeyboardButton('👨‍💻 Консультация менеджера', callback_data='consultant')
inline_menu.add(inline_charter_btn).add(inline_tour_btn).add(inline_hotel_btn).add(inline_visa_btn).add(inline_exchange_btn).add(inline_consultant_btn)

# ____________EVISA_____________________________


visa_btn = InlineKeyboardMarkup(row_width=1)
yes_visa_btn = InlineKeyboardButton('Да', callback_data='visa_yes')
menu_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
visa_btn.add(yes_visa_btn).add(menu_btn)

visa_type = InlineKeyboardMarkup(row_width=1)
visa_simple_btn = InlineKeyboardButton('Обычная - 3 рабочих дня (40$)', callback_data='обычная')
visa_express_1_btn = InlineKeyboardButton('Срочная - 2 рабочих дня (80$)', callback_data='экспресс 2 дня')
visa_express_2_btn = InlineKeyboardButton('Срочная - 1 рабочий день (90$)', callback_data='экспресс 1 ден')
visa_express_3_btn = InlineKeyboardButton('Срочная - 4 часа (120$)', callback_data='экспресс 4 часа')
visa_type.add(visa_simple_btn).add(visa_express_1_btn).add(visa_express_2_btn).add(visa_express_3_btn)

visa_cities = InlineKeyboardMarkup(row_width=1)
bo_y_btn = InlineKeyboardButton('Bo-Y', callback_data='BO-Y')
Tan_Son_btn = InlineKeyboardButton('Tan Son Nhat Airport (Ho Chi Minh city)', callback_data='Tan Son Nhat Airport (Ho Chi Minh city)')
PhuQuoc_btn = InlineKeyboardButton('Phu Quoc International airport', callback_data='Phu Quoc International airport')
Hanoi_btn = InlineKeyboardButton('Noi Bai Airport (Hanoi)', callback_data='Noi Bai Airport (Hanoi)')
Nhatrang_btn = InlineKeyboardButton('CamRanh Airport (Nhatrang)', callback_data='CamRanh Airport (Nhatrang)')
Moc_Bai_btn = InlineKeyboardButton('Moc Bai Landport ', callback_data='Moc Bai Landport ')
Da_Nang_btn = InlineKeyboardButton('Da Nang Airport', callback_data='Da Nang Airport')
visa_cities.add(bo_y_btn, Tan_Son_btn, PhuQuoc_btn, Hanoi_btn, Nhatrang_btn, Moc_Bai_btn, Da_Nang_btn)

# __________________Чартерные билеты_________________________

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

charter_way_btn = InlineKeyboardMarkup(row_width=1)
one_way = InlineKeyboardButton('В одну сторону', callback_data='в одну сторону')
two_way = InlineKeyboardButton('В обе стороны', callback_data='В обе стороны')
charter_way_btn.add(one_way).add(two_way)

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

# __________________Пакетные Туры_________________________

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

# __________________Бронирование отелей_________________________

hotel_btn = InlineKeyboardMarkup(row_width=1)
yes_hotel_btn= InlineKeyboardButton('Да', callback_data='hotel_yes')
no_hotel_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
hotel_btn.add(yes_hotel_btn).add(no_hotel_btn)


# __________________Обмен валюты_________________________

exchange_btn = InlineKeyboardMarkup(row_width=1)
yes_exchange_btn = InlineKeyboardButton('Да', callback_data='exchange_yes')
no_exchange_btn = InlineKeyboardButton('Нет, вернуться в меню', callback_data='main_menu')
exchange_btn.add(yes_exchange_btn).add(no_exchange_btn)

currency_btn = InlineKeyboardMarkup(row_width=1)
rub_btn = InlineKeyboardButton('RUB', callback_data='rub')
kzt_btn = InlineKeyboardButton('KZT', callback_data='kzt')
kgs_btn = InlineKeyboardButton('KGS', callback_data='kgs')
uzs_btn = InlineKeyboardButton('UZS', callback_data='kzt')
usdt_btn = InlineKeyboardButton('USDT', callback_data='usdt')
currency_btn.row(rub_btn, kzt_btn, kgs_btn, uzs_btn, usdt_btn)


exchange_cities = InlineKeyboardMarkup(row_width=1)
nha_trang = InlineKeyboardButton('Нячанг', callback_data='нячанг')
muyne = InlineKeyboardButton('Муйне', callback_data='муйне')
phukok = InlineKeyboardButton('о.Фукуок', callback_data='о.фукуок')
danang = InlineKeyboardButton('Дананг', callback_data='дананг')
hochimin = InlineKeyboardButton('Хошимин', callback_data='хошимин')
hanoi = InlineKeyboardButton('Ханой', callback_data='ханой')
exchange_cities.row(nha_trang, phukok, muyne) 
exchange_cities.row(danang, hochimin, hanoi)


exchange_delivery = InlineKeyboardMarkup(row_width=1)
delivery_cash = InlineKeyboardButton('Доставка наличные', callback_data='доставка наличные')
pickup = InlineKeyboardButton('Самовывоз', callback_data='самовывоз')
atm = InlineKeyboardButton('Получить через банкомат', callback_data='банкомат')
exchange_delivery.add(delivery_cash, pickup, atm)

approve_btn = InlineKeyboardMarkup(row_width=1)
approve = InlineKeyboardButton('Подтвердить', callback_data='aprove')
decline = InlineKeyboardButton('Отменить', callback_data='decline')
approve_btn.add(approve, decline)