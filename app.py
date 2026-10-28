
import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    secret = os.environ.get("MY_SECRET_MESSAGE", "переменная не задана")
    return f"""
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Моё облачное приложение</title>
        </head>
        <body>
            <h1>Приложение успешно работает!</h1>
            <p>Это моё первое приложение в облаке.</p>
            <p>Сообщение из переменной окружения: {secret}</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
