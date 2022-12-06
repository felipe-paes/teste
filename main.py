from flask import Flask, render_template, request, url_for, redirect
import function, csv

app = Flask(__name__, template_folder='templates', static_folder='static')

def update():
    with open('hotel.csv', newline='') as file_in:
        reader = csv.DictReader(file_in)
        table = []
        for row in reader:
            table += [row]
        return table

@app.route('/')
def login():

	return render_template("login.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', table=update())


@app.route("/insert", methods=['GET', 'POST'])
def insertlayout():
    if request.method == 'POST':
        name = request.form['name']
        especie = request.form['especie']
        dono = request.form['dono']   
        function.insert(name, especie, dono)
        return redirect("/home")
    return render_template("insert.html")


@app.route("/remove", methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        i = request.form['i']
        function.remove(int(i))
        return redirect("/home")
    return render_template('remove.html')


@app.route("/alternate", methods=['GET', 'POST'])
def alternate():
    if request.method == 'POST':
        i = request.form['i']
        name = request.form['name']
        especie = request.form['especie']
        dono = request.form['dono']
        function.alternate(int(i), name, especie, dono)
        return redirect("/home")
    return render_template('alternate.html')

if __name__ == '__main__':
    app.run(debug=True)