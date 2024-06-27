from flask import Flask, request, jsonify

app = Flask(__name__)

items = ['banana', 'apple','mango']
@app.route("/")
def hello():
    return  'Hello World'


@app.route("/items", methods=["GET"])
def get_item():
    return jsonify(items)


@app.route("/items", methods=["POST"])
def add_item():
    item = request.get_json()
    items.append(item)
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
