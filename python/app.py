from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'name': 'alice', 'email': '[email protected]'})

if __name__ == '__main__':
    app.run()

@app.route('/create', methods=['POST'])
def create():
    # Your logic here
    return jsonify({'message': 'Resource created successfully'})
