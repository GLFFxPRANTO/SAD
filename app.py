from flask import Flask, request

app = Flask(__name__)

@app.route('/likes1')
def likes():
    uid = request.args.get('uid')

    if not uid or not uid.isdigit():  # চেক করবো UID সংখ্যা কিনা
        return 'INVALID UID CHECK TO 8-10 DIGIT', 400

    if 8 <= len(uid) <= 10:
        return f'PLAYER {uid} GOT MAXIMUM LIKES TODAY. USE ANOTHER UID.'
    else:
        return 'INVALID UID CHECK TO 8-10 DIGIT', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
