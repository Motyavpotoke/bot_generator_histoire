import telebot
import logging
import threading
from buttons import markup_additionally, markup_menu, markup_characters, markup_locations, markup_genre, \
    markup_the_script, markup_end, markup
from init import (Database, Genre, Characters, Locations, Additionally, Genre_user, Characters_user,
                  Locations_user, additionally_user, Add_content, content_user, CONTROL, tok_user, session_user,
                  session, spent_tokens_user, spent_tokens_add)
from gpt import Continue_text_gpt, Question_gpt2
from setting_gpt import MAX_MODEL_TOKENS, count_tokens, create_prompt, contiune_text
from text import Greeting
from errors import error666
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
db_lock = threading.Lock()
administrators = []


@bot.message_handler(commands=['debug'])
def debug(message):
    user_id = message.chat.id
    if user_id in administrators:
        with open('errors.cod.log', 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Нет доступа')


@bot.message_handler(func=lambda message: message.text == 'Написать сценарий')
def promt_message(message):
    try:
        user_id = message.chat.id
        if user_id in administrators:
            bot.send_message(message.chat.id, 'Сначала настрой нейросеть.', reply_markup=markup),
            bot.send_message(message.chat.id, 'Выбери жанр:',
                             parse_mode='html', reply_markup=markup_genre)
        else:
            bot.send_message(message.chat.id, 'Нет доступа')

    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Дополнить')
def additionally(message):
    try:
        with db_lock:
            user_id = message.chat.id
            if user_id in administrators:
                bot.delete_message(message.chat.id, message.message_id - 1)
                bot.send_message(message.chat.id, 'Введи что должна учесть нейросеть:')

                def add_additionally(message):
                    text = message.text
                    if count_tokens(text) > MAX_MODEL_TOKENS:
                        bot.send_message(message.chat.id, "Промт слишком большой!", parse_mode='html')
                        bot.register_next_step_handler(message, additionally)
                        return
                    id = message.chat.id
                    DB = Additionally()
                    DB.add_additionally(text, id)
                    bot.send_message(message.chat.id, 'Теперь давай сгенерируем сценарий.',
                                     reply_markup=markup_the_script)

                bot.register_next_step_handler(message, add_additionally)
            else:
                bot.send_message(message.chat.id, 'Нет доступа')

    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


@bot.message_handler(commands=['start'])
def handler_start(message):
    try:
        user_id = message.chat.id
        if user_id in administrators:
            with db_lock:
                db_user = Database()
                try:
                    if not db_user.check_user_exists(message.chat.id, message.chat.first_name):
                        db_user.add_user(message.chat.id, message.chat.first_name)
                        name = message.chat.first_name
                        start = Greeting(name)
                        bot.send_message(message.chat.id, start, parse_mode='html', reply_markup=markup_menu)
                    else:
                        name = message.chat.first_name
                        start = Greeting(name)
                        bot.send_message(message.chat.id, start, parse_mode='html', reply_markup=markup_menu)
                finally:
                    db_user.close()
        else:
            bot.send_message(message.chat.id, 'Нет доступа')
    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data)
