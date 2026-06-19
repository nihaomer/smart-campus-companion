from flask import Flask, send_from_directory
import mysql.connector

app = Flask(__name__, static_folder='.')

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="smart_campus"
    )

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/users')
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"users": users}

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, request, jsonify

@app.route('/signup', methods=['POST'])
def signup():
    
    data = request.json
    username = data['username']
    email = data['email']
    password = data['password'] 
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "User registered successfully!"})
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401