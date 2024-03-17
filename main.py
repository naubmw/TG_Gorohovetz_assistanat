
import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('Апи токен')

# Главное меню с кнопками
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопки с смайликами
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_info = types.KeyboardButton(text="ℹ️ информация о городе")
    button_info_sub1 = types.KeyboardButton(text="🏙️ информация о городе")
    button_info_sub2 = types.KeyboardButton(text="🏢 администрация города")
    button_navigation = types.KeyboardButton(text="🗺️ навигация по городу")
    button_navigation_sub1 = types.KeyboardButton(text="🚇 общественный транспорт")
    button_navigation_sub2 = types.KeyboardButton(text="🚖 такси")
    button_sights = types.KeyboardButton(text="🏛️ достопримечательности")
    button_sights_sub1 = types.KeyboardButton(text="🏰 замки и дворцы")
    button_sights_sub2 = types.KeyboardButton(text="⛪️ церкви и соборы")
    button_find_pet = types.KeyboardButton(text="🐾 найти питомца")
    button_find_pet_sub1 = types.KeyboardButton(text="🏢 приюты для животных")
    button_find_pet_sub2 = types.KeyboardButton(text="🐶 объявления о продаже животных")
    button_transport = types.KeyboardButton(text="🚌 транспорт и такси")
    button_transport_sub1 = types.KeyboardButton(text="🚍 автобусы и маршрутки")
    button_transport_sub2 = types.KeyboardButton(text="🚖 такси")
    button_school = types.KeyboardButton(text="🏫 Школа")
    button_school_sub1 = types.KeyboardButton(text="📚 школьные чаты")
    # Добавляем кнопки на клавиатуру
    keyboard.add(button_info, button_navigation, button_sights, button_find_pet, button_transport, button_school)
    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id, "Привет! Я Ассистент города Гороховец. Чем могу помочь?", reply_markup=keyboard)

# Ответ на выбор кнопки "Информация о городе"
@bot.message_handler(func=lambda message: message.text == "ℹ️ информация о городе")
def city_info(message):
    # Создаем кнопки подвкладок
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_info_sub1 = types.KeyboardButton(text="🏙️ информация о городе")
    button_info_sub2 = types.KeyboardButton(text="🏢 администрация города")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_info_sub1, button_info_sub2, button_back)
    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Информация о городе"
@bot.message_handler(func=lambda message: message.text == "🏙️ информация о городе")
def city_info_sub1(message):
    # Тут можно добавить информацию о городе
    bot.send_message(message.chat.id, "Здесь будет информация о городе")

# Ответ на выбор подвкладки "Администрация города"
@bot.message_handler(func=lambda message: message.text == "🏢 администрация города")
def city_info_sub2(message):
    # Тут можно добавить информацию об администрации города
    bot.send_message(message.chat.id, "Здесь будет информация об администрации города")
  
# Ответ на выбор кнопки "Навигация по городу"
@bot.message_handler(func=lambda message: message.text == "🗺️ навигация по городу")
def city_navigation(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_navigation_sub1 = types.KeyboardButton(text="🚇 общественный транспорт")
    button_navigation_sub2 = types.KeyboardButton(text="🚖 такси")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_navigation_sub1, button_navigation_sub2, button_back)

    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Общественный транспорт"
@bot.message_handler(func=lambda message: message.text == "🚇 общественный транспорт")
def city_navigation_sub1(message):
    # Тут можно добавить информацию о общественном транспорте
    bot.send_message(message.chat.id, "Здесь будет информация об общественном транспорте")

# Ответ на выбор подвкладки "Такси"
@bot.message_handler(func=lambda message: message.text == "🚖 такси")
def city_navigation_sub2(message):
    # Тут можно добавить информацию о такси
    bot.send_message(message.chat.id, "Здесь будет информация о такси")

# Ответ на выбор кнопки "Достопримечательности"
@bot.message_handler(func=lambda message: message.text == "🏛️ достопримечательности")
def city_sights(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_sights_sub1 = types.KeyboardButton(text="🏰 замки и дворцы")
    button_sights_sub2 = types.KeyboardButton(text="⛪️ церкви и соборы")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_sights_sub1, button_sights_sub2, button_back)
    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Замки и дворцы"
