from flask import Flask
from routes import main_routes
from models.database import init_db
from dotenv import load_dotenv
import os

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

# Створюємо екземпляр додатку
# Ім'я додатку передається в якості аргументу
app = Flask(__name__)

# Налаштовуємо секретний ключ
# Секретний ключ використовується для підпису куків
# Це необхідно для безпеки додатку
# Ключ повинен бути випадковим і складатися з багатьох символів
# Наприклад, можна використати генератор паролів
# Наприклад, https://passwordsgenerator.net/
app.secret_key = os.getenv("SECRET_KEY")

# Реєструємо маршрути
# Маршрути реєструються за допомогою функції register_blueprint
app.register_blueprint(main_routes)

# Ініціалізуємо базу даних
# Ініціалізація бази даних відбувається в контексті додатку
with app.app_context():
    init_db()

# Запускаємо додаток
# Якщо файл запущений як головний, то запускаємо сервер
# Якщо файл імпортований в інший файл, то сервер не запускається
if __name__ == '__main__':
    app.run(debug=True)
