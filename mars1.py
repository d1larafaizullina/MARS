"""
Решение задач:
WEB. Введение во flask. Обработка HTML-форм
"""


from flask import Flask, url_for, request
import os

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


# Варианты выбора
@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name.upper() == 'MARS' or planet_name.upper() == 'МАРС':
        html = f'''
        <h1>Мое предложение: {planet_name.upper()}!</h1>
        <div class="alert alert-primary" role="alert">
            <p><strong>Эта планета близка к земле;</strong></p>
        </div>
        <div class="alert alert-secondary" role="alert">
            <p><strong>На ней много необходимых ресурсов;</strong></p>
        </div>
        <div class="alert alert-success" role="alert">
            <p><strong>На ней есть вода и атмосфера;</strong></p>
        </div>
        <div class="alert alert-primary" role="alert">
            <p><strong>На ней есть небольшое магнитное поле;</strong></p>
        </div>
        <div class="alert alert-secondary" role="alert">
            <p><strong>Наконец она просто красива!</strong></p>
        </div>
        '''
    elif planet_name.upper() == 'ВЕНЕРА' or planet_name.upper() == 'VENUS':
        html = f'''
        <h1>Мое предложение: {planet_name.upper()}!</h1>
        <div class="alert alert-primary" role="alert">
            <p><strong>Эта планета близка к земле;</strong></p>
        </div>
        <div class="alert alert-secondary" role="alert">
            <p><strong>На ней много необходимых ресурсов;</strong></p>
        </div>
        <div class="alert alert-success" role="alert">
            <p><strong>На ней не холодно;</strong></p>
        </div>
        <div class="alert alert-primary" role="alert">
            <p><strong>На ней всегда лето;</strong></p>
        </div>
        <div class="alert alert-secondary" role="alert">
            <p><strong>Наконец она просто красива!</strong></p>
        </div>
        '''
    else:
        html = f'''
        <div class="alert alert-danger" role="alert">
        <p><strong>Увы, предложения планеты с именем \'{planet_name.upper()}\'
         нет</strong></p>
        </div>
        '''
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                     initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Планета: {planet_name}</title>
                  </head>
                  <body>
                    {html}
                  </body>
                </html>'''


# Результат отбора
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                     initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты отбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success">Поздравляем!
                     Ваш рейтинг после {level} этапа отбора</div>
                    <div class="alert alert-secondary">
                    составляет {rating}!</div>
                    <div class="alert alert-warning">Желаем удачи!</div>
                  </body>
                </html>'''


# Загрузка файла
@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        file_content = request.files['file_content']
        if file_content:
            file_content.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                           'upload.png'))
    with open("cgi-bin/load_photo.html", 'r',
              encoding='utf-8') as html_stream:
        return html_stream.read()


# Пейзажи Марса
@app.route('/carousel')
def carousel():
    with open("cgi-bin/carousel.html", 'r',
              encoding='utf-8') as html_stream:
        return html_stream.read()


if __name__ == '__main__':
    print(os.getcwd())
    app.run(port=8080, host='127.0.0.1', debug=True)
