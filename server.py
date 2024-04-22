import random
from flask import *
app = Flask(__name__)
code = ''
ipconnect = ''
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/generate')
def generate():
  global code
  global codetext
  code = random.randint(10000000, 99999999)
  codetext = str(code)
  print(code)
  return codetext
@app.route("/take", methods=["post"])
def take():
  global code
  global codetext
  from flask import request
  try:
        b = request.json.get('code')
        # Ваш код обработки данных
        if b == codetext:
          code = ''
          codetext = ''
          return "Success"
        else:
          return "NoU"
  except Exception as e:
        return f"Error: {str(e)}"
app.run(debug=True)
