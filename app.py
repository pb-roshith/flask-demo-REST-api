from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'},
]

data = '''<h1>/api/items - display all</h1>
        <h1>/api/items/id - display only selected</h1>
'''

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/')
def index():
    return data

if __name__ == '__main__':
    app.run(debug=True)
