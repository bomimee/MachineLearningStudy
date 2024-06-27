from flask import Flask, request, jsonify

app = Flask(__name__)

# items = ["banana, mango, apple"]
items = [
    {"id":1, "name":"Apple", "price": 5000},
    {"id":2, "name":"banana", "price": 4000},
    {"id":3, "name":"mango", "price": 6000},
]
@app.route("/")
def hello():
    return 'Hello World'

@app.route("/items", methods=['GET'])
def get_item():
    return jsonify(items)

@app.route("/items", methods=['POST'])
def add_item():
    # 요청 정보가 받아서
    item = request.get_json()
    # items에 추가 하기
    items.append(item)
    return jsonify(items)

# 메인메서드
if __name__ == '__main__':
    app.run(debug=True)