from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.journal import Journal

@app.route("/")
def journal():
    dates = Journal.show_days()
    return render_template("index.html", dates = dates)

@app.route("/newentry")
def newentry():
    return render_template("newentry.html")

@app.route("/addentry", methods=["POST"])
def addentry():
    date = request.form["date"]
    print(date)
    if len(date) < 1:
        flash("Date is missing")
        return redirect("/newentry")
    else: 
        Journal.add_day(request.form)
        return redirect("/")
    
@app.route("/dates/<int:id>")
def showday(id):
    day = Journal.show_day(data = {"id": id})
    return render_template("showday.html", day = day)