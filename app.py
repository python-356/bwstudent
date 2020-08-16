from flask import Flask, render_template, request, redirect, url_for
import config
from exts import db
from models import Student

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# 显示所有学生信息
@app.route('/')
def index():

    context = {
        "students": Student.query.all()
    }

    return render_template('index.html', **context)


# 查找符合搜索框中的学生信息
@app.route('/info/', methods=['POST'])
def findSrudent():
    if request.method == 'POST':
        name = request.form.get('str')
        context = {
            "students": Student.query.filter_by(name=name)
        }
        return render_template('student_info.html', **context)


# 添加学生信息
@app.route('/add/', methods=['GET','POST'])
def addSrudent():
    if request.method == 'GET':
        return render_template('student_add.html')
    else:
        name = request.form.get('name')
        english = request.form.get('english')
        python = request.form.get('python')
        c = request.form.get('c')

        stu = Student()
        stu.name = name
        stu.English = english
        stu.Python = python
        stu.C = c
        stu.Total_score = int(english) + int(python) + int(c)
        db.session.add(stu)
        db.session.commit()

        return redirect(url_for('index'))




# 修改学生信息
@app.route('/update/<id>', methods=['GET','POST'])
def updateSrudent(id):
    if request.method == 'GET':
        print("id::", id)
        context = { "ids":id}

        return render_template('student_update.html', **context)
    else:
        print("id::", id)
        name = request.form.get('name')
        english = request.form.get('english')
        python = request.form.get('python')
        c = request.form.get('c')

        Student.query.filter_by(id=id).update({'name': name, 'English': english, 'Python':python, 'C':c, 'Total_score':int(english) + int(python) + int(c)  })
        db.session.commit()

        return render_template('index.html')


# 删除学生信息
@app.route('/delete/<id>', methods=['GET'])
def deleteSrudent(id):

    students = Student.query.filter_by(id=id).first()
    db.session.delete(students)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
