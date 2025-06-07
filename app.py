from flask import Flask, request, jsonify, send_from_directory
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0804'
app.config['MYSQL_DB'] = 'campus_drive'

mysql = MySQL(app)

@app.route('/students', methods=['GET'])
def get_all_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    result = []
    for student in students:
        result.append({
            'id': student[0],
            'name': student[1],
            'department': student[2],
            'year': student[3]
        })
    return jsonify({"students": result})

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    required_fields = ['id', 'name', 'department', 'year']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required field"}), 400
    
    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO students (id, name, department, year) VALUES (%s, %s, %s, %s)",
                    (data['id'], data['name'], data['department'], data['year']))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Student created", "student": data}), 201
    except Exception as e:
        mysql.connection.rollback()
        cur.close()
        return jsonify({"error": str(e)}), 400

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    if not cur.fetchone():
        cur.close()
        return jsonify({"error": "Student not found"}), 404
    
    try:
        updates = []
        values = []
        for key, value in data.items():
            if key in ['name', 'department', 'year']:
                updates.append(f"{key} = %s")
                values.append(value)
        if not updates:
            cur.close()
            return jsonify({"error": "No valid fields to update"}), 400
        query = f"UPDATE students SET {', '.join(updates)} WHERE id = %s"
        values.append(student_id)
        cur.execute(query, tuple(values))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Student updated"})
    except Exception as e:
        mysql.connection.rollback()
        cur.close()
        return jsonify({"error": str(e)}), 400

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    if cur.rowcount == 0:
        cur.close()
        return jsonify({"error": "Student not found"}), 404
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(debug=True)
