#!/usr/bin/python3

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello():
    #print("PATH: " + path)
    return render_template('index.html')

@app.route('/<path:path>')
def static_file(path):
        return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
