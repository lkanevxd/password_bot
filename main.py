from hash import *
from config import *
from markup import *
from database import *
from handlers import *


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    data = call.data
    message = call.message
    try:
        if data == "addpassword":
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(chat_id=message.chat.id, text="введи адрес сайта...",
                             reply_markup=cancel_markup())
            bot.register_next_step_handler(message, addpassword_handler_1)
        elif data.startswith("pwd_"):
            pwd_id = int(data.split("_")[-1])
            pwd = get_password(pwd_id, message.chat.id)
            master_pass = get_master_password_hash(message.chat.id)
            decrypted_pass = decrypt_data(pwd['password'], master_pass)
            decrypted_login = decrypt_data(pwd['login'], decrypted_pass)
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, f"<b>адрес сайта:</b> <code>{pwd['url']}</code>\n"
                                              f"<b>логин:</b> <code>{decrypted_login}</code>\n"
                                              f"<b>пароль:</b> <code>{decrypted_pass}</code>\n"
                                              f"<b>комментарий:</b> <i>{pwd['comment']}</i>",
                             reply_markup=password_markup(pwd_id))
        elif data.startswith("remove_"):
            pwd_id = int(data.split("_")[-1])
            delete_password(message.chat.id, pwd_id)
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, f"запись удалена с концами нахуй", reply_markup=to_passwords())
        elif data == "back_to_passwords":
            bot.delete_message(message.chat.id, message.message_id)
            passwords = get_passwords(message.chat.id)
            bot.send_message(message.chat.id, f"все твои записи:",
                             reply_markup=passwords_markup(passwords))
    except:
        bot.send_message(message.chat.id, f"невозможно получить доступ к зашифрованной базе данных, баран бля")


@bot.message_handler(commands=['start'])
def start_handler(message):
    user = hash_data(str(message.chat.id))
    if not os.path.exists(f"Databases/{user}/"):
        bot.send_message(message.chat.id, f"придумай мастер-пароль...", reply_markup=strong_password_markup())
        bot.register_next_step_handler(message, configure_database_1)
    else:
        if os.path.exists(f"Databases/{user}/passwords.db.crypt"):
            markup = new_session_markup()
        else:
            markup = main_markup()
        bot.send_message(message.chat.id, f"здарова, {message.chat.first_name}!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_handler(message):
    text = message.text
    if text == "открыть новую сессию":
        bot.send_message(message.chat.id, f"введи мастер-пароль...")
        bot.register_next_step_handler(message, new_session_handler_1)
    else:
        try:
            if text == "просмотреть пароли":
                passwords = get_passwords(message.chat.id)
                bot.send_message(message.chat.id, f"все твои записи:",
                                 reply_markup=passwords_markup(passwords))
            elif text == "сгенерировать надежный пароль":
                password = gen_strong_password()
                bot.send_message(message.chat.id, f"<b>вот твой автоматически-сгенерированный пароль:</b> <code>{password}</code>")
            elif text == "закрыть сессию":
                bot.send_message(message.chat.id, f"введи мастер-пароль...")
                bot.register_next_step_handler(message, close_session_handler)
        except:
            bot.send_message(message.chat.id, f"невозможно получить доступ к зашифрованной базе данных, баран бля")


bot.polling(none_stop=True, interval=0)
