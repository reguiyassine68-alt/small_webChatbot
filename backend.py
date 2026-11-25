import dotenv
import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
dotenv.load_dotenv()
llm= OpenAI(
    api_key= os.getenv('GROQ_API_KEY'),
    base_url= "https://api.groq.com/openai/v1"

)
default_prompt = "You are [YaGui-Bot], a helpful AI assistant. Your purpose is to give clear, accurate answers and practical help. use this just to definde yourself"
messages=[{
                   'role': 'system',
                   'content': default_prompt
              }]
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/chat', methods=['post'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '').strip()
    if not user_msg:
        return jsonify({'error': 'empty message'}), 400
    messages.append({
        'role': 'user',
        'content': user_msg
    })

    try:
        response = llm.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=messages
        )
        bot_reply = response.choices[0].message.content
        messages.append({
                            'role': 'assistant',
                            'content': bot_reply
                        })
        return jsonify({'reply': bot_reply})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/reset', methods=['post'])
def reset():
    global messages
    messages = [{
        'role': 'system', 
        'content': default_prompt
        }]
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=True)
