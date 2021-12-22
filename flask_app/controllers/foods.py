from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.config.mysqlconnection import query_db
from flask_app.models.food import Food
from flask_app.models.journal import Journal

@app.route("/newfood/<int:journal_id>", methods=["POST"])
def addfoodlist(journal_id):
    food_id = Food.insert(request.form)
    data = {"journal_id": journal_id, "food_id": food_id}
    Food.add_food_to_day(data)
    return redirect(f"/dates/{journal_id}")

@app.route("/foods/remove/<int:id>/<int:journal_id>")
def removefood(id, journal_id):
    data = {"id": id}
    Food.deletefoodfromday(data)
    return redirect(f"/dates/{journal_id}")

@app.route("/foods/delete/<int:id>/<int:journal_id>")
def deletefood(id, journal_id):
    data = {"id": id}
    Food.deletefoodfromday(data)
    Food.deletefood(data)
    return redirect(f"/dates/{journal_id}")

@app.route("/foods/add_to_day/<int:food_id>/<int:journal_id>")
def addtolist(food_id, journal_id):
    data = {"journal_id": journal_id, "food_id": food_id}
    Food.add_food_to_day(data)
    return redirect(f"/dates/{journal_id}")

@app.route("/foods/edit/<int:id>/<int:journal_id>")
def showedit(id, journal_id):
    day = Journal.show_day({"id": journal_id})
    food = Food.onefood({"id": id})
    return render_template("editfood.html", day = day, food = food)

@app.route("/foods/edit/<int:id>/<int:journal_id>", methods=["POST"])
def updatefood(id, journal_id):
    data = {
        "id": id,
        "category": request.form["category"],
        "name": request.form["name"],
        "calories": request.form["calories"]
    }
    Food.updatefood(data)
    return redirect(f"/dates/{journal_id}")
    
    
    

    
    
