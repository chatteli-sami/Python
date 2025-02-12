from flask import render_template, request, redirect
from flask_app.models.student import Student
from flask_app.models.teacher import Teacher
from flask_app import app


@app.route('/')
def index():
    s = Student.get_all()
    print(s)
    t = Teacher.get_all()
    print(t)
    return render_template('school.html')
