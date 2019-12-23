# Dojo Tweets
# Neil Denning


from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt   
from datetime import datetime 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "nrd_key"
bcrypt = Bcrypt(app) 
database = "dojo_tweets_2"

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
    if len(request.form['password']) < 2:
        is_valid = False
        flash("Password must be at least 2 characters long")
    if request.form['c_password'] != request.form['password']:
        is_valid = False
        flash("Passwords must match")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please use a valid email address")
    
    if is_valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL(database)

        query = "INSERT into users (first_name, last_name, email, password_hash, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, %(pass)s, NOW(), NOW())"

        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'email': request.form['email'],
            'pass': pw_hash
            
        }

        user_id = mysql.query_db(query, data) 
        session['user_id'] = user_id  


        return redirect("/success")
    else: 
        return redirect("/")

@app.route("/login", methods=["POST"])
def login_user():
    is_valid = True

    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please enter your email")
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
                return redirect("/success")
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


@app.route("/success")
def landing():
    if 'user_id' not in session:
        return redirect("/")

    mysql = connectToMySQL(database)
    query = "SELECT * FROM users WHERE users.id = %(id)s"
    data = {'id': session['user_id']}
    user = mysql.query_db(query, data)

    mysql = connectToMySQL(database)
    query = "SELECT tweets.user_id, tweets.id as tweet_id, users.first_name, tweets.content, tweets.created_at, COUNT(tweet_id) as times_liked FROM liked_tweets RIGHT JOIN tweets ON tweets.id = liked_tweets.tweet_id JOIN users ON tweets.user_id = users.id GROUP BY tweets.id ORDER BY tweets.created_at DESC;"
    tweets = mysql.query_db(query)



    mysql = connectToMySQL(database)
    query = "SELECT * FROM liked_tweets WHERE user_id = %(user_id)s"
    data = {
        'user_id': session['user_id']
    }
    liked_tweets = [tweet['tweet_id'] for tweet in mysql.query_db(query, data)]

    for tweet in tweets:
        time_since_posted = datetime.now() - tweet['created_at']
        days = time_since_posted.days
        hours = time_since_posted.seconds//3600 
        minutes = (time_since_posted.seconds//60)%60
        if tweet['tweet_id'] in liked_tweets:
            tweet['already_liked'] = True
        else:
            tweet['already_liked'] = False

        tweet['time_since_posted'] = (days, hours, minutes)
        
    return render_template("landing.html", user=user[0], tweets=tweets)


@app.route("/tweets/create", methods=['POST'])
def save_tweet():
    if 'user_id' not in session:
        return redirect("/")
        
    is_valid = True
    if len(request.form['content']) < 1:
        is_valid = False
        flash('Tweet cannot be blank')
    if len(request.form['content']) > 256:
        is_valid = False
        flash('Tweet cannot be more than 255 characters')
    
    if is_valid:
        mysql = connectToMySQL(database)
        query = "INSERT INTO tweets ( user_id, content, created_at, updated_at) VALUES ( %(id)s, %(cont)s, NOW(), NOW())"
        data = {'id': session['user_id'],
                'cont': request.form['content']}
        tweet = mysql.query_db(query, data)
    
    return redirect("/success")


@app.route("/tweets/<tweet_id>/add_like")
def like_tweet(tweet_id):
    mysql = connectToMySQL(database)
    query = "INSERT INTO liked_tweets (user_id, tweet_id) VALUES (%(user_id)s, %(tweet_id)s)"
    data = {
        'user_id': session['user_id'],
        'tweet_id': tweet_id
    }    
    mysql.query_db(query, data)
    return redirect("/success")


@app.route("/tweets/<tweet_id>/unlike")
def unlike_tweet(tweet_id):
    mysql = connectToMySQL(database)
    query = "DELETE FROM liked_tweets WHERE user_id = %(user_id)s AND tweet_id = %(tweet_id)s"
    data = {
        'user_id': session['user_id'],
        'tweet_id': tweet_id
    }
    
    mysql.query_db(query, data)
    return redirect("/success")


@app.route("/tweets/<tweet_id>/delete")
def delete_tweet(tweet_id):
    mysql = connectToMySQL(database)
    # if ON DELETE CASCADE is not set up for tweets DELETE likes first
    query = "DELETE FROM liked_tweets WHERE tweet_id = %(tweet_id)s"
    data = {
        'tweet_id': tweet_id
    }    
    mysql.query_db(query, data)

    mysql = connectToMySQL(database)
    query = "DELETE FROM tweets WHERE id = %(tweet_id)s"    
    mysql.query_db(query, data)
    return redirect("/success")


@app.route("/tweets/<tweet_id>/edit")
def edit_tweet(tweet_id):
    if 'user_id' not in session:
        flash("You cannot edit tweets that are not yours.")
        return redirect("/")

    mysql = connectToMySQL(database)
    query = "SELECT * FROM tweets WHERE id = %(tid)s"
    data = {'tid': tweet_id}    
    query_result = mysql.query_db(query, data)
    return render_template("edit_tweet.html", tweet=query_result[0])


@app.route("/tweets/<tweet_id>/update", methods=['POST'])
def update_tweet(tweet_id):
    if 'user_id' not in session:
        flash("You cannot edit tweets that are not yours.")
        return redirect("/")
        
    is_valid = True
    if len(request.form['content']) < 1:
        is_valid = False
        flash('Tweet cannot be blank')
    if len(request.form['content']) >= 256:
        is_valid = False
        flash('Tweet cannot be more than 255 characters')
    
    if is_valid:
        query = "UPDATE tweets SET content = %(cont)s, updated_at = NOW()"
        data = {'cont': request.form['content']}
        mysql = connectToMySQL('dojo_tweets')
        result = mysql.query_db(query, data)
        flash('Tweet successfully updated')
        return redirect("/success")
    else:
       return redirect("/tweets/{}/edit".format(tweet_id)) 



if __name__ == "__main__":
    app.run(debug=True)


