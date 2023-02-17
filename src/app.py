import os

from flask import Flask, redirect, render_template, request, send_from_directory

app = Flask(__name__)


def get_theme():
    return request.cookies.get('theme') or 'dark'


@app.before_request
def before_request():
    if request.path != '/' and request.path.endswith('/'):  # remove trailing slash
        return redirect(request.path.removesuffix('/'))


@app.errorhandler(404)
def page_not_found(_):
    return render_template('error.html', theme=get_theme(), error_code=404,
                           error_message='Error 404 page not found')

@app.route('/')
def index():
    return render_template('index.html', theme=get_theme())



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
