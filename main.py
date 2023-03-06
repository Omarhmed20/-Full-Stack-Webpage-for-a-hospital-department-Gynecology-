from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Hanan737398366",
  database="Try1"
)
mycursor = mydb.cursor()

@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/contact')
def contact():
    


   return render_template('contact.html')

@app.route('/')
def login():
    # if doctor ... return render_template('viewAppointment.html')
    # if admin ... return render_template('Admin.html')
    # if patient ... return render_template('bookAppointment.html')


   return render_template('login.html')


@app.route('/bookAppointment')
def bookAppointment():
    if request.method == 'POST': 
        pfirstname = request.form['pfirstname']
        plastname = request.form['plastname']
        date = request.form['date']
        time = request.form['time']
        admin_id = request.form['admin_id']
        symptoms = request.form['symptoms']
        urgency = request.form['urgency']
        #sql = "INSERT INTO conact (email,name,message) VALUES (%s,%s,%s)"
        #val= (email,name,message)
        #mycursor.execute(sql, val)
        #myd.commit()
        return render_template('index.html')
    else:
        return render_template('bookAppointment.html')
    


   


@app.route('/signup',methods = ['POST', 'GET'])
def signup():
    if request.method == "POST":
        role = request.form['role']
        if role == "Doctor":
            return render_template("signupDoctor.html")
            return render_template("signupPatient.html")

    return render_template("signup.html")    





@app.route('/signupDoctor')
def signupDoctor():
    


   return render_template('signupDoctor.html')

@app.route('/signupPatient')
def signupPatient():
    


   return render_template('signupPatient.html') 

@app.route('/addentry')
def addentry():
    


   return render_template('Add Entry.html')

@app.route('/admin')
def Admin():
    


   return render_template('Admin.html')    

@app.route('/viewAppointment')
def viewAppointment():
    #feha moshkla be2ol "'data' is undefined"


   return render_template('viewAppointment.html')  

@app.route('/viewData')
def viewData():
    #to view rooms or patients or doctors or appointment


   return render_template('viewData.html')



if __name__ == '__main__':
   app.run()