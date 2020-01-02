# Dojo Survey Server
# Neil Denning

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "fixed"


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/action", methods=['POST'])
def handle_form():
    session['data'] = {
        'user_name': request.form['user_name'],
        'dojo_location': request.form['dojo_location'],
        'favorite_language': request.form['favorite_language'],
        'experience': request.form['experience'],
        'gender': request.form['gender'],
        'comment': request.form['comment']}

    return redirect("/result")

@app.route("/result")
def show_result():
    print(session['data'])
    return render_template("results.html", result_data=session['data'])


@app.route("/home")
def go_back():
    return render_template("main.html")


if __name__=="__main__":
    app.run(debug=True)

