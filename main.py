from flask import Flask, redirect, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('login.html')

@app.route('/results', methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        id = request.form["id"]
        subject = request.form["subject"]
        first = request.form["first"]
        second = request.form["second"]
        third = request.form["third"]
        sashualo = (int(first) + int(second) + int(third))/3
        average = round(sashualo, 1)
        res = 'Passed'
        if average < 4:
            res = 'Failed'

        with sql.connect("students.db") as con:
            cur = con.cursor()
            cur.execute('create table if not exists moswavleebi(name, id, subject, first, second, third, average, result)')
            cur.execute("INSERT INTO moswavleebi(name, id, subject, first, second, third, average, result) VALUES (?,?,?,?,?,?,?,?)",(name,id,subject,first,second,third,average,res))            
            con.commit()  
            return redirect(url_for('results'))    
        con.close()

@app.route('/database', methods=['POST', 'GET'])
def results():
        con = sql.connect("students.db")
        
        cur = con.cursor()
        x = cur.execute("select * from moswavleebi")
        
        rows = x.fetchall()
        saxeli = []
        piradi =[]
        sagani = []
        davaleba1 = []
        davaleba2 = []
        davaleba3 = []
        sashualo = []
        result = []
        dict = {'name': saxeli, 'id': piradi, 'subject': sagani, 'first': davaleba1, 'second': davaleba2, 'third': davaleba3, 'average': sashualo, 'result': result}
        for i in rows:
            dict['name'].append(i[0])
            dict['id'].append(i[1])
            dict['subject'].append(i[2])
            dict['first'].append(i[3])
            dict['second'].append(i[4])
            dict['third'].append(i[5])
            dict['average'].append(i[6])
            dict['result'].append(i[7])
        print(dict)
        return render_template("results.html",data = rows)

@app.route('/student', methods=['POST', 'GET'])
def student():
    if request.method == 'POST':
        with sql.connect("students.db") as con:
            con = sql.connect("students.db")           
            cur = con.cursor()
            y = request.form["search"]
            x = cur.execute(f"select * from moswavleebi where id={y}")
            print(x)
    return render_template('one.html')

        

if __name__ == '__main__':
    app.run(debug=True)

