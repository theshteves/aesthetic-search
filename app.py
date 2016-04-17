#!/usr/bin/python3
import urllib2
import json

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello():
    #print("PATH: " + path)

    r = urllib2.urlopen("http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC").read()
    parsed_json = json.loads(r)
    data = parsed_json['data']
    input_info = []
    for gif in data:
        input_info.append([gif['images']['downsized_medium'], gif['slug']])
    return render_template('index.html',gifs=input_info)

@app.route('/<path:path>')
def static_file(path):
        return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
