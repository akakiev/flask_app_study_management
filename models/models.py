from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Створюємо таблицю для зв'язку студентів і груп
student_group_assoc_table = Table('student_group', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)

# Створюємо таблицю для зв'язку груп і занять
group_lesson_assoc_table = Table('group_lesson', Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True),
    Column('lesson_id', Integer, ForeignKey('lessons.id'), primary_key=True)
)

# Створюємо моделі
# Класи моделей повинні успадковувати клас Base
# Кожен клас моделі повинен мати атрибути __tablename__ і id
# Атрибути __tablename__ вказує на назву таблиці в базі даних
# Атрибут id вказує на поле, яке буде первинним ключем
# Взаємозв'язки між моделями визначаються за допомогою атрибутів relationship
# Параметр back_populates вказує на атрибут, який вказує на зворотній зв'язок
# Параметр secondary вказує на таблицю, яка використовується для зв'язку двох таблиць
# Параметр primaryjoin вказує на умову, за якою відбувається зв'язок
# Параметр secondaryjoin вказує на умову, за якою відбувається зв'язок
# Параметр foreign_keys вказує на поля, за якими відбувається зв'язок
# Параметр viewonly вказує на те, що це поле не можна змінювати
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    
    group = relationship('Group', secondary=student_group_assoc_table, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"

# Група може мати багато студентів
# Група може мати багато занять
# Група може мати багато викладачів
# Група може мати багато аудиторій
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship('Student', secondary=student_group_assoc_table, back_populates='group')
    lessons = relationship('Lesson', secondary=group_lesson_assoc_table, back_populates='groups')   

    def __repr__(self):
        return f"<Group(id={self.id}, name='{self.name}')>"

# Заняття може бути в багатьох групах
# Заняття може мати багато викладачів
# Заняття може мати багато аудиторій
# Заняття може мати багато студентів 
class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    groups = relationship('Group', secondary=group_lesson_assoc_table, back_populates='lessons')

    # Перевизначення методу __repr__ для зручного виведення об'єктів
    # Метод __repr__ викликається при використанні функції print
    # Наприклад, print(lesson)
    def __repr__(self):
        return f"<Lesson(id={self.id}, name='{self.name}', description='{self.description}')>"