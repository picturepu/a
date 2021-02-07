#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import tg_analytic
from telebot import types
import pandas
import time
import cherrypy

API_TOKEN = '1592677355:AAG9cEilizbqUfUFAyfxacsnIqMb0IC7tCY' 

bot = telebot.TeleBot(API_TOKEN)

WEBHOOK_HOST = '20.185.43.20'
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = '/home/azureuser/tebot/webhook_cert.pem'
WEBHOOK_SSL_PRIV = '/home/azureuser/tebot/webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)

##############################Команды##############################################
@bot.message_handler(commands=['start'])
def start(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.reply_to(message, "Привіт, я бот який допоможе тобі у навчанні.", reply_markup=keyboard())
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Если что-то поломалось, и ты не знаешь почему, то пиши мне @its_oneguy")
##############################Клавиатура стартового экрана##################################
def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ras1 = types.KeyboardButton('Інформація')
    sob2 = types.KeyboardButton('Конференції')
    help3 = types.KeyboardButton('Сайти')
    sobyanin4 = types.KeyboardButton('Classroom-и')
    chats5 = types.KeyboardButton('Чати')
    niggi6 = types.KeyboardButton('Книги')
    markup.add(ras1, sob2, help3, sobyanin4, chats5, niggi6)
    return markup
#######################Клавиатуры дополненительные################################################
def keyboardate():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Понеділок')
    btn2 = types.KeyboardButton('Вівторок')
    btn3 = types.KeyboardButton('Середа')
    btn4 = types.KeyboardButton('Четвер')
    btn5 = types.KeyboardButton('Пятниця')
    btn6 = types.KeyboardButton('Субота')
    btn7 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return markup

def keyboardinfo():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    teacher1 = types.KeyboardButton('Вчителі')
    rozklad2 = types.KeyboardButton('Розклад')
    rozkladzvinkiv3 = types.KeyboardButton('Розклад дзвінків')
    nazad4 = types.KeyboardButton('Назад')
    markup.add(teacher1, rozklad2, rozkladzvinkiv3, nazad4)
    return markup

def keyboardkonf():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        konf1 = types.KeyboardButton('Фізика zoom')
        konf2 = types.KeyboardButton('Інформатика и ІТ zoom')
        konf3 = types.KeyboardButton('Інформатика 1 группа skype')
        konf4 = types.KeyboardButton('Геометрія google')
        konf5 = types.KeyboardButton('Хімія google')
        konf6 = types.KeyboardButton('Зарубіжна література zoom')
        konf7 = types.KeyboardButton('Географія google')
        konf8 = types.KeyboardButton('Астрономія zoom')
        konf9 = types.KeyboardButton('Говорилка zoom')
        back = types.KeyboardButton('Назад')
        markup.add(konf1, konf2, konf3, konf4, konf5, konf6, konf7, konf8, konf9, back)
        return markup
def keyboardteach():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    it = types.KeyboardButton('Інформатика')
    ua = types.KeyboardButton('Українська мова')
    en = types.KeyboardButton('Англійська мова')
    fiz = types.KeyboardButton('Фізика')
    ast = types.KeyboardButton('Астрономія')
    zli = types.KeyboardButton('Зарубіжна література')
    geo = types.KeyboardButton('Географія')
    mat = types.KeyboardButton('Математика')
    back = types.KeyboardButton('Назад')
    markup.add(it, ua, en, fiz, ast, zli, geo, mat, back)
    return markup
def keyboardsite():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    math = types.KeyboardButton('Сайт алгебри')
    dnevnik = types.KeyboardButton('Електронний щоденник')
    back = types.KeyboardButton('Назад')
    markup.add(math, dnevnik, back)
    return markup
def keyboardcroom():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    geo = types.KeyboardButton('Географія classroom')
    chem = types.KeyboardButton('Хімія classroom')
    astr = types.KeyboardButton('Астрономія classroom')
    geom = types.KeyboardButton('Геометрія classroom')
    back = types.KeyboardButton('Назад')
    markup.add(geo, chem, astr, geom, back)
    return markup
def keyboardchats():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    math = types.KeyboardButton('Чат математики')
    phys = types.KeyboardButton('Чат фізики')
    geog = types.KeyboardButton('Чат географії')
    biol = types.KeyboardButton('Чат біології')
    back = types.KeyboardButton('Назад')
    markup.add(math, phys, geog, biol, back)
    return markup
def keyboardknigi():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    return markup
#####################Важные слова###########################################################

@bot.message_handler(func=lambda message: "Допомога" == message.text, content_types=['text'])
def helps(message):
    bot.reply_to(message, "Если что-то поломалось, и ты не знаешь почему, то пиши мне @its_oneguy", reply_markup=keyboard())

@bot.message_handler(func=lambda message: "Інформація" == message.text, content_types=['text'])
def infor(message):
    bot.reply_to(message, "Що потрібно?", reply_markup=keyboardinfo())

@bot.message_handler(func=lambda message: "Конференції" == message.text, content_types=['text'])
def konf(message):
    bot.reply_to(message, "Ось всі конференції", reply_markup=keyboardkonf())

@bot.message_handler(func=lambda message: "Сайти" == message.text, content_types=['text'])
def helps(message):
    bot.reply_to(message, "Ось які сайти які я знаю", reply_markup=keyboardsite())

@bot.message_handler(func=lambda message: "Classroom-и" == message.text, content_types=['text'])
def helps(message):
    bot.reply_to(message, "Ось ті класруми які ми маємо", reply_markup=keyboardcroom())

@bot.message_handler(func=lambda message: "Чати" == message.text, content_types=['text'])
def helps(message):
    bot.reply_to(message, "Ось ті чати ми маємо", reply_markup=keyboardchats())

@bot.message_handler(func=lambda message: "Книги" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://t.me/joinchat/SGaRy7Nb-ZS2V3H0', reply_markup=keyboardknigi())
#####################Важные слова###########################################################
    
@bot.message_handler(func=lambda message: "Співрозмовник" == message.text, content_types=['text'])
def sogo(message):
    bot.reply_to(message, "Я не працюю, можливо буду, а можливо ні", reply_markup=keyboard())

@bot.message_handler(func=lambda message: "Розклад" == message.text, content_types=['text'])
def roskl(message):
    bot.reply_to(message, "На котрий день тобі потрібен розклад?", reply_markup=keyboardate())

@bot.message_handler(func=lambda message: "Назад" == message.text, content_types=['text'])
def back(message):
    bot.reply_to(message, "Добре, що хочеш?", reply_markup=keyboard())

@bot.message_handler(func=lambda message: "Вчителі" == message.text, content_types=['text'])
def back(message):
    bot.reply_to(message, "Який потрібен тобі зараз?", reply_markup=keyboardteach())

@bot.message_handler(func=lambda message: "Розклад дзвінків" == message.text, content_types=['text'])
def back(message):
    bot.reply_to(message, "1-ий урок 8.10 - 8.55 \n 2-ий урок 9.05 - 9.50 \n 3-ий урок 10.05 - 10.50 \n 4-ий урок 11.05 - 11.50 \n 5-ий урок 12.05 - 12.50 \n 6-ий урок 13.05 - 13.50 \n 7-ий урок 14.05 - 14.50", reply_markup=keyboardknigi())

#################Расписание#################################################################
    
@bot.message_handler(func=lambda message: "Понеділок" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, '1. Фіз-ра⚽ \n 2. Англійська мова 🇬🇧\n 3. Алгебра 🚑\n 4. Алгебра\n 5. Всесвітня історія ✝\n 6. Астрономія 🌓')

@bot.message_handler(func=lambda message: "Вівторок" == message.text, content_types=['text'])
def tue(message):
    bot.send_message(message.chat.id, '1. Геометрія (1 группа) 👨‍🎓 \n Фізика (2 группа) 📡\n 2. Геометрія (1 группа)\n Фізика (2 группа)\n3. Фізика (1 группа)📡 \n Геометрія (2 группа)👨‍🎓 \n4. Фізика (1 группа)\n Геометрія (2 группа)\n5. Фізика (лекція)\n6. Українська мова 🇺🇦 \n 7. Українська мова')

@bot.message_handler(func=lambda message: "Середа" == message.text, content_types=['text'])
def wed(message):
    bot.send_message(message.chat.id, '1. Фіз-ра ⚽\n2. Географія 🌎\n3. Географія\n4. Українська література 📖\n5. Українська література\n6. Інформатика 💻\n7. Інформатика')

@bot.message_handler(func=lambda message: "Четвер" == message.text, content_types=['text'])
def thu(message):
    bot.send_message(message.chat.id, '1. Хімія (1 группа)\nІнформаційні технології (2 группа)💻 \n2. Інформаційні технології (1 группа)\nХімія (2 группа)\n3. Хімія\n4.Мистецтво 🎨\n5. Алгебра 🚑\n6. Геометрія 👨‍🎓\n7. Історія України 🏺  ')

@bot.message_handler(func=lambda message: "Пятниця" == message.text, content_types=['text'])
def fri(message):
    bot.send_message(message.chat.id, '1. Фізика\n2. Фізика📡\n3. Англійська мова 🇬🇧\n4. Фіз-ра⚽\n5. Зарубіжна література 📖\n6. Виховна година🕓')

@bot.message_handler(func=lambda message: "Субота" == message.text, content_types=['text'])
def sat(message):
    bot.send_message(message.chat.id, '1. Біологія ☣\n2. Біологія\n3. Алгебра 🚑\n4. Алгебра\n5. Науковий практикум 📡\n6. Науковий практикум')
    
##################Конференции##################################################################

@bot.message_handler(func=lambda message: "Фізика zoom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://us04web.zoom.us/j/2509604987?pwd=bjVSczI2a3VEWTZYdUZjVmdJbityUT09')

@bot.message_handler(func=lambda message: "Інформатика и ІТ zoom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://us04web.zoom.us/j/7939162434?pwd=UXlub3ZYK2FLMVpTbHM1VUxZaG8wZz09')

@bot.message_handler(func=lambda message: "Інформатика 1 группа skype" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://join.skype.com/bHoMS0ZntVit')

@bot.message_handler(func=lambda message: "Геометрія google" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://meet.google.com/yoo-esyf-sdp')

@bot.message_handler(func=lambda message: "Зарубіжна література zoom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Іди в чат зарубіжки, воно не постійне')

@bot.message_handler(func=lambda message: "Географія google" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://meet.google.com/hsq-miim-fzw')
    
@bot.message_handler(func=lambda message: "Астрономія zoom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://us02web.zoom.us/j/83052039200?pwd=NzhhK2tHWUR5YkQ0NEF2L3p1Ujl3Zz09')

@bot.message_handler(func=lambda message: "Говорилка zoom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://us04web.zoom.us/j/7728419604?pwd=Um5Vbk9sOXdqd3JPZlRHMFhLUlRyQT09')
    
##################Учителя#####################################################################

@bot.message_handler(func=lambda message: "Інформатика" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Войцеховский Микола Олексійович (інформатика 2 група, ІТ) - nickalexv@hotmail.com - +380509311670')
    
@bot.message_handler(func=lambda message: "Українська мова" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Любомира Володимирівна (укр. мова, 1 група) - fml811kl@gmail.com - +380968129398 \n\n Порало Наталія Дмитрівна (укр. мова 2 група, укр. літ) - oginka@bk.ru')
    
@bot.message_handler(func=lambda message: "Англійська мова" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Чумакова Оксана Олександрівна (англ. мова 2 група) - oksana7902932@bigmir.net')
    
@bot.message_handler(func=lambda message: "Фізика" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Рубцова Ірина Львівна (фізика) - ira.rubts@gmail.com - +380501910780')
    
@bot.message_handler(func=lambda message: "Астрономія" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Василь Олександрович (Астрономія) - v.ponomar08@gmail.com')
    
@bot.message_handler(func=lambda message: "Зарубіжна література" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Віталіна Олегівна (зар. літ) - vitakot1997@gmail.com')
    
@bot.message_handler(func=lambda message: "Географія" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Арміне Лаврентіївна (географія, ОЗ) - armminemir@gmail.com')
    
@bot.message_handler(func=lambda message: "Математика" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Олексій Анатолійович (Алгебра) - pecheritsa.aleksey@gmail.com - +380972687157 \n\n Вікторія Борисівна (Геометрія) - +380634197635')
    
##################Сайты#######################################################################
@bot.message_handler(func=lambda message: "Сайт алгебри" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'http://sites.google.com/view/omg-upml')

@bot.message_handler(func=lambda message: "Електронний щоденник" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://atoms.com.ua/')

##################Classroom-ы#################################################################
@bot.message_handler(func=lambda message: "Географія classroom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://classroom.google.com/c/MTU2MTMyMDM3MzU5?cjc=lo2aefg')
    
@bot.message_handler(func=lambda message: "Хімія classroom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'Це єдиний классрум без посилання, тільки по коду:')
    bot.send_message(message.chat.id, 'exkqjcj')
    
@bot.message_handler(func=lambda message: "Астрономія classroom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://classroom.google.com/c/MTYzMDEwOTU3NjIz?cjc=jc4apb4')

@bot.message_handler(func=lambda message: "Геометрія classroom" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://classroom.google.com/c/MTgwNzUyMzE5NDA3?cjc=lijlnxa')
##################Чаты#######################################################################

@bot.message_handler(func=lambda message: "Чат математики" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://t.me/joinchat/MLIwYBN1JY9yiUw0Dw9ZBA')

@bot.message_handler(func=lambda message: "Чат фізики" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://t.me/joinchat/MLIwYBmeGMOc6NiPg7wsJQ')

@bot.message_handler(func=lambda message: "Чат географії" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://t.me/joinchat/NGbFclTnZJk8dS6AGq_K6Q')

@bot.message_handler(func=lambda message: "Чат біології" == message.text, content_types=['text'])
def mon(message):
    bot.send_message(message.chat.id, 'https://t.me/joinchat/OBBhBhe_b23nSVUnHv2-cg')
##################Конец бота##################################################################

bot.remove_webhook()

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Disable CherryPy requests log
access_log = cherrypy.log.access_log
for handler in tuple(access_log.handlers):
    access_log.removeHandler(handler)

# Start cherrypy server
cherrypy.config.update({
    'server.socket_host'    : WEBHOOK_LISTEN,
    'server.socket_port'    : WEBHOOK_PORT,
    'server.ssl_module'     : 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
