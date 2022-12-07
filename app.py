from flask import Flask, render_template, request, url_for, redirect
import function, csv

app = Flask(__name__)

def formulario():
    tasks = []
    with open('hotel.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        first_line = True
        for row in reader:
            if not first_line:
                tasks.append({
                    "name": row[0],
                    "especie": row[1],
                    "dono": row[2],
                })
            else:
                first_line = False
    return tasks

@app.route('/')
def login():

	return render_template("login.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', tasks=formulario())


@app.route("/insert", methods=['GET', 'POST'])
def insertlayout():
    if request.method == 'POST':
        name = request.form['name']
        especie = request.form['especie']
        dono = request.form['dono']   
        function.insert(name, especie, dono)
        return redirect("/home")
    return render_template("insert.html")


@app.route("/deletar", methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        i = request.form['i']
        function.deletar(int(i))
        return redirect("/home")
    return render_template('deletar.html')


@app.route("/alterar", methods=['GET', 'POST'])
def alterar():
    if request.method == 'POST':
        i = request.form['i']
        name = request.form['name']
        especie = request.form['especie']
        dono = request.form['dono']
        function.alterar(int(i), name, especie, dono)
        return redirect("/home")
    return render_template('alterar.html')

app.run(debug=True)