from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.database import Session
from models.models import Group, Student, Lesson

main_routes = Blueprint('main_routes', __name__)

# Головна сторінка
@main_routes.route('/')
def home():
    return render_template('main.html')

# Group management
# Операції з групами

# Сторінка для перегляду груп
# Перегляд груп доступний за посиланням /groups
# На сторінці /groups повинен бути список груп, які є в базі даних
@main_routes.route('/groups', methods=['GET'])
def view_groups():
    session = Session()
    groups = session.query(Group).all()
    session.close()
    return render_template('group/management.html', groups=groups)

# Сторінка для додавання групи
# Додавання групи доступно за посиланням /groups/add
# На сторінці /groups/add повинна бути форма для додавання групи
@main_routes.route('/groups/add', methods=['GET', 'POST'])
def add_group():
    session = Session()
    name = request.form.get('name')
    if name:
        group = Group(name=name)
        session.add(group)
        session.commit()
    session.close()
    return redirect(url_for('main_routes.view_groups'))

# Сторінка для перегляду групи
# Перегляд групи доступний за посиланням /groups/<group_id>
# На сторінці /groups/<group_id> повинна бути інформація про групу та список студентів, які входять до групи
@main_routes.route('/groups/<int:group_id>')
def view_group(group_id):
    session = Session()
    group = session.query(Group).get(group_id)
    students = session.query(Student).filter(Student.group.any(id=group_id)).all()
    session.close()
    return render_template('group/management.html', group=group, students=students)

# Student management
# Операції зі студентами

# Сторінка для перегляду студентів
# Перегляд студентів доступний за посиланням /students
# На сторінці /students повинен бути список студентів, які є в базі даних
@main_routes.route('/students', methods=['GET'])
def view_students():
    session = Session()
    students = session.query(Student).all()
    session.close()
    return render_template('student/management.html', students=students)

# Сторінка для додавання студента
# Додавання студента доступно за посиланням /students/add
# На сторінці /students/add повинна бути форма для додавання студента
@main_routes.route('/students/add', methods=['GET', 'POST'])
def add_student():
    session = Session()
    name = request.form.get('name')
    age = request.form.get('age')
    group_id = request.form.get('group_id')

    # Перевірка, чи ім'я та вік не є пустими
    # Якщо ім'я або вік є пустими, то виводимо повідомлення про помилку
    if not name or not age:
        flash("Ім'я та вік обов'язкові для заповнення")
        return redirect(url_for('main_routes.view_students'))
    
    # Перевірка, чи вік є числом
    # Якщо вік не є числом, то виводимо повідомлення про помилку
    try:
        age = int(age)
    except ValueError:
        flash('Вік повинен бути числом')
        return redirect(url_for('main_routes.view_students'))
    
    student = Student(name=name, age=age)
    # Додавання студента до групи
    # Якщо group_id не є пустим, то додаємо студента до групи
    if group_id:
        group = session.query(Group).get(int(group_id))
        # Перевірка, чи група існує
        # Якщо група не існує, то виводимо повідомлення про помилку
        if group:
            student.group.append(group)
        else:
            flash('Група не існує')
            return redirect(url_for('main_routes.view_students'))
    session.add(student)
    session.commit()
    session.close()
    return redirect(url_for('main_routes.view_students'))

# Lesson management
# Операції зі заняттями

# Сторінка для перегляду занять
# Перегляд занять доступний за посиланням /lessons
# На сторінці /lessons повинен бути список занять, які є в базі даних
@main_routes.route('/lessons')
def view_lessons():
    session = Session()
    lessons = session.query(Lesson).all()
    session.close()
    return render_template('lesson/management.html', lessons=lessons)

# Сторінка для додавання заняття
# Додавання заняття доступно за посиланням /lessons/add
# На сторінці /lessons/add повинна бути форма для додавання заняття
@main_routes.route('/lessons/add', methods=['GET', 'POST'])
def add_lesson():
    session = Session()
    name = request.form.get('name')
    description = request.form.get('description')
    if name:
        lesson = Lesson(name=name, description=description)
        session.add(lesson)
        session.commit()
    session.close()
    return redirect(url_for('main_routes.view_lessons'))