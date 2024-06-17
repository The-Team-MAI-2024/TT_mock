from flask import Flask, jsonify
import os
import time

# Создание экземпляра Flask приложения
def create_app():
    app = Flask(__name__)
    
    # Определение маршрута для корневого URL
    @app.route('/')
    def home():
        server_number = os.getenv('SERVER_NUMBER', 'unknown') # Получение номера сервера из переменной окружения
        response_time = float(os.getenv('RESPONSE_TIME', '0')) # Получение времени отклика из переменной окружения
        time.sleep(response_time) 
        return jsonify(message=f"Server {server_number} responded! Response time: {response_time}") # Возвращение JSON ответа с сервера

    return app
