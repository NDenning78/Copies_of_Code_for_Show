# Belt Exam at "Coding Dojo"
# Neil Denning

from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL  
from flask_bcrypt import Bcrypt
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

'''
C - create - INSERT
R - read - SELECT
U - update - UPDATE
D - delete - DELETE
'''

app = Flask(__name__)
app.secret_key = "secret_key"
bcrypt = Bcrypt(app)
database = "belt_exam"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register_user():
    is_valid = True
    
    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("First name must be at least 2 characters long")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last name must be at least 2 characters long")
    if len(request.form['password']) < 3:
        is_valid = False
        flash("Password must be at least 3 characters long")
        
    if request.form['c_password'] != request.form['password']:
        is_valid = False
        flash("Passwords must match")

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please use a valid email address")
    
    if is_valid:
        pass_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL(database)

        query = "INSERT INTO users (first_name, last_name, email, password_hash, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pass_hash)s, NOW(), NOW())"
       
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],            
            'email': request.form['email'],
            'pass_hash': pass_hash,
        }
      
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id

        return redirect("/landing")
    else:
        return redirect("/")


@app.route("/login", methods=["POST"])
def login_user():
    is_valid = True

    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please enter your email")

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please use a valid email address")

    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please enter your password")
    
        
    if is_valid:
        mysql = connectToMySQL(database)
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        data = {
            'email': request.form['email']
        }
        user = mysql.query_db(query, data)
        if user:
            hashed_password = user[0]['password_hash']
            if bcrypt.check_password_hash(hashed_password, request.form['password']):
                session['user_id'] = user[0]['id']
                return redirect("/landing")
            else:
                flash("Password is invalid")
                return redirect("/")
        else:
            flash("Please use a valid email address")
            return redirect("/")
    else:
        return redirect("/")
            

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/landing")
def landing():
    if 'user_id' not in session:
        return redirect("/")

    mysql = connectToMySQL(database)
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {'user_id': session['user_id']}
    user = mysql.query_db(query, data)

    mysql = connectToMySQL(database)
    query = "SELECT * FROM quotes LEFT JOIN users ON quotes.user_id = users.id LEFT JOIN likes ON quotes.id = likes.quote_id ORDER BY quotes.created_at DESC"
    quotes = mysql.query_db(query)
    
    print("*"*20)
    print(quotes)

    mysql = connectToMySQL(database)
    query = "SELECT * FROM likes WHERE user_id = %(user_id)s"
    data = {
        'user_id': session['user_id']
    }
    is_liked = mysql.query_db(query,data)
    liked_quotes = []
    print("*"*20)
    print(is_liked)
    
    for liked in is_liked:
        liked_quotes.append(liked['quote_id'])
    print("*"*20)
    print(liked_quotes)

    return render_template("/landing.html", user=user[0], quotes=quotes, liked_quotes=liked_quotes)


@app.route("/save_quote", methods=["POST"])
def save_quote():
    if 'user_id' not in session:
        return redirect("/")

    is_valid = True
    if len(request.form['author']) < 3:
        is_valid = False
        flash("Author required")
    if len(request.form['quote_content']) < 10:
        is_valid = False
        flash("Quote required")  
    if is_valid:
        mysql = connectToMySQL(database)
        query = "INSERT INTO quotes (user_id, author, content, created_at, updated_at) VALUES (%(user_id)s, %(author)s, %(content)s, NOW(), NOW())"
        data = {'user_id': session['user_id'],
                'author': request.form['author'],
                'content': request.form['quote_content']
        }
        quote_id = mysql.query_db(query, data)
        return redirect("/landing")  
    else:
        return redirect("/landing")


@app.route("/quote_details/<quote_id>")
def quote_details(quote_id):
    mysql = connectToMySQL(database)
    query = "SELECT * FROM quotes LEFT JOIN users ON quotes.user_id = users.id WHERE quotes.id = %(quote_id)s"
    data = {'quote_id': quote_id}
    user = mysql.query_db(query, data)

    mysql = connectToMySQL(database)
    query = "SELECT * FROM quotes LEFT JOIN users ON quotes.user_id = users.id WHERE quotes.id = %(quote_id)s"
    data = {
        'quote_id': quote_id
    }
    quote = mysql.query_db(query, data)
    print(quote)

    return render_template("/quote_details.html", user=user[0], quote=quote)    


@app.route("/posted_by_quotes/<quote_user_id>")
def posted_by_quotes(quote_user_id):
    mysql = connectToMySQL(database)
    query = "SELECT * FROM users WHERE id = %(quote_user_id)s"
    data = {'quote_user_id': quote_user_id}
    user = mysql.query_db(query, data)


    mysql = connectToMySQL(database)
    query = "SELECT * FROM quotes LEFT JOIN users ON quotes.user_id = users.id WHERE quotes.user_id = %(quote_user_id)s"
    data = {
        'quote_user_id': quote_user_id
    }
    quotes = mysql.query_db(query, data)
    print(quotes)


    return render_template("/quotes.html", user=user[0], quotes=quotes)


@app.route("/edit/<user_id>")
def edit_user(user_id):
    mysql = connectToMySQL(database)
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {'user_id': session['user_id']}
    user = mysql.query_db(query, data)

    return render_template("edit.html", user=user[0])


@app.route("/update_user_info/<user_id>", methods=["POST"])
def update_user_info(user_id):
    is_valid = True

    if len(request.form['first_name']) < 1:
        is_valid = False
        flash("Please update your first name")

    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Please update your last name")
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please update your email")

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please use a valid email address")

    if is_valid:

        mysql = connectToMySQL(database)
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, created_at = NOW(), updated_at = NOW() WHERE users.id = %(user_id)s"
        data = {
            'user_id': user_id,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        mysql.query_db(query,data)

        return redirect("/landing")
    else:
        return redirect("/edit/<user_id>")


@app.route("/delete/<quote_id>")
def delete_quote(quote_id):
    mysql = connectToMySQL(database)
    query = "DELETE FROM quotes WHERE quotes.id = %(quote_id)s"
    data = {
        'quote_id': quote_id
    }    
    mysql.query_db(query, data)

    return redirect("/landing")


@app.route("/like/<quote_id>")
def like_message(quote_id):
    mysql = connectToMySQL(database)
    query = "INSERT INTO likes (user_id, quote_id, created_at, updated_at) VALUES (%(user_id)s, %(quote_id)s, NOW(), NOW())"
    data = {
        'user_id': session['user_id'],
        'quote_id': quote_id
    }
    likes_id = mysql.query_db(query, data)

    return redirect("/landing")


@app.route("/unlike/<quote_id>")
def unlike_message(quote_id):
    mysql = connectToMySQL(database)
    query = "DELETE FROM likes WHERE user_id = %(user_id)s AND quote_id = %(quote_id)s "
    data = {
        'user_id': session['user_id'],
        'quote_id': quote_id
    }
    mysql.query_db(query, data)

    return redirect("/landing")



if __name__=="__main__":
    app.run(debug=True)

# The END.