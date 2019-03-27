from time import sleep
from flask import Flask, request

app = Flask('varnishtest')


def row(key, value):
    return '<tr><td>' + str(key) + '</td><td>' + str(value) + '</td></tr>'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def view(path):
    result = '<!DOCTYPE html><html lang="en"><head><title>headers</title></head><body><table>'
    result += row('URL', '/' + path)
    for header, value in request.headers.items():
        result += row(header, value)
    result += '</table></body></html>'
    if 'sleep' in request.args:
        sleep(int(request.args['sleep']))
    return result