def setting_the_script(callback):
    try:
        with db_lock:
            user_id = callback.message.chat.id
            bot.answer_callback_query(callback.id)
            db = Genre()
            db1 = Characters()
            db2 = Locations()
            if callback.data == 'genre1':
                genre = 'Хоррор'
                db.add_Genre(genre, user_id)
                db.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Теперь выбери любого героя:', parse_mode='html',
                                 reply_markup=markup_characters)
            if callback.data == 'genre2':
                genre = 'Комедия'
                db.add_Genre(genre, user_id)
                db.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Теперь выбери любого героя:', parse_mode='html',
                                 reply_markup=markup_characters)
            if callback.data == 'genre3':
                genre = 'Фантастика'
                db.add_Genre(genre, user_id)
                db.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Теперь выбери любого героя:', parse_mode='html',
                                 reply_markup=markup_characters)
            if callback.data == 'characters1':
                characters = 'Золушка'
                db1.add_characters(characters, user_id)
                db1.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Затерянный город: История происходит в  затерянном городе,'
                                                           ' который исчез. '
                                                           'В этом городе могут обитать разные неизвестные миру '
                                                           'существа'"\n"
                                                           'Тропические джунгли: История происходит в лесу с '
                                                           'высокими деревьями.С которыз свисают лианы,'
                                                           'но не кто не знает что за существа обитают в глубине '
                                                           'джунглей' '\n'
                                                           'Жаркая пустыня: История происходит в '
                                                           'жаркой пустыне в которой нету источников воды и домов,'
                                                           'но в песке могут находиться разные опасные существа''\n')
                bot.send_message(callback.message.chat.id, '<b>Теперь выбери локацию:</b>', parse_mode='html',
                                 reply_markup=markup_locations)
            if callback.data == 'characters2':
                characters = 'Русалка'
                db1.add_characters(characters, user_id)
                db1.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Затерянный город: История происходит в  затерянном городе,'
                                                           ' который исчез. '
                                                           'В этом городе могут обитать разные неизвестные миру '
                                                           'существа'"\n"
                                                           'Тропические джунгли: История происходит в лесу с '
                                                           'высокими деревьями.С которыз свисают лианы,'
                                                           'но не кто не знает что за существа обитают в глубине '
                                                           'джунглей' '\n'
                                                           'Жаркая пустыня: История происходит в '
                                                           'жаркой пустыне в которой нету источников воды и домов,'
                                                           'но в песке могут находиться разные опасные существа''\n')
                bot.send_message(callback.message.chat.id, '<b>Теперь выбери локацию:</b>', parse_mode='html',
                                 reply_markup=markup_locations)
            if callback.data == 'characters3':
                characters = 'Патрик'
                db1.add_characters(characters, user_id)
                db1.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Затерянный город: История происходит в  затерянном городе,'
                                                           ' который исчез. '
                                                           'В этом городе могут обитать разные неизвестные миру '
                                                           'существа'"\n"
                                                           'Тропические джунгли: История происходит в лесу с '
                                                           'высокими деревьями.С которыз свисают лианы,'
                                                           'но не кто не знает что за существа обитают в глубине. '
                                                           'джунглей' '\n'
                                                           'Жаркая пустыня: История происходит в '
                                                           'жаркой пустыне в которой нету источников воды и домов,'
                                                           'но в песке могут находиться разные опасные существа.''\n')
                bot.send_message(callback.message.chat.id, '<b>Теперь выбери локацию:</b>', parse_mode='html',
                                 reply_markup=markup_locations)
            if callback.data == 'characters4':
                characters = 'Винипух'
                db1.add_characters(characters, user_id)
                db1.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Затерянный город: История происходит в  затерянном городе,'
                                                           ' который исчез. '
                                                           'В этом городе могут обитать разные неизвестные миру '
                                                           'существа'"\n"
                                                           'Тропические джунгли: История происходит в лесу с '
                                                           'высокими деревьями.С которыз свисают лианы,'
                                                           'но не кто не знает что за существа обитают в глубине '
                                                           'джунглей' '\n'
                                                           'Жаркая пустыня: История происходит в '
                                                           'жаркой пустыне в которой нету источников воды и домов,'
                                                           'но в песке могут находиться разные опасные существа''\n')
                bot.send_message(callback.message.chat.id, '<b>Теперь выбери локацию:</b>', parse_mode='html',
                                 reply_markup=markup_locations)

            if callback.data == 'locations1':
                locations = ('Затерянный город: История происходит в затерянном городе '
                             'с заброшенными домами и неизвестными обитателями этого города \n')

                db2.add_locations(locations, user_id)
                db2.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Если хочешь что то добавить, нажимай "Дополнить".\n'
                                                           'Если нет нажимай "Начать генерацию сценария"',
                                 parse_mode='html',
                                 reply_markup=markup_additionally)
            if callback.data == 'locations2':
                locations = ('Тропические джунгли: История происходит в джунглях с высокими деревьями и неизвестными '
                             'существами')
                db2.add_locations(locations, user_id)
                db2.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Если хочешь что то добавить, нажимай "Дополнить".\n'
                                                           'Если нет нажимай "Начать генерацию сценария"',
                                 parse_mode='html',
                                 reply_markup=markup_additionally)
            if callback.data == 'locations3':
                locations = 'Жаркая пустыня: История происходит в жаркой. сухой с опасными жителями данного биома.'
                db2.add_locations(locations, user_id)
                db2.close()
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, 'Если хочешь что то добавить, нажимай "Дополнить".\n'
                                                           'Если нет нажимай "Начать генерацию сценария"',
                                 parse_mode='html',
                                 reply_markup=markup_additionally)
    except Exception as e:
        bot.send_message(callback.message.chat.id, error666)
        logging.error(str(e))
    finally:
        db.close()
        db1.close()
        db2.close()


@bot.message_handler(func=lambda message: message.text == 'Токены')
def tokens_info(message):
    try:
        with db_lock:
            user_id = message.chat.id
            if user_id in administrators:
                user_id = message.chat.id
                spent = spent_tokens_user()
                try:
                    spent1 = spent.spent_tokens(user_id)
                finally:
                    spent.close()
                bot.send_message(message.chat.id, f'Потраченные токены: {spent1}\n\n'
                                                  'При новом сценарии токены считаются\n'
                                                  'для нового сценария.', parse_mode='html')
            else:
                bot.send_message(message.chat.id, 'Нет доступа')
    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Начать генерацию сценария')
