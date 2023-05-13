from flask import Flask, jsonify, request
from data import stars
app = Flask(__name__)

@app.route('/')

def main():
    return jsonify({
        'data': stars
    })

@app.route('/star')

def planet():
    starName = request.args.get('name')
    starData = next(i for i in stars if i ['name'] == starName)
    return jsonify({
        'data': starData
    })



app.run()
