from flask import *
from flask_sqlalchemy import *

import pandas as pd
import os

UPLOAD_FOLDER = os.path.join('csv_files')
 
ALLOWED_EXTENSIONS = {'csv'}
        
app = Flask(__name__)

app.secret_key = 'secret123'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def upload():
    session['uploaded_files'] = ''
    if request.method == 'POST':
        files = request.files.getlist("file")
        file = Dataset.query.filter_by(id).first_or_404()
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            session['uploaded_files'] += os.path.join(app.config['UPLOAD_FOLDER'], file.filename+' ')
        return render_template('success.html', files=files)
    return render_template("index.html")
 
 
@app.route('/show')
def show():
    htmls = []
    data_session = session.get('uploaded_files')
    files = data_session.split(' ')[0:-1]
    for file in files:
        filedir = pd.read_csv(file, error_bad_lines=False, engine="python", encoding='unicode_escape')
        file_to_html = filedir.to_html()
        htmls.append(file_to_html) 
    return render_template('read.html', htmls=htmls)
 
 
if __name__ == '__main__':
    app.run(debug=True)