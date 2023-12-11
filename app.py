from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Simple response logic
    if 'اسمك' in user_message:
        reply = 'اسمي محمد.'
    elif 'عمرك' in user_message:
        reply = 'عمري 22 عاما.'
    elif 'كليتك' in user_message or 'اين تدرس' in user_message or 'كلية ايه' in user_message:
        reply = 'كلية التكنولوجيا و التنمية.'
    else:
        reply = 'لا أستطيع فهم السؤال. يمكنك أن تسألني عن اسمي أو عمري.'

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
