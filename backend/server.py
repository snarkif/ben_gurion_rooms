from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize the room statuses (e.g., 10 rooms, all free initially)
rooms = ["green"] * 10

@app.route('/get_rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

@app.route('/update_room', methods=['POST'])
def update_room():
    data = request.json
    room_index = data['index']
    new_status = data['status']
    rooms[room_index] = new_status
    return jsonify({"message": "Room status updated", "rooms": rooms})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
