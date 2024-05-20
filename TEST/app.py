from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, flash
db = SQL('sqlite:///users.db')
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
if __name__ == "__main__":
    app.run(debug=True, port=6000)