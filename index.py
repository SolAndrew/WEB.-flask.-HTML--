from flask import Flask, url_for

app = Flask(__name__)


@app.route('/sample_page')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/Mars.jpg" alt="Марса не будет">
                    <h3>Вот она какая, красная планета.</h3>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')