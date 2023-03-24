from flask import *
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import os

#--Определяем папку хранения csv-файлов и расширение для загрузки
UPLOAD_FOLDER = os.path.join('csv_files')
ALLOWED_EXTENSIONS = {'csv'}

#--Конфиги, подключение к SQLite
app = Flask(__name__)
app.secret_key = 'secret123'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datasets.db'

#--Определяем ОРМ как SQLAlchemy 
db = SQLAlchemy(app)

#--Создаем "модель" для хранения имён csv-файлов
class DataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

#--Отображение/удаление датасетов из БД 
@app.route('/', methods=['GET', 'POST'])
def delete():
    try:
        datasets = DataSet.query.all()
     
        if request.method == 'POST':
            db.session.query(DataSet).delete()
            db.session.commit()
            return render_template('index.html')
    except:
        return render_template('index.html', datasets=datasets)    
    else:   
        return render_template('index.html', datasets=datasets)
    
#--Загрузка датасетов в БД
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        datasets = DataSet.query.all()
        if request.method == 'POST':
            names = []
            files = request.files.getlist("file")
            for file in files:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                names.append(file.filename)
            for name in names:
                dataset = DataSet(name=name)
                if not db.session.query(db.session.query(DataSet).filter_by(name=name).exists()).scalar():
                    db.session.add(dataset)
                    db.session.commit()
            datasets = DataSet.query.all()
            return render_template('success.html', datasets=datasets)
    except:
        return render_template('upload.html', datasets=datasets)    
    else:   
        return render_template('upload.html', datasets=datasets)

#--Отображение csv в виде таблиц на html
@app.route('/upload/<int:id>')
def show(id):
    dataset = DataSet.query.get(id)
    file_name = (DataSet.query.filter_by(id=dataset.id).first().name)
    file = (os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    file_pd = pd.read_csv(file, error_bad_lines=False, engine="python", encoding='unicode_escape')
    file_to_html = file_pd.to_html()

    return render_template('read.html', file_to_html=file_to_html)


if __name__ == '__main__':
    app.run(debug=True)