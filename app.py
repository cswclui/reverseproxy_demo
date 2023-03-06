from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/about')
def get_about():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    #jsonify function will serialize the given Python object into a JSON-formatted string. 
    return jsonify({"host_name": host_name, "host_ip": host_ip}) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