@bot.message_handler(func=lambda message: message.text == "🏰 замки и дворцы")
def city_sights_sub1(message):
    # Тут можно добавить информацию о замках и дворцах
    bot.send_message(message.chat.id, "Здесь будет информация о замках и дворцах")

# Ответ на выбор подвкладки "Церкви и соборы"
@bot.message_handler(func=lambda message: message.text == "⛪️ церкви и соборы")
def city_sights_sub2(message):
    # Тут можно добавить информацию о церквах и соборах
    bot.send_message(message.chat.id, "Здесь будет информация о церквах и соборах")

# Ответ на выбор кнопки "Найти питомца"
@bot.message_handler(func=lambda message: message.text == "🐾 найти питомца")
def find_pet(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_find_pet_sub1 = types.KeyboardButton(text="🏢 приюты для животных")
    button_find_pet_sub2 = types.KeyboardButton(text="🐶 объявления о продаже животных")
    button_upload_photo = types.KeyboardButton(text="📷 Загрузить фото питомца")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_find_pet_sub1, button_find_pet_sub2, button_upload_photo, button_back)
    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Приюты для животных"
@bot.message_handler(func=lambda message: message.text == "🏢 приюты для животных")
def find_pet_sub1(message):
    # Тут можно добавить информацию о приютах для животных
    bot.send_message(message.chat.id, "Здесь будет информация о приютах для животных")

# Ответ на выбор подвкладки "Объявления о продаже животных"
@bot.message_handler(func=lambda message: message.text == "🐶 объявления о продаже животных")
def find_pet_sub2(message):
    # Тут можно добавить информацию о объявлениях о продаже животных
    bot.send_message(message.chat.id, "Здесь будет информация о объявлениях о продаже животных")

# Ответ на выбор кнопки "Загрузить фото питомца"
@bot.message_handler(func=lambda message: message.text == "📷 Загрузить фото питомца")
def upload_pet_photo(message):
    # Тут можно добавить функцию загрузки фото питомца
    bot.send_message(message.chat.id, "Загрузите фото вашего питомца")

# Ответ на выбор кнопки "Транспорт и такси"
@bot.message_handler(func=lambda message: message.text == "🚌 транспорт и такси")
def city_transport(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    button_transport_sub1 = types.KeyboardButton(text="🚍 автобусы и маршрутки")
    button_transport_sub2 = types.KeyboardButton(text="🚖 такси")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_transport_sub1, button_transport_sub2, button_back)
    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Автобусы и маршрутки"
@bot.message_handler(func=lambda message: message.text == "🚍 автобусы и маршрутки")
def city_transport_sub1(message):
    # Тут можно добавить информацию об автобусах и маршрутках
    bot.send_message(message.chat.id, "Здесь будет информация об автобусах и маршрутках")

# Ответ на выбор подвкладки "Такси"
@bot.message_handler(func=lambda message: message.text == "🚖 такси")
def city_transport_sub2(message):
    # Тут можно добавить информацию о такси
    bot.send_message(message.chat.id, "Здесь будет информация о такси")

# Ответ на выбор кнопки "Школа"
@bot.message_handler(func=lambda message: message.text == "🏫 Школа")
def school_menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_school_sub1 = types.KeyboardButton(text="📚 школьные чаты")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_school_sub1, button_back)
    bot.send_message(message.chat.id, "Выберите подвкладку:", reply_markup=keyboard)

# Ответ на выбор подвкладки "Школьные чаты"
@bot.message_handler(func=lambda message: message.text == "📚 школьные чаты")
def school_chat(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_chat_1 = types.KeyboardButton(text="👦 Школьный чат 1")
    button_chat_2 = types.KeyboardButton(text="👧 Школьный чат 2")
    button_chat_3 = types.KeyboardButton(text="🧑 Школьный чат 3")
    button_back = types.KeyboardButton(text="🔙 Назад")
  
    keyboard.add(button_chat_1, button_chat_2, button_chat_3, button_back)
    bot.send_message(message.chat.id, "Выберите школьный чат:", reply_markup=keyboard)

# Ответ на выбор кнопки "Назад"
@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def go_back(message):
    send_welcome(message)

# Запускаем бота
bot.polling()
