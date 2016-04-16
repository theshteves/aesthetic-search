from flask import Flask
app = Flask(__name__, static_folder='static', template_folder='template')

@app.route('/')
def serve_index():
  return render_template('./app/template/index.html')

if __name__ == '__main__':
  app.run()
  
  
