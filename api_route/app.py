from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def api():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

if __name__ == '__main__':
    app.run(debug=True)
