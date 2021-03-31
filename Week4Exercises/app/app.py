import logging

from flask import Flask, request, render_template, make_response, redirect, abort

import security
from admin import admin
from database import DB

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
db = DB(app)
app.db = db
app.register_blueprint(admin)


@app.route("/login", methods=["POST"])
def login():
    user_data = db.login_query(request.form)
    if user_data:
        resp = redirect("/")
        # Set cookies to auth user
        session = security.create_session(user_data)
        cookie = security.create_cookie(session)
        resp.set_cookie("auth", cookie)
        resp.set_cookie("SameSite", "Strict")
        return resp
    abort(401, description="Login failed :( Invalid credentials, maybe")


@app.route("/logout")
def logout():
    resp = make_response("<script>window.location.href = '/';</script>")
    # Set cookie empty and expire it immediately
    resp.set_cookie("auth", "", expires=0)
    return resp


@app.route("/")
def index():
    session = security.get_session(request)
    if session and "username" in session:
        user = db.get_user(session["username"], session["secret"])
        return render_template("home.html", page="home", user=user)
    return render_template("index.html", page="root")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
