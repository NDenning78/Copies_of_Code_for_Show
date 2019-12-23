# Dojo Survey Server
# Neil Denning

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "fixed"


@app.route("/")
def index():
    return render_template("dojoSurveyFixed_main_index.html")

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
    return render_template("dojoSurveyFixed_results_index.html", result_data=session['data'])


@app.route("/home")
def go_back():
    return render_template("dojoSurveyFixed_main_index.html")


if __name__=="__main__":
    app.run(debug=True)



'''<<<<<
Flask.redirect(location, statuscode, response)

"location" = URL where response should be directed.

"statuscode" = statuscode sent to browser's header.

"response" = response parametwer used to instantiate response.

"Statuscodes"

STATUS CODES

HTTP_300_MULTIPLR_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED

FLASK.ABORT(CODE)

400_BAD_REQUEST
401_UNATHENTICATED
403_FORBIDDEN
404_NOT_FOUND
406_NOT_ACCEPTABLE
415_UNSOPPORTED_MEDIA_TYPE
429_TOO_MANY_REQUESTS



"host" = hostname to listen to. Defaults to 127.0..0.1 (localhost).
Set to '0.0.0.0' to have server available externally.

"port" = defaults to 5000. this can be changed as well.

"debug" = defaults to false. if set to true, provides debug information.

"options" = to be forwarded to underlying Werkzeug server,

"HTTP Protocol Methods" <<<<<

"GET" = Sends data in unencrypted form to server

"HEAD" = Same as GET, but without response body

"POST" = Used to send HTML form data to server.

"PUT" = Replaces all current representations of target resource with uploaded content.

"DELETE" = Removes all current representations of target resource given by URL.



"additional parameters" <<<<<

"int" = accepts integer

"float" = for floating point value

"path" = accepts slashes uswed as directory separator

"JINJA template engine uses the following delimiters for escaping from HTML"

{%...%} for Statements

{{...}} for Expressions to print to the template output

{#...#} for Comments not included in the template output

#...## for Line Statements


"REQUEST OBJECT"

"Form" = Dictionary object containing key-value pairs of form parameters and values.

"args" = Parsed contents of query string which i spart of URL after question mark(?)

"Cookies" = Dictionary object holding Cookie names and values. Helps with tracking data.

"files" = Data pertaining to the upload file.

"Method" = Current request method.



'''
