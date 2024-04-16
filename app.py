from flask import render_template, redirect, url_for, Blueprint
from mijn_project import app


app.app_context().push()




@app.route('/')
def index():  # put application's code here
    return render_template("home.html")















if __name__ == '__main__':
    app.run(debug=True)
