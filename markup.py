from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def new_session_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("открыть новую сессию")
    btn2 = KeyboardButton("сгенерировать надежный пароль")
    markup.add(btn1, btn2)

    return markup


def main_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("просмотреть пароли")
    btn2 = KeyboardButton("сгенерировать надежный пароль")
    btn3 = KeyboardButton("закрыть сессию")
    markup.add(btn1, btn2, btn3)

    return markup


def passwords_markup(passwords):
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("добавить запись", callback_data=f"addpassword")
    markup.add(btn1)
    if passwords:
        for pwd in passwords:
            btn = InlineKeyboardButton(f"🔒 {pwd['url']}", callback_data=f"pwd_{pwd['id']}")
            markup.add(btn)
    else:
        btn = InlineKeyboardButton("нихуя нет", callback_data="empty")
        markup.add(btn)

    return markup


def cancel_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("отменить")
    markup.add(btn)

    return markup


def set_empty_comment():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("оставить комментарий пустым")
    btn2 = KeyboardButton("отменить")
    markup.add(btn1, btn2)

    return markup


def password_markup(pwd_id):
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("удалить запись 🗑", callback_data=f"remove_{pwd_id}")
    back = InlineKeyboardButton("назад", callback_data="back_to_passwords")
    markup.add(btn1, back)

    return markup


def to_passwords():
    markup = InlineKeyboardMarkup()
    back = InlineKeyboardButton("назад", callback_data="back_to_passwords")
    markup.add(back)

    return markup


def strong_password_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("сгенерировать надежный пароль")
    markup.add(btn1)

    return markup


def gen_strong_password_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("сгенерировать надежный пароль")
    btn2 = KeyboardButton("отменить")
    markup.add(btn1, btn2)

    return markup
