from flask import Flask, jsonify
import mysql.connector
import socket
import os

app = Flask(__name__)

def get_db_info():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")
    db_name = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return db_name, os.getenv('DB_HOST')

@app.route('/')
def index():
    db_name, db_ip = get_db_info()
    web_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({
        'db_name': db_name,
        'db_ip': db_ip,
        'web_server_ip': web_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
