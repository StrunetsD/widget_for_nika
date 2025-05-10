from flask import Flask, request, jsonify, render_template
from utils.nika_utils import get_nika_response
from utils.html_parser import html_to_text
app = Flask(__name__)
## <iframe src="http://localhost:5000" width="350" height="500"></iframe> - добавление на целевые веб-страницы
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_nika_response(user_message)
    result_response = html_to_text(response)
    return jsonify({'response': result_response})

@app.route('/')
def index():
    return render_template('chat_widget.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)