def additionally_gpt(message):
    try:
        with db_lock:
            user_id = message.chat.id
            if user_id in administrators:
                user_id = message.chat.id
                r = tok_user()
                t = r.promt5(user_id)
                r.close()
                if t is not None and t > 0:
                    user_id = message.chat.id
                    D1 = Genre_user()
                    D2 = Characters_user()
                    D3 = Locations_user()
                    D4 = additionally_user()
                    info1 = D1.promt1(user_id)
                    info2 = D2.promt2(user_id)
                    info3 = D3.promt3(user_id)
                    info4 = D4.promt4(user_id)
                    D1.close()
                    D2.close()
                    D3.close()
                    D4.close()
                    promt1 = create_prompt(info1, info2, info3, info4)
                    bot.send_message(message.chat.id, 'Если хотите завершить сценарий\n'
                                                      'просто нажмите на кнопку.\n'
                                                      '"Конец"', reply_markup=markup_end, parse_mode='html')
                    message1 = bot.send_message(message.chat.id, 'Генерация ответа', parse_mode='html')
                    user_id = message.chat.id
                    g = Question_gpt2()
                    n1 = g.promt(promt1)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=message1.message_id, text=
                    n1, parse_mode='html')
                    SAVE = Add_content()
                    SAVE.add_content(n1, user_id)
                    SAVE.close()
                    g = promt1 + n1
                    f = count_tokens(g)
                    u = t - f
                    F = CONTROL()
                    F.add_tokens(u, user_id)
                    F.close()
                    sp2 = spent_tokens_add()
                    sp2.add_spent(f, user_id)
                    sp2.close()

                else:
                    bot.send_message(message.chat.id, 'У вас закончились сессии',
                                     parse_mode='html', reply_markup=markup_menu)

                def contiune(message):
                    text = message.text
                    if text == 'Конец':
                        bot.send_message(message.chat.id, 'Перевожу в меню:', reply_markup=markup_menu)
                        return
                    if count_tokens(text) > MAX_MODEL_TOKENS:
                        bot.send_message(message.chat.id, "Продолжение слишком огромное\n"
                                                          "Напишите его заного в меньшем размере.\n",
                                         parse_mode='html')
                        bot.register_next_step_handler(message, contiune)
                        return
                    r = tok_user()
                    t1 = r.promt5(user_id)
                    r.close()
                    if t1 is not None and t1 > 0:
                        c = content_user()
                        c1 = c.promt5(user_id)
                        c.close()
                        gpt = Continue_text_gpt()
                        con = contiune_text(text)
                        GPT1 = gpt.promt(c1, g, con)
                        script = f'{c1} \n\n {text} \n\n {GPT1}'
                        f1 = count_tokens(con + c1 + GPT1)
                        r12 = tok_user()
                        t23 = r12.promt5(user_id)
                        r12.close()
                        u2 = t23 - f1
                        F1 = CONTROL()
                        F1.add_tokens(u2, user_id)
                        F1.close()
                        bot.send_message(message.chat.id, GPT1, parse_mode='Markdown')
                        SAVE = Add_content()
                        SAVE.add_content(script, user_id)
                        if t is not None and t <= 100:
                            bot.send_message(message.chat.id, 'Ваши токены на исходе\n'
                                                              f'Осталось: {t1}', parse_mode='html')
                        spent = spent_tokens_user()
                        spent1 = spent.spent_tokens(user_id)
                        spent.close()
                        f12 = f1
                        result = spent1 + f12
                        sp2 = spent_tokens_add()
                        sp2.add_spent(result, user_id)
                        sp2.close()

                        bot.register_next_step_handler(message, contiune)
                    else:
                        user = session_user()
                        user1 = user.promt5(user_id)
                        if user1 != None:
                            user = user1 - 1
                            se = session()
                            se.add_session(user, user_id)
                            se.close()
                            bot.send_message(message.chat.id, 'Сессия завершена', parse_mode='html',
                                             reply_markup=markup_menu)
                            user = session_user()
                            user0 = user.promt5(user_id)
                            user.close()
                            if user0 is not None and user0 > 0:
                                tokens = 300
                                con = CONTROL()
                                con.add_tokens(tokens, user_id)
                                con.close()
                                bot.send_message(message.chat.id, f'У тебя осталось: <b>{user0}</b> запросов',
                                                 parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас закончились все сессии',
                                             parse_mode='html', reply_markup=markup_menu)

                bot.register_next_step_handler(message, contiune)
            else:
                bot.send_message(message.chat.id, 'Нет доступа')

    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Мой сценарий')
def The_script_user(message):
    try:
        with db_lock:
            user_id = message.chat.id
            if user_id in administrators:
                user_id = message.chat.id
                c = content_user()
                try:
                    c1 = c.promt5(user_id)
                finally:
                    c.close()
                bot.send_message(message.chat.id, 'Твой последний сценарий:\n\n'
                                                  f'{c1}', parse_mode='html')
            else:
                bot.send_message(message.chat.id, 'Нет доступа')
    except Exception as e:
        bot.send_message(message.chat.id, error666)
        logging.error(str(e))


bot.polling()
