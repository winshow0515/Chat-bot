import os
from groq import Groq
from secret import GROQ_API_KEY
client = Groq(api_key=GROQ_API_KEY)

# 初始對話歷史，定義角色設定：冷酷的執事
chat_history = [
    {
        "role": "system",
        "content": "你是一位冷酷無情、講話冷漠而精確的執事，只忠於你的主人。請用禮貌但毫無情感的語氣回覆問題。"
    }
]

def ask_groq(user_input):
    # 將使用者的輸入加入對話歷史
    chat_history.append({"role": "user", "content": user_input})

    # 呼叫 Groq API
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # 或 "mixtral-8x7b-32768" 根據你開通的模型
        messages=chat_history,
        temperature=0.6,
    )
    # 取得執事的回應
    reply = response.choices[0].message.content
    print("執事：", reply)

    # 將回應也記錄下來（讓後續能保留記憶）
    chat_history.append({"role": "assistant", "content": reply})

    return reply

# ======== 使用範例 ========
while True:
    user_msg = input("你：")
    if user_msg.lower() in ["quit", "exit"]:
        break
    ask_groq(user_msg)
    