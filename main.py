import telebot
from telebot import types

bot = telebot.TeleBot('5551651151:AAGIKgx1tXFfAb7ULfM84nv8a_sqojYL0FI')
@bot.message_handler(commands=['start']) # метод, который отслеживает различные команды

def start(message):
    mess = f'Привет {message.from_user.first_name} ' #ловим имя и фамилию пользователя и сохраняем их в переменную
    bot.send_message(message.chat.id, mess) # метод, который позволяет отправить сообщение(или любой другой тип данных) в телеграмбот


@bot.message_handler(content_types=['text']) #метод, который отслеживет текст введенный пользователем
def get_user_text(message):
    if message.text == 'BMW':
        markup = types.InlineKeyboardMarkup()  # метод позволяющий создавать различные кновки вместе с текстом
        markup.add(types.InlineKeyboardButton('Перейдите по ссылке', url='https://cars.av.by/bmw')) # компануем кнопку
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)  # вставляем кновку вместе с текстом
    elif message.text == 'Audi':
        markup = types.InlineKeyboardMarkup()  # метод позволяющий создавать различные кновки вместе с текстом
        markup.add(types.InlineKeyboardButton('Перейдите по ссылке', url='https://cars.av.by/audi')) # компануем кнопку
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
    elif message.text == 'Mercedes':
        markup = types.InlineKeyboardMarkup()  # метод позволяющий создавать различные кновки вместе с текстом
        markup.add(types.InlineKeyboardButton('Перейдите по ссылке', url='https://cars.av.by/mercedes-benz')) # компануем кнопку
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')

bot.polling(none_stop=True) #запускаем бот, со значением работы постоянно