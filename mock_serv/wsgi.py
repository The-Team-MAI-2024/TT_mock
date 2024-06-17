from app import create_app

# Создание экземпляра Flask приложения
app = create_app()

# Запуск Flask приложения, если данный файл запускается напрямую
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
