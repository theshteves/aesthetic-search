#!/usr/bin/python3

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    #print("PATH: " + path)
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
