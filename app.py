from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/chatbox')
def chat_page():
    return render_template('chat.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_msg = request.json.get('message')
    print(f"使用者說: {user_msg}")  # 可選：印出訊息到後端
    return jsonify({'reply': f"你說的{user_msg}，是什麼意思？"})  # 固定回傳 Hello

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)