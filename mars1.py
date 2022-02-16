from flask import Flask, url_for, request
import os

app = Flask(__name__)


# Колонизация Марса
@app.route('/')
def show():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    with open('cgi-bin/index.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


# Рекламная кампания
@app.route('/promotion')
def promotion():
    with open('cgi-bin/promotion.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


# Изображение Марса
@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars2.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


# Реклама с картинкой
@app.route('/promotion_image')
def promotion_image():
    with open("cgi-bin/promotion_image.html", 'r',
              encoding='utf-8') as html_stream:
        return html_stream.read()


# Отбор астронавтов
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        with open("cgi-bin/astronaut_selection.html", 'r',
                  encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    print(os.getcwd())
    app.run(port=8080, host='127.0.0.1')
