from flask import Flask, jsonify, json

app = Flask(__name__)

with open('discworld.json', 'r') as json_file:
    data = json_file.read()

@app.route('/api/data', methods=['GET'])
def get_data():
    """Return discworld.json as response data"""
    objects = json.loads(data)
    
    result = ""

    for key in objects:
        value = objects[key]
        result += f"{key}: {value}"

    return result
    
    


if __name__ == '__main__':
    app.run(debug=True)

