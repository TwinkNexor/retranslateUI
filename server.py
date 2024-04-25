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
@app.route('/download_file', methods=['GET'])
def download_file():
    file_path = '/root/wireguard/config/peer1/peer1.conf'  # Укажите путь к вашему файлу
    return send_file(file_path, as_attachment=True)
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
if __name__ == '__main__':
    app.run(host='37.46.131.124', port=5000)  # Замените '0.0.0.0' на желаемый IP-адрес
