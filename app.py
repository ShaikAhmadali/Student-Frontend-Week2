from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#create Flask application
app = Flask(__name__)

#configure the SqLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

#Home Route
@app.route('/')
def home():
    return "Student REST API is Running"

@app.route('/home')
def index():
    return render_template('index.html')

# Create Student (POST API)
@app.route('/students', methods=['POST'])
def add_student():

    # Receive JSON data from Postman
    data = request.get_json()

    # Validation
    if not data:
        return jsonify({"error": "No data received"}), 400

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    if not data.get("age"):
        return jsonify({"error": "Age is required"}), 400

    if not data.get("course"):
        return jsonify({"error": "Course is required"}), 400

    # Create Student object
    student = Student(
        name=data["name"],
        age=data["age"],
        course=data["course"]
    )

    # Save into database
    db.session.add(student)
    db.session.commit()

    # Return success response
    return jsonify({
        "message": "Student added successfully!"
    }), 201

#-----------GET API-----------
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()

    student_list = []

    for student in students:
        student_list.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course
        })

    return jsonify(student_list)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404
    
    return jsonify({
    "id": student.id,
    "name": student.name,
    "age": student.age,
    "course": student.course
})

#----------PUT API----------
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    student = Student.query.get(id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    student.name = data["name"]
    student.age = data["age"]
    student.course = data["course"]

    db.session.commit()

    return jsonify({
        "message": "student updated successfully!"
    })

#---------DELETE API---------
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404
    
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({
        "message": "Student deleted successfully!"
    })


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)