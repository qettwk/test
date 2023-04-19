import telebot # импорт библиотеки для работы Python с Telegram ботами

mybot = telebot.TeleBot('6026532140:AAFSDrDcF5ARezc0FzhqxU9hBULtFh7q3Bo') # ключ для бота
@mybot.message_handler(content_types=['text']) # бот "ловит" текстовые сообщения типа "текст"


def echo_message(message): # функция, на вход сообщение
    mybot.send_message(message.from_user.id, message.text) # отправка сообщения (параметра "text" объекта "message")
                                                            # тому же пользователю

mybot.polling(none_stop=True, interval=0)                   # "опрос" работы бота без перерырыва (интервал 0)
mybot.echo_message                                           # применение функции бота
