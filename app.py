from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def chat_page():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_msg = request.json.get('message')
    print(f"使用者說: {user_msg}")  # 可選：印出訊息到後端
    return jsonify({'reply': 'Hello'})  # 固定回傳 Hello

if __name__ == '__main__':
    app.run(debug=True)