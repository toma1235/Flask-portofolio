from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,request, redirect



app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'
    
#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    
    return render_template('index.html', button_python=button_python, button_discord=button_discord)
        
@app.route('/feedback', methods=['POST'])
def process_FEEDBACK():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        toma = Feedback(email=email, text=text)
        db.session.add(toma)
        db.session.commit()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)