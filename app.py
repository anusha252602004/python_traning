from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'roottoor'
app.config['MYSQL_DB']= 'anusha_ece'
mysql = MySQL(app)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/myname')
def printMyname():
    return "your name"

@app.route('/home')
def loadHomeHtml():
    return render_template("home.html")

@app.route('/about')
def loadAboutHtml():
    return render_template("about.html")

@app.route('/contact')
def loadContactHtml():
    return render_template("contact.html")

@app.route('/user_detail')
def userDetail():
    sql ="SELECT*FROM people"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results= cur.fetchall()
    print(results)
    cur.close()
    return jsonify(results)

@app.route('/register_form',methods=['GET'])
def register_form():
    return render_template("register.html")


@app.route("/add",methods= ["POST"])
def addUser():
    id = request.form['id']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    sql = "insert into people(id,email,password) values(%s,%s,%s)"
    val = [id,email,password]
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return"register success"

@app.route("/update",methods= ["POST"])
def update():
    id = request.form['id']
    email = request.form['email']
    cur = mysql.connection.cursor()
    sql = "update people set email=%s where id=%s"
    val = [email,id]
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return"update success"

@app.route("/update_form",methods= ["GET"])
def update_form():
    return render_template("update.html")

@app.route("/delete",methods= ["POST"])
def delete():
    id = request.form['id']
    cur = mysql.connection.cursor()
    sql = "delete from people where id=%s"
    val = [id]
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return"delete success"
@app.route("/delete_form",methods= ["GET"])
def delete_form():
    return render_template("delete.html")

@app.route("/myweb",methods= ["GET"])
def myweb():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

