from telebot import TeleBot, types
import test as anime

BoyGoW = TeleBot('982167824:AAEiCXI9z3uYKKOUVingUuaki_kA2uV2n4s')

def show_zodiac_bottons_on(message):
    keyboard = types.InlineKeyboardMarkup()

    for zod in anime.zods:
        key_zod = types.InlineKeyboardButton(text=zod, callback_data='zodiac')
        keyboard.add(key_zod)

<<<<<<< HEAD
    BoyGoW.send_message(message.from_user.id, 'Выбери свой знак зодиака, МАЛЬЧИК!', reply_markup=keyboard)
=======
    BoyGoW.send_message(message.from_user.id, 'ВЫбери свой знак зодиака, МАЛЬЧИК!', reply_markup=keyboard)
>>>>>>> 65901c6bfcbd6628f27af3e58cb7e7bfe76d76e3

@BoyGoW.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == r'\hello':
        BoyGoW.send_message(message.from_user.id, 'Привет, МАЛЬЧИК! Сечас я расскажу твой гороскоп!')
        show_zodiac_bottons_on(message)
    elif message.text == r'\help':
        BoyGoW.send_message(message.from_user.id, 'Напиши \\hello МАЛЬЧИК!!!')
    else:
        BoyGoW.send_message(message.from_user.id, 'Ты не разобрался, МАЛЬЧИК, напиши \\help')

@BoyGoW.callback_query_handler(func=lambda call: True)
def callback_worker(call):
<<<<<<< HEAD
    if call.data == 'zodiac':
=======
    if call_data == 'zodiac':
>>>>>>> 65901c6bfcbd6628f27af3e58cb7e7bfe76d76e3
        msg = anime.get_prediction()
        BoyGoW.send_message(call.message.chat.id, msg)

BoyGoW.polling(none_stop=True, interval=0)