from databaseconfig import Session , Users,engine
from flask import Flask ,request,render_template,redirect,url_for,flash,session

app = Flask(__name__)
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/signup/',methods=['GET','POST'])
def sign():
    if request.method == 'POST':
        sessionDB = Session(engine)
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        user = Users (username = username , password = password , name = name)
        sessionDB.add(user)
        sessionDB.commit()
        return redirect(url_for('log'))
    else:
        return render_template('signup.html')
    
@app.route('/index/login/',methods=['GET','POST'])
def log():
    if request.method == 'POST':
        sessionDB = Session(engine)
        username = request.form['username']
        password = request.form['password']
        try:
            user = sessionDB.query(Users).filter_by(username=username).one()
            if user.password == password:
                session['id']=user.idusers
                return redirect(url_for('profil'))
        except:
            flash('user name or password is not correct ')
            return redirect(url_for('log'))
    else:
        return render_template('login.html')
    
@app.route('/login/main/')
def profil():
    if 'id' in session:
        session.pop('id',None)
        return 'mohamed'
        
    return redirect(url_for('log'))
if __name__ == '__main__':
    app.secret_key = 'super_'
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
   

