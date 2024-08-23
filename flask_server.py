from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__)

# Global variables to store current game data
current_target_coord = None
current_target_color = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    if current_target_coord and current_target_color:
        return jsonify({
            'coordinates': current_target_coord,
            'color': current_target_color
        })
    return jsonify({'error': 'No data available'})

@app.route('/update', methods=['POST'])
def update():
    global current_target_coord, current_target_color
    data = request.json
    current_target_coord = data.get('coordinates')
    current_target_color = data.get('color')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='192.168.56.1', port=5000)
