from flask import Flask, request

app = Flask(__name__)

@app.route('/likes1')
def likes():
    uid = request.args.get('uid')
    if uid:
        return f'PLAYER {uid} GOT MAXIMUM LIKES TODAY. USE ANOTHER UID.'
    else:
        return 'UID not provided.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
