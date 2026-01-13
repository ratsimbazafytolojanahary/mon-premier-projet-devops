from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = "db",
        database = "postgres",
        user = "postgres",
        password = "rft3055"
    )
    return conn

@app.route('/')
def home():
    return "<h1>Bienvenue sur mon API DevOps !</h1>"

@app.route('/status')
def status():
    try:
        # On utilise notre fonction de connexion
        conn = get_db_connection()
        cur = conn.cursor()
        
        # On demande la version à PostgreSQL
        cur.execute('SELECT version();')
        version = cur.fetchone()
        
        cur.close()
        conn.close()
        
        # On renvoie la réponse en format JSON (standard DevOps)
        return jsonify({
            "status": "online",
            "database_version": version[0],
            "message": "La connexion Python-PostgreSQL fonctionne !"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)