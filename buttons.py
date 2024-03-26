from telebot import types

markup_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu_btn1 = types.KeyboardButton("Написать сценарий")
menu_btn2 = types.KeyboardButton("Мой сценарий")
menu_btn3 = types.KeyboardButton("Токены")
markup_menu.add(menu_btn1)
markup_menu.add(menu_btn2, menu_btn3)

markup_additionally = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Дополнить")
btn2 = types.KeyboardButton("Начать генерацию сценария")
markup_additionally.add(btn1, btn2)

markup_end = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Конец")
markup_end.add(btn1)

markup_the_script = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn5 = types.KeyboardButton("Начать генерацию сценария")
markup_the_script.add(btn5)

markup_genre = types.InlineKeyboardMarkup(row_width=2)
markup_genre1 = types.InlineKeyboardButton(text='Хоррор', callback_data='genre1')
markup_genre2 = types.InlineKeyboardButton(text='Комедия', callback_data='genre2')
markup_genre3 = types.InlineKeyboardButton(text='Фантастика', callback_data='genre3')
markup_genre.add(markup_genre1, markup_genre2)
markup_genre.add(markup_genre3)


markup_locations = types.InlineKeyboardMarkup(row_width=2)
markup_locations0 = types.InlineKeyboardButton(text='Затерянный город', callback_data='locations1')
markup_locations3 = types.InlineKeyboardButton(text='Тропические джунгли', callback_data='locations2')
markup_locations4 = types.InlineKeyboardButton(text='Жаркая пустыня', callback_data='locations3')
markup_locations.add(markup_locations0, markup_locations3)
markup_locations.add(markup_locations4)

markup_characters = types.InlineKeyboardMarkup(row_width=2)
markup_characters1 = types.InlineKeyboardButton(text='Золушка', callback_data='characters1')
markup_characters2 = types.InlineKeyboardButton(text='Русалка', callback_data='characters2')
markup_characters3 = types.InlineKeyboardButton(text='Патрик', callback_data='characters3')
markup_characters4 = types.InlineKeyboardButton(text='Винипух', callback_data='characters4')
markup_characters.add(markup_characters1, markup_characters2)
markup_characters.add(markup_characters3, markup_characters4)


markup = types.ReplyKeyboardRemove()
