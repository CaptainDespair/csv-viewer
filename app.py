from flask import *
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import os

UPLOAD_FOLDER = os.path.join('csv_files')

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.secret_key = 'secret123'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datasets.db'

db = SQLAlchemy(app)

class DataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        names = []
        files = request.files.getlist("file")
        for file in files: 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            # session['uploaded_files'] += os.path.join(app.config['UPLOAD_FOLDER'], file.filename+' ')
            names.append(file.filename)
        try:
            for name in names:
                dataset = DataSet(name=name)
                if not db.session.query(db.session.query(DataSet).filter_by(name=name).exists()).scalar():
                    db.session.add(dataset)
                    db.session.commit()
            return render_template('success.html', files=files)
        except (KeyboardInterrupt):
            return 'Ошибка'
    else:
        return render_template('index.html')
    
#     # session['uploaded_files'] = ''
#     # if request.method == 'POST':
#     #     files = request.files.getlist("file")
#     #     for file in files:
#     #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#     #         session['uploaded_files'] += os.path.join(app.config['UPLOAD_FOLDER'], file.filename+' ')
#     #     return render_template('success.html', files=files)
    #return render_template("index.html")
 
@app.route('/show/<string:name>')
def show():
    datasets = DataSet.query.all()

    data_session = session.get('uploaded_files')
    file = (os.path.join(app.config['UPLOAD_FOLDER'], db.session.query(DataSet).filter_by(id=id)))
    filedir = pd.read_csv(file, error_bad_lines=False, engine="python", encoding='unicode_escape')
    file_to_html = filedir.to_html()
    return render_template('read.html', datasets=datasets)

if __name__ == '__main__':
    app.run(debug=True